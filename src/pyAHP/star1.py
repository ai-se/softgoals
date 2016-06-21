from __future__ import print_function, division
import sys, os, time
sys.path.append(os.path.abspath("."))
__author__ = 'panzer'
from utilities.lib import *
from de import DE, Mutator
from pyAHP.model import Model, Point
from utilities.nsga2 import select as sel_nsga2
from utilities.plotter import med_spread_plot, line_plot, point_plot, point_plot_3d
from prettytable import PrettyTable
import csv, numpy as np
from collections import OrderedDict
from pyAHP.dotter import Grapher, Recommender
from utilities.sk import rdivDemo

def default():
  return O(
    k1 = 100,
    k2 = 100,
    best_percent = 33,
    gen_step = 20
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
    self.mutator = Mutator(model.get_tree())

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
                                cost = dec_node.base_cost, benefit = dec_node.base_benefit))
      decisions.append(Decision(id = dec_node.id, name = dec_node.name,
                                support=sup_neg, value = -1,
                                type = dec_node.type, container=dec_node.container,
                                cost = dec_node.base_cost, benefit = dec_node.base_benefit))
    decisions.sort(key=lambda x:x.support, reverse=True)
    sorted_decs = []
    aux = set()
    for dec in decisions:
      if dec.id not in aux:
        sorted_decs.append(dec)
        aux.add(dec.id)
    assert len(sorted_decs) == len(self.model.bases), "Mismatch after sorting support"
    return sorted_decs

  def generate(self, presets = None, check_validity = False):
    population = list()
    while len(population) < self.settings.k2:
      point = Point(self.mutator.generate())
      if not point in population:
        for preset in presets:
          point.decisions[preset.id] = preset.value
        if check_validity:
          self.model.reset_nodes(point.decisions)
          self.model.eval(self.model.get_tree().root)
          if self.model.get_tree().root.value != 1:
            continue
        population.append(point)
    return population

  @staticmethod
  def objective_stats(generations):
    stats = []
    obj_len = len(generations[0][0].objectives)
    objective_map = {}
    for i in range(obj_len):
      objectives = []
      data_map = {}
      meds = []
      iqrs = []
      for gen, pop in enumerate(generations):
        objs = [pt.objectives[i] for pt in pop]
        objectives.append(objs)
        med, iqr = median_iqr(objs)
        meds.append(med)
        iqrs.append(iqr)
      objective_map[i] = objectives
      data_map["meds"] = meds
      data_map["iqrs"] = iqrs
      stats.append(data_map)
    return stats, objective_map

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

  def prune(self, support, check_validity):
    gens = []
    for i in range(len(support)):
      decisions = support[:i]
      population = self.generate(decisions, check_validity=check_validity)
      for point in population:
        self.evaluate(point, decisions)
      gens.append(population)
    obj_stats, objective_map = self.objective_stats(gens)
    return obj_stats, gens, objective_map

  def report(self, stats, sub_folder, fig_name):
    #headers = [obj.__name__.split("_")[-1] for obj in self.de.settings.obj_funcs]
    headers = ["root cost", "root benefit", "softgoals", "preset decisions cost"]
    med_spread_plot(stats, headers, fig_name="img/"+sub_folder+"/"+fig_name+".png")
    return "img/"+sub_folder+"/"+fig_name+".png"

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
          pos_decs.append(Decision(id = decisions[j].id, value = decisions[j].value,
                                   cost = decisions[j].cost, benefit = decisions[j].benefit))
          neg_decs.append(Decision(id = decisions[j].id, value = decisions[j].value,
                                   cost = decisions[j].cost, benefit = decisions[j].benefit))
        elif j == i:
          pos_decs.append(Decision(id = decisions[j].id, value = +1,
                                   cost = decisions[j].cost, benefit = decisions[j].benefit))
          neg_decs.append(Decision(id = decisions[j].id, value = -1,
                                   cost = decisions[j].cost, benefit = decisions[j].benefit))
        # else:
        #   pos_decs.append(Decision(id = decisions[j].id, value = -1 * decisions[j].value))
        #   neg_decs.append(Decision(id = decisions[j].id, value = -1 * decisions[j].value))
      if decisions[i].value == 1:
        pos_pop = self.generate(pos_decs, check_validity=True)
        neg_pop = self.generate(neg_decs, check_validity=False)
      else:
        pos_pop = self.generate(pos_decs, check_validity=False)
        neg_pop = self.generate(neg_decs, check_validity=True)
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
                      prefered_value = decisions[i].value,
                      cost = decisions[i].cost, benefit = decisions[i].benefit))
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

