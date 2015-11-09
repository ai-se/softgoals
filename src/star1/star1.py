from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
__author__ = 'george'
sys.dont_write_bytecode = True
from utilities.lib import *
from pystar.models.CSServices import graph as cs_agent_sr_graph
from pystar.model import Model
from utilities.de import DE, Point
from utilities.plotter import med_spread_plot

def default():
  return O(
    k1 = 100,
    k2 = 100
  )

class Star1(O):
  def __init__(self, model, **settings):
    O.__init__(self)
    self.model = model
    self.model.bases.extend(self.get_conflicts())
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
            temp_toggle = sign(edge.get_contribution_weight(edge.value))
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
    best_size = len(best)
    rest_size = len(rest)
    p_best = best_size / (best_size + rest_size)
    p_rest = rest_size / (best_size + rest_size)
    sup_map = {}
    for dec_node in self.model.bases:
      f_best = 0
      for point in best:
        if point.decisions[dec_node.id] > 0:
          f_best += 1
      f_best /= best_size
      l_best = f_best * p_best
      f_rest = 0
      for point in rest:
        if point.decisions[dec_node.id] > 0:
          f_rest += 1
      f_rest /= best_size
      l_rest = f_rest * p_rest
      sup_best = l_best**2 / (l_best + l_rest)
      sup_map[dec_node.id] = sup_best
    return sup_map

  def generate(self, presets = None):
    population = list()
    while len(population) < self.de.settings.candidates:
      point = Point(self.model.generate())
      if not point in population:
        population.append(point)
    for point in population:
      for preset in presets:
        point.decisions[preset] = 1
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

  def prune(self, support):
    gens = []
    for i in range(len(support)):
      sup_keys = support[:i]
      population = self.generate(sup_keys)
      for point in population:
        self.de.settings.evaluation(point, self.model, self.de.settings.obj_funcs)
      gens.append(population)
    obj_stats = self.objective_stats(gens)
    return obj_stats

  def report(self, stats):
    headers = [obj.__name__.split("_")[-1] for obj in self.de.settings.obj_funcs]
    med_spread_plot(stats, headers, fig_name="img/"+self.model.get_tree().name+".png")


def run():
  model = Model(cs_agent_sr_graph)
  star = Star1(model)
  best, rest = star.sample()
  sup_map = star.rank(best, rest)
  sup_keys = sorted(sup_map, key=lambda k: sup_map[k], reverse=True)
  obj_stats = star.prune(sup_keys)
  star.report(obj_stats)



