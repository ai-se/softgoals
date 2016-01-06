from __future__ import print_function, division
import sys, os, time
sys.path.append(os.path.abspath("."))
__author__ = 'george'
sys.dont_write_bytecode = True
from utilities.lib import *
from pystar.models.CSServices import graph as cs_agent_sr_graph
from pystar.model import Model
import pystar.template as template
from utilities.de import DE, Point
from utilities.plotter import med_spread_plot
from pystar.models.dot_models import *
from prettytable import PrettyTable

def default():
  return O(
    k1 = 100,
    k2 = 100
  )

class Decision(O):
  def __init__(self, **params):
    O.__init__(self, **params)

class Star1(O):
  def __init__(self, model, **settings):
    O.__init__(self)
    self.model = model
    #self.model.bases.extend(self.get_conflicts());self.model.assign_costs()
    self.settings = default().update(**settings)
    self.de = DE(model, gens = self.settings.k1)


  def get_conflicts(self):
    model = self.model
    graph = model.get_tree()
    nodes = []
    for node in graph.get_nodes():
      if node.type == "softgoal" and len(node.from_edges) > 1:
        toggle = None
        for edge_id in node.from_edges:
          edge = graph.get_edge(edge_id)
          if edge.type == "contribution":
            temp_toggle = sign(template.Edge.get_contribution_weight(edge.value))
            if toggle is None: toggle = temp_toggle
            if temp_toggle != toggle:
              nodes.append(node)
              break
    return nodes

  def sample(self):
    stat = self.de.run()
    stat.tiles()
    best = set()
    for obj_index in range(len(self.de.settings.obj_funcs)):
      sorted_pop = sorted(stat.generations[-1], key=lambda x: x.objectives[obj_index], reverse=True)[:len(stat.generations[-1])//5]
      best.update(sorted_pop)
    rest = set()
    for gen in stat.generations:
      for point in gen:
        if not point in best:
          rest.add(point)
    return best, rest

  def rank(self, best, rest):
    # TODO - Change this method to include the value along with the decision
    best_size = len(best)
    rest_size = len(rest)
    p_best = best_size / (best_size + rest_size)
    p_rest = rest_size / (best_size + rest_size)
    decisions = []
    for dec_node in self.model.bases:
      f_best, pos_count, neg_count = 0, 0, 0
      for point in best:
        if point.decisions[dec_node.id] > 0:
          pos_count += 1
        elif point.decisions[dec_node.id] < 0:
          neg_count += 1
      node_value = 1 if pos_count > neg_count else -1
      f_best = max(pos_count, neg_count)
      f_best /= best_size
      l_best = f_best * p_best
      f_rest = 0
      func = gt if node_value == 1 else lt
      for point in rest:
        if func(point.decisions[dec_node.id], 0):
          f_rest += 1
      f_rest /= best_size
      l_rest = f_rest * p_rest
      sup_best = l_best**2 / (l_best + l_rest)
      decisions.append(Decision(id = dec_node.id, name = dec_node.name,
                                support=sup_best, value = node_value,
                                type = dec_node.type, container=dec_node.container,
                                cost = self.model.cost_map[dec_node.id]))
    decisions.sort(key=lambda x:x.support, reverse=True)
    return decisions

  def generate(self, presets = None):
    population = list()
    while len(population) < self.settings.k2:
      point = Point(self.model.generate())
      if not point in population:
        population.append(point)
    for point in population:
      for preset in presets:
        point.decisions[preset.id] = preset.value
    return population

  def objective_stats(self, generations):
    stats = []
    for i in range(len(self.de.settings.obj_funcs)):
      data_map = {}
      meds = []
      iqrs = []
      for gen, pop in enumerate(generations):
        objs = [pt.objectives[i] for pt in pop]
        med, iqr = median_iqr(objs)
        meds.append(med)
        iqrs.append(iqr)
      data_map["meds"] = meds
      data_map["iqrs"] = iqrs
      stats.append(data_map)
    return stats

  def evaluate(self, point, decisions):
    model = self.model
    if not point.objectives:
      model.reset_nodes(point.decisions)
      point.objectives = [func(model) for func in self.de.settings.obj_funcs[:2]]
      point.objectives.append(sum(decision.cost for decision in decisions if decision.value > 0))
      point._nodes = [node.clone() for node in model.get_tree().get_nodes()]
    return point.objectives

  def prune(self, support):
    gens = []
    for i in range(len(support)):
      decisions = support[:i]
      population = self.generate(decisions)
      for point in population:
        self.evaluate(point, decisions)
        # TODO - Mark Best objective model here
        #self.de.settings.evaluation(point, self.model, self.de.settings.obj_funcs)
      gens.append(population)
    obj_stats = self.objective_stats(gens)
    return obj_stats, gens

  def report(self, stats, subfolder):
    headers = [obj.__name__.split("_")[-1] for obj in self.de.settings.obj_funcs]
    med_spread_plot(stats, headers, fig_name="img/"+subfolder+"/"+self.model.get_tree().name+".png")

  def get_elbow(self, gens, index, obj_index=None):
    pop = gens[index]
    pop = sorted(pop, key=lambda x: x.objectives[obj_index])
    point = pop[len(pop)//2]
    return point

def print_decisions(decisions):
  columns = ["rank", "name", "type", "value", "cost"]
  table = PrettyTable(columns)
  for i, decision in enumerate(decisions):
    row = [i+1, decision.name, decision.type, decision.value, decision.cost]
    table.add_row(row)
  print("")
  print(table)

def run(graph, subfolder, index = None):
  #graph = DelayModeratedBulletinBoard()
  #model = Model(cs_agent_sr_graph)
  start = time.time()
  model = Model(graph)
  print("## %s"%graph.name)
  print("```")
  star = Star1(model)
  best, rest = star.sample()
  decisions = star.rank(best, rest)
  obj_stats, gens = star.prune(decisions)
  delta = time.time() - start
  star.report(obj_stats, subfolder)
  print("```")
  print("### Time Taken : %s"%delta)
  print("![1](../../../src/img/%s/%s.png)"%(subfolder,graph.name))
  print("```")
  print_decisions(decisions)
  print("```")
  if index is not None:
    print("### Top %d Decisions from above table."%index)
    print("```")
    point = star.get_elbow(gens, index, obj_index = 0)
    columns = ["name", "type", "value"]
    table = PrettyTable(columns)
    for node in point.get_nodes():
      row = [node.name, node.type, node.value]
      table.add_row(row)
    print(table)
    print("```")