def linear_seq_clusterer(stats, decisions, key="iqrs", delta=0.25):
  point_to_cluster = OrderedDict()
  for stat in stats:
    vals = stat[key]
    clusters = []
    cluster_prev = [vals[0]]
    clusters.append(cluster_prev)
    current_cluster = point_to_cluster.get(0, set())
    current_cluster.add(len(clusters))
    point_to_cluster[0] = current_cluster
    for index, val in enumerate(vals[1:]):
      prev_mean = np.mean(cluster_prev)
      if abs(prev_mean - val) > delta * prev_mean:
        cluster_prev = [val]
        clusters.append(cluster_prev)
      else:
        cluster_prev.append(val)
      current_cluster = point_to_cluster.get(index+1, set())
      current_cluster.add(len(clusters))
      point_to_cluster[index+1] = current_cluster
  columns = ["Cluster ID", "Decision Name"]
  table = PrettyTable(columns)
  prev_val = None
  for key, val in point_to_cluster.items():
    current_val = ",".join(map(str, list(val)))
    if current_val == prev_val:
      row = ["\"", decisions[key].name]
    else:
      row = [current_val, decisions[key].name]
      prev_val = current_val
    table.add_row(row)
  print("\n### Decisions Clustered")
  print("```")
  print(table)
  print("```")

def smoothen(objective_map, decisions, keys=[0, 1, 2]):
  smoothened = []
  for key in keys:
    objectives = objective_map[key]
    sk_data = []
    for index, (decision, dec_objectives) in enumerate(zip(decisions, objectives)):
      sk_data.append([str(index)]+dec_objectives)
    ranks = rdivDemo(sk_data, do_print=False)
    rank_map = {}
    for rank, _, x in ranks:
      meds_iqrs = rank_map.get(rank, [[], []])
      med, iqr = median_iqr(x.all)
      meds_iqrs[0].append(med)
      meds_iqrs[1].append(iqr)
      rank_map[rank] = meds_iqrs
    smooth_objs = {}
    meds, iqrs = [], []
    for rank, _, x in ranks:
      meds_iqrs = rank_map[rank]
      med, iqr = round(float(np.mean(meds_iqrs[0])), 2), round(float(np.mean(meds_iqrs[1])), 2)
      meds.append(med)
      iqrs.append(iqr)
      smooth_objs["meds"] = meds
      smooth_objs["iqrs"] = iqrs
    smoothened.append(smooth_objs)
  return smoothened


VALID_ONLY = True
def run(graph, subfolder, optimal_index = None):
  #graph = DelayModeratedBulletinBoard()
  #model = Model(cs_agent_sr_graph)
  start = time.time()
  model = Model(graph, generation_mode="triangular")
  print("## [Model](https://github.com/ai-se/softgoals/blob/master/pdf/AOWS.pdf)")
  print("## %s"%graph.name)
  star = Star1(model)
  if star.de.termination is not None:
    print("### Early Termination Cost = %d"%star.de.termination)
  print("```")
  best, rest = star.sample(subfolder)
  decisions = star.rank(best, rest)
  obj_stats, gens, objective_map = star.prune(decisions, check_validity=VALID_ONLY)
  smoothened = smoothen(objective_map, decisions)
  smoothened.append(obj_stats[3])
  med_iqr_plot = star.report(obj_stats, subfolder, model.get_tree().name)
  smoothened_plot = star.report(smoothened, subfolder, model.get_tree().name+"_smooth")
  print("```")
  print("![1](../../../src/%s)"%med_iqr_plot)
  print("### Smoothened Plot")
  print("![1](../../../src/%s)"%smoothened_plot)
  print_decisions(decisions)
  plot_support(decisions, "img/%s/%s_support.png"%(subfolder,graph.name))

  # tree_name = Grapher(graph, decisions, subfolder).draw_tree()
  # print("![1](../../../src/img/%s/%s.png)"%(subfolder,tree_name))
  # tracks = star.visualize(decisions)
  # reco_tree_name = Recommender(graph, decisions, tracks, subfolder).draw_tree()
  # print("##[Recommendation](../../../src/img/%s/%s.png)"%(subfolder,reco_tree_name))
  linear_seq_clusterer(obj_stats[:2], decisions, key="meds")
  delta = time.time() - start
  print("\n### Time Taken : %s"%delta)
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
  run(tree, "junk")