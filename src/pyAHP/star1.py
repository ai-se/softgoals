from __future__ import print_function, division
import sys, os, time
sys.path.append(os.path.abspath("."))
__author__ = 'panzer'
from utilities.lib import *
from de import DE
from pyAHP.model import Model, Point
from utilities.nsga2 import select as sel_nsga2
from utilities.plotter import med_spread_plot, line_plot, point_plot, point_plot_3d
from prettytable import PrettyTable
import csv
from pyAHP.dotter import Grapher, Recommender

def default():
  return O(
    k1 = 10,
    k2 = 100,
    best_percent = 33,
    gen_step = 2
  )

class Decision(O):
  def __init__(self, **params):
    O.__init__(self, **params)

  def __hash__(self):
    return hash(self.id)

class Star1(O):
  def __init__(self, model, **settings):
    O.__init__(self)
    self.model = model
    self.settings = default().update(**settings)
    self.de = DE(model, gens = self.settings.k1)

  # def sample(self, sub_folder):
  #   stat = self.de.run()
  #   self.to_csv(stat, "csv/"+sub_folder+"/"+self.model.get_tree().name+".csv")
  #   stat.settings.gen_step = self.settings.gen_step
  #   stat.tiles()
  #   population = set()
  #   for point in stat.generations[0]:
  #     population.add(point)
  #   for point in stat.generations[-1]:
  #     population.add(point)
  #   best_size = int(len(population) * self.settings.best_percent/100)
  #   best = sel_nsga2(self.model, list(population), best_size)
  #   rest = population - set(best)
  #   return best, list(rest)

  def sample(self, sub_folder):
    stat = self.de.run()
    self.to_csv(stat, "csv/"+sub_folder+"/"+self.model.get_tree().name+".csv")
    stat.settings.gen_step = self.settings.gen_step
    stat.tiles()
    best = set()
    population = set()
    for point in stat.generations[0]:
      population.add(point)
    for point in stat.generations[-1]:
      population.add(point)
    for obj_index in range(len(self.de.settings.better)):
      sorted_pop = sorted(list(population), key=lambda x: x.objectives[obj_index], reverse=True)[:len(stat.generations[-1])//5]
      best.update(sorted_pop)
    rest = population - best
    return list(best), list(rest)

  def rank(self, best, rest):
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
      f_pos_best = pos_count / best_size
      l_pos_best = f_pos_best * p_best
      f_neg_best = neg_count / best_size
      l_neg_best = f_neg_best * p_best
      f_pos_rest, f_neg_rest = 0, 0
      for point in rest:
        if point.decisions[dec_node.id] > 0:
          f_pos_rest += 1
        else:
          f_neg_rest += 1
      f_pos_rest /= rest_size
      f_neg_rest /= rest_size
      l_pos_rest = f_pos_rest * p_rest
      l_neg_rest = f_neg_rest * p_rest
      if l_pos_best == 0 and l_pos_rest == 0:
        sup_pos = 0
      else:
        sup_pos = l_pos_best ** 2 / (l_pos_best + l_pos_rest)
      if l_neg_best == 0 and l_neg_rest == 0:
        sup_neg = 0
      else:
        sup_neg = l_neg_best ** 2 / (l_neg_best + l_neg_rest)
      decisions.append(Decision(id = dec_node.id, name = dec_node.name,
                                support=sup_pos, value = 1,
                                type = dec_node.type, container=dec_node.container,
                                cost = dec_node.base_cost))
      decisions.append(Decision(id = dec_node.id, name = dec_node.name,
                                support=sup_neg, value = -1,
                                type = dec_node.type, container=dec_node.container,
                                cost = dec_node.base_cost))
    decisions.sort(key=lambda x:x.support, reverse=True)
    sorted_decs = []
    aux = set()
    for dec in decisions:
      if dec.id not in aux:
        sorted_decs.append(dec)
        aux.add(dec.id)
    assert len(sorted_decs) == len(self.model.bases), "Mismatch after sorting support"
    return sorted_decs

  def generate(self, presets = None):
    population = list()
    while len(population) < self.settings.k2:
      point = Point(self.model.generate())
      if not point in population:
        for preset in presets:
          point.decisions[preset.id] = preset.value
        population.append(point)
    return population

  @staticmethod
  def objective_stats(generations):
    stats = []
    obj_len = len(generations[0][0].objectives)
    for i in range(obj_len):
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
      self.model.eval(self.model.get_tree().root)
      point.objectives = self.model.get_tree().evaluate(model, point)
      point.objectives.append(sum(decision.cost for decision in decisions if decision.value > 0))
      point._nodes = [node.clone() for node in model.get_tree().nodes.values()]
      point.objectives = [0 if one is None else one for one in point.objectives]
    return point.objectives

  def prune(self, support):
    gens = []
    for i in range(len(support)):
      decisions = support[:i]
      population = self.generate(decisions)
      for point in population:
        self.evaluate(point, decisions)
      gens.append(population)
    obj_stats = self.objective_stats(gens)
    return obj_stats, gens

  def report(self, stats, sub_folder):
    #headers = [obj.__name__.split("_")[-1] for obj in self.de.settings.obj_funcs]
    headers = ["root cost", "root benefit", "softgoals", "decisions cost"]
    med_spread_plot(stats, headers, fig_name="img/"+sub_folder+"/"+self.model.get_tree().name+".png")

  def to_csv(self, stats, fname):
    directory = fname.rsplit("/", 1)[0]
    mkdir(directory)
    last_gen = sorted(stats.generations[-1], key=lambda x:x.objectives[1]-x.objectives[0], reverse=True)
    self.plot_objectives(last_gen, directory)
    ids = self.model.get_tree().nodes.keys()
    names = [self.model.get_tree().nodes[key].name for key in ids] + ["?cost", "?benefit", "?softgoals"]
    table = [names]
    max_cost, max_benefit = -1, -1
    for point in last_gen:
      row = [point.get_nodes()[key].value for key in ids] + point.objectives
      max_cost = max(point.objectives[0], max_cost)
      max_benefit = max(point.objectives[1], max_benefit)
      table.append(row)
    with open(fname, "wb") as file_obj:
      writer = csv.writer(file_obj)
      writer.writerows(table)

  def plot_objectives(self, points, directory):
    directory = directory.replace("csv/", "img/")
    objectives = []
    for point in points:
      dec_lens = sum([1 if dec == 1 else 0 for dec in point.decisions.values()])
      obj = [dec_lens]
      for o in point.objectives[:2]:
        obj.append(o)
      objectives.append(obj)
    zipped = zip(*objectives)
    x = zipped[0]
    costs = zipped[1]
    benefits = zipped[2]
    tree_name = self.model.get_tree().name
    mkdir(directory)
    point_plot(x, {"cost":costs}, ['ro'], "%s/%s_costs.png"%(directory, tree_name))
    point_plot(x, {"benefit":benefits}, ['bx'], "%s/%s_benefits.png"%(directory, tree_name))
    point_plot_3d(x, costs, benefits, 'r', 'x', "%s/%s_3d.png"%(directory, tree_name),
                  "Number of Decisions", "Costs", "Benefits")

  def visualize(self, decisions):
    tracks = []
    for i in range(len(decisions)):
      pos_decs, neg_decs = [], []
      for j in range(len(decisions)):
        if j < i:
          pos_decs.append(Decision(id = decisions[j].id, value = decisions[j].value, cost = decisions[j].cost))
          neg_decs.append(Decision(id = decisions[j].id, value = decisions[j].value, cost = decisions[j].cost))
        elif j == i:
          pos_decs.append(Decision(id = decisions[j].id, value = +1, cost = decisions[j].cost))
          neg_decs.append(Decision(id = decisions[j].id, value = -1, cost = decisions[j].cost))
        # else:
        #   pos_decs.append(Decision(id = decisions[j].id, value = -1 * decisions[j].value))
        #   neg_decs.append(Decision(id = decisions[j].id, value = -1 * decisions[j].value))
      pos_pop = self.generate(pos_decs)
      neg_pop = self.generate(neg_decs)
      for pos, neg in zip(pos_pop, neg_pop):
        self.evaluate(pos, pos_decs)
        self.evaluate(neg, neg_decs)
      p_meds, p_iqrs = [], []
      n_meds, n_iqrs = [], []
      for o_i in range(len(pos_pop[0].objectives)):
        p_objs = [pt.objectives[o_i] for pt in pos_pop]
        n_objs = [pt.objectives[o_i] for pt in neg_pop]
        med, iqr = median_iqr(p_objs)
        p_meds.append(med)
        p_iqrs.append(iqr)
        med, iqr = median_iqr(n_objs)
        n_meds.append(med)
        n_iqrs.append(iqr)
      tracks.append(O(id = decisions[i].id, name = decisions[i].name,
                      pos_meds = p_meds, pos_iqrs = p_iqrs,
                      neg_meds = n_meds, neg_iqrs = n_iqrs,
                      prefered_value = decisions[i].value))
    return tracks




  @staticmethod
  def get_elbow(gens, index, obj_index=None):
    pop = gens[index]
    pop = sorted(pop, key=lambda x: x.objectives[obj_index])
    point = pop[len(pop)//2]
    return point

def print_decisions(decisions):
  columns = ["rank", "name", "type", "value", "cost", "support"]
  table = PrettyTable(columns)
  for i, decision in enumerate(decisions):
    row = [i+1, decision.name, decision.type, decision.value, decision.cost, round(decision.support, 5)]
    table.add_row(row)
  print("\n### Decisions Ranked")
  print("```")
  print(table)
  print("```")

def plot_support(decisions, fig_name):
  support = [d.support for d in decisions]
  x = range(1, len(decisions)+1)
  y = {"support": support}
  line_plot(x, y, fig_name=fig_name)
  print("\n### Support Chart")
  print("![1](../../../src/%s)"%fig_name)

def run(graph, subfolder, optimal_index = None):
  #graph = DelayModeratedBulletinBoard()
  #model = Model(cs_agent_sr_graph)
  start = time.time()
  model = Model(graph)
  print("## %s"%graph.name)
  print("```")
  star = Star1(model)
  best, rest = star.sample(subfolder)
  decisions = star.rank(best, rest)
  obj_stats, gens = star.prune(decisions)
  delta = time.time() - start
  star.report(obj_stats, subfolder)
  print("```")
  print("\n### Time Taken : %s"%delta)
  print("![1](../../../src/img/%s/%s.png)"%(subfolder,graph.name))
  print_decisions(decisions)
  plot_support(decisions, "img/%s/%s_support.png"%(subfolder,graph.name))
  tree_name = Grapher(graph, decisions, subfolder).draw_tree()
  print("![1](../../../src/img/%s/%s.png)"%(subfolder,tree_name))
  tracks = star.visualize(decisions)
  reco_tree_name = Recommender(graph, decisions, tracks, subfolder).draw_tree()
  print("###[Recommendation](../../../src/img/%s/%s.png)"%(subfolder,reco_tree_name))
  # if optimal_index is not None:
  #   print("\n### Top %d Decisions from above table."%optimal_index)
  #   print("```")
  #   point = star.get_elbow(gens, optimal_index, obj_index = 0)
  #   columns = ["name", "type", "value"]
  #   table = PrettyTable(columns)
  #   for node in point.get_nodes():
  #     if node.value:
  #       row = [node.name, node.type, node.value]
  #       table.add_row(row)
  #   print(table)
  #   print("```")


if __name__ == "__main__":
  from pyAHP.models.sample import tree
  #tree.name = "sample"
  run(tree, "visualize")