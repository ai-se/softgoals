from __future__ import print_function, division
import sys, os, time
sys.path.append(os.path.abspath("."))
__author__ = 'panzer'
from utilities.lib import *
from de import DE
from pyAHP.model import Model, Point
from utilities.nsga2 import select as sel_nsga2
from utilities.plotter import med_spread_plot
from prettytable import PrettyTable
import csv

def default():
  return O(
    k1 = 10,
    k2 = 100,
    best_percent = 20,
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

  # def sample(self):
  #   stat = self.de.run()
  #   stat.settings.gen_step = self.settings.gen_step
  #   stat.tiles()
  #   population = set()
  #   # for gen in stat.generations:
  #   #   for point in gen:
  #   #     population.add(point)
  #   for point in stat.generations[0]:
  #     population.add(point)
  #   for point in stat.generations[-1]:
  #     population.add(point)
  #   print(len(population))
  #   best_size = int(len(population) * self.settings.best_percent/100)
  #   best = sel_nsga2(self.model, list(population), best_size)
  #   print(len(best))
  #   rest = population - set(best)
  #   return list(best), list(rest)

  def sample(self, subfolder):
    stat = self.de.run()
    self.to_csv(stat, "csv/"+subfolder+"/"+self.model.get_tree().name+".csv")
    stat.settings.gen_step = self.settings.gen_step
    stat.tiles()
    best = set()
    population = set()
    for point in stat.generations[0]:
      population.add(point)
    for point in stat.generations[-1]:
      population.add(point)
    for obj_index in range(len(self.de.settings.obj_funcs)):
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
      funcs = [Point.evaluate_cost, Point.evaluate_benefit, Point.evaluate_softgoals]
      point.objectives = [func(model) for func in funcs]
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
    last_gen = stats.generations[-1]
    ids = self.model.get_tree().nodes.keys()
    names = [self.model.get_tree().nodes[key].name for key in ids] + ["?cost", "?benefit", "?softgoals"]
    table = [names]
    max_cost, max_benefit = -1, -1
    for point in last_gen:
      row = [point.get_nodes()[key].value for key in ids] + point.objectives
      max_cost = max(point.objectives[0], max_cost)
      max_benefit = max(point.objectives[1], max_benefit)
      table.append(row)
    print(max_cost, max_benefit)
    with open(fname, "wb") as file_obj:
      writer = csv.writer(file_obj)
      writer.writerows(table)



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
  run(tree, "log_ahp")