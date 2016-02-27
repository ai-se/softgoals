from __future__ import print_function, division
import sys, os
__author__ = 'george'
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath("."))
from lib import *
import time
from math import exp
from pystar.model import Model, Point

MIN_FRONTIER_SIZE=1

def default():
  return O(
    gens = 10,
    candidates = 6,
    f = 0.75,
    cr = 0.3,
    seed = 1,
    better = [gt, gt],
    obj_funcs = [Point.eval_softgoals, Point.eval_goals],
    evaluation = Point.evaluate,
    is_percent = False,
    binary = True,
    dominates = "bdom",
    cdom_delta = 0.01
  )

class DE(O):
  def __init__(self, model, **settings):
    O.__init__(self)
    self.model = model
    self.settings = default().update(candidates=self.assign_frontier_size()).update(**settings)
    seed(self.settings.seed)
    if self.settings.dominates == "bdom":
      self.dominates = self.bdom
    else:
      self.dominates = self.cdom
      self.limits = self.set_limits()
    self.model.settings.obj_funcs = self.settings.obj_funcs
    self.model.settings.better = self.settings.better
    self.model.settings.is_percent = self.settings.is_percent

  def set_limits(self):
    mins = []
    maxs = []
    weights = []
    model = self.model
    for comp, func in zip(self.settings.better, self.settings.obj_funcs):
      weights.append(-1 if comp==lt else 1)
      if func == Point.eval_all_goals:
        mins.append(0)
        if self.settings.is_percent: maxs.append(100)
        else:
          maxs.append(len(model.get_tree().get_nodes(node_type=["softgoal", "goal"])))
      elif func == Point.eval_softgoals:
        mins.append(0)
        if self.settings.is_percent: maxs.append(100)
        else:
          maxs.append(len(model.get_tree().get_nodes(node_type=["softgoal"])))
      elif func == Point.eval_goals:
        mins.append(0)
        if self.settings.is_percent: maxs.append(100)
        else:
          maxs.append(len(model.get_tree().get_nodes(node_type=["goal"])))
      elif func == Point.eval_coverage:
        mins.append(0)
        if self.settings.is_percent: maxs.append(100)
        else:
          maxs.append(len(model.get_tree().get_nodes()))
      elif func == Point.eval_costs:
        mins.append(0)
        maxs.append(sum(model.cost_map.values()))
      elif func == Point.eval_paths:
        mins.append(0)
        maxs.append(sum(model.cost_map.values())*len(model.get_tree().get_nodes()))
    return O(mins=mins, maxs=maxs, weights=weights)

  def assign_frontier_size(self):
    num_decs = len(self.model.generate().keys())
    return min(int(2**num_decs), default().candidates)

  def generate(self, size):
    population = list()
    generator = Generator(self.model)
    while len(population) < size:
      #point = Point(self.model.generate())
      point = Point(generator.generate())
      if not point in population:
        population.append(point)
    return population

  def run(self):
    """
    Runner function to run differential evolution
    :return: Optimal population
    """
    settings = self.settings
    #print(settings)
    stat = Statistics()
    start = time.time()
    if settings.candidates < MIN_FRONTIER_SIZE:
      print("```")
      print("### Possible candidates = %s lesser than minimum frontier size = %s"%(settings.candidates, MIN_FRONTIER_SIZE))
      exit()
      # raise RuntimeError(500, "Cannot generate %s candidates with %s leaves"
      #           %(settings.candidates, len(self.model.bases)))
    population = self.generate(settings.candidates)
    stat.insert(population)
    for _ in range(self.settings.gens):
      clones = population[:]
      for point in population:
        original_obj = settings.evaluation(point, self.model, settings.obj_funcs)
        mutant = self.mutate(point, population)
        mutated_obj = settings.evaluation(mutant, self.model, settings.obj_funcs)
        if self.dominates(mutated_obj, original_obj) and (not mutant in clones):
          clones.remove(point)
          clones.append(mutant)
      population = clones
      stat.insert(population)
    stat.runtime = time.time() - start
    return stat

  def bdom(self, obj1, obj2):
    """
    Binary Domination
    :param obj1: Objective 1
    :param obj2: Objective 2
    :return: Check objective 1 dominates objective 2
    """
    at_least = False
    for i,(a, b) in enumerate(zip(obj1, obj2)):
      if self.settings.better[i](a,b):
        at_least = True
      elif a == b:
        continue
      else:
        return False
    return at_least

  def cdom(self, obj1, obj2):
    """
    Continuous Domination
    :param obj1: Objective 1
    :param obj2: Objective 2
    :return: Check if objective 1 dominates objective 2 based on exponential loss.
    """
    def norm(val, least, most):
      least = min(least, val)
      most = max(most, val)
      return (val - least) / (most - least + 0.0001)
    def exp_loss(x_i, y_i, w_i, n):
      return -1*exp(w_i*(x_i-y_i)/n)
    def loss(x, y):
      x_norm = [norm(v,lo,hi) for v,lo,hi in zip(x, self.limits.mins, self.limits.maxs)]
      y_norm = [norm(v,lo,hi) for v,lo,hi in zip(y, self.limits.mins, self.limits.maxs)]
      n = len(x)
      losses = [exp_loss(x_i, y_i, w_i, n) for x_i, y_i, w_i in zip(x_norm, y_norm, self.limits.weights)]
      return sum(losses)/n
    l1 = loss(obj1, obj2)
    l2 = loss(obj2, obj1)
    return abs(l1 - l2) > self.settings.cdom_delta and l1 < l2



  def mutate(self, one, pop):
    """
    Function to mutate point using
    DE mutation strategy and return it
    :param one: Point to be mutated
    :param pop: Population to mutate from
    :return: Mutated point
    """
    if self.settings.binary:
      return self.mutate_binary(one, pop)
    else:
      return self.mutate_real(one, pop)

  def mutate_real(self, one, pop):
    """
    Function to perform real mutation to
    compute real values
    :param one: Point to be mutated
    :param pop: Population to selected from
    :return: mutant
    """
    two, three, four = DE.three_others(one, pop)
    random_key = choice(one.decisions.keys())
    mutated_decs = one.decisions.copy()
    for key in one.decisions.keys():
      if (rand() < self.settings.cr) or (key == random_key):
        mutated_decs[key] = Point.trim(two.decisions[key] + self.settings.f * (three.decisions[key] - four.decisions[key]))
    return Point(mutated_decs)

  def mutate_binary(self, one, pop):
    two, three, four = DE.three_others(one, pop)
    random_key = choice(one.decisions.keys())
    mutated_decs = one.decisions.copy()
    crossover_vector = [t if rand() < self.settings.f else f for _ in mutated_decs]
    for i, key in enumerate(one.decisions.keys()):
      if (rand() < self.settings.cr) or (key == random_key):
        mutated_decs[key] = OR(two.decisions[key], AND(crossover_vector[i], XOR(three.decisions[key], four.decisions[key])))
    return Point(mutated_decs)


  @staticmethod
  def three_others(one, pop):
    """
    Return three other points from population
    :param one: Point not to consider
    :param pop: Population to look in
    :return: two, three, four
    """
    def one_other():
      while True:
        x = choice(pop)
        if not x.id in seen:
          seen.append(x.id)
          return x
    seen = [one.id]
    two = one_other()
    three = one_other()
    four = one_other()
    return two, three, four

def XOR(a, b):
  if (a==t and b==f) or (a==f and b==t):
    return t
  return f

def OR(a, b):
  if a==t or b==t:
    return t
  return f

def AND(a, b):
  if a==t and b==t:
    return t
  return f


class Generator(O):
  """
  Generator to generate a valid solution
  via propagation.
  """
  def __init__(self, model):
    O.__init__(self)
    self.model = model

  def generate(self):
    node_dict, decisions = {}, {}
    self.model.clear_nodes()
    nodes = self.model.get_tree().get_nodes(node_type=["softgoal", "goal"])
    for node in nodes:
      value = t if node.type == "goal" else t/2
      node_dict = Generator.update_dict(node_dict, self.propagate(node, value))
    for base in self.model.bases:
      decisions[base.id] = node_dict.get(base.id, choice([t,f]))
    return decisions

  @staticmethod
  def update_dict(target, source):
    for key in source.keys():
      if key not in target:
        target[key] = source[key]
    return target

  def propagate(self, node, value):
    if node.value is not None:
      return {node.id : value}
    node.value = value
    deps, rest= self.model.dep_and_rest(node.from_edges)
    if not deps and not rest:
      value = 1 if value > 0 else -1
      node.value = value
      return {node.id : value}
    decisions = {}
    if deps:
      dep_nodes = shuffle([self.model.get_tree().get_node(dep.source) for dep in deps])
      if value == t:
        for dep_node in dep_nodes:
          decisions = Generator.update_dict(decisions, self.propagate(dep_node, t))
      else:
        decisions = Generator.update_dict(decisions, self.propagate(dep_nodes[0], f))
        for dep_node in dep_nodes[1:]:
          decisions = Generator.update_dict(decisions, self.propagate(dep_node, choice([t, f])))
    if not rest:
      return decisions

    edge_type = rest[0].type
    if edge_type == "decompositions":
      kids = shuffle([self.model.get_tree().get_node(edge.source) for edge in rest])
      if rest[0].value == "and" and value == t:
        for kid in kids:
          decisions = Generator.update_dict(decisions, self.propagate(kid, t))
      elif rest[0].value == "and" and value == f:
        decisions = Generator.update_dict(decisions, self.propagate(kids[0], f))
        for kid in kids[1:]:
          decisions = Generator.update_dict(decisions, self.propagate(kid, choice([t, f])))
      elif rest[0].value == "or" and value == t:
        decisions = Generator.update_dict(decisions, self.propagate(kids[0], t))
        for kid in kids[1:]:
          decisions = Generator.update_dict(decisions, self.propagate(kid, choice([t, f])))
      else:
        for kid in kids:
          decisions = Generator.update_dict(decisions, self.propagate(kid, f))
    elif edge_type == "contribution":
      for edge in shuffle(rest):
        kid = self.model.get_tree().get_node(edge.source)
        contrib = edge.value
        contrib_value = None
        if value == t:
          if contrib == "make": contrib_value = t
        elif value == t/2:
          if contrib == "make" or contrib == "help":
            contrib_value = t/2
          else:
            contrib_value = f/2
        elif value == f/2:
          if contrib == "make" or contrib == "help":
            contrib_value = f/2
          else:
            contrib_value = t/2
        else:
          if contrib == "make":
            contrib_value = f
          elif contrib == "break":
            contrib_value = t
        if contrib_value is None:
          # Conflict Arises over here due to wrong choice
          # of value for edge. Hence random assign
          contrib_value = choice([t/2, f/2])
          #raise RuntimeError("Either node value is %s or edge %s is unknown"%(kid.value, contrib))
        decisions = Generator.update_dict(decisions, self.propagate(kid, contrib_value))
    return decisions


def _main():
  from pystar.models.dot_models import CSServices
  model = Model(CSServices())
  generator = Generator(model)
  print(len(generator.generate().keys()))

if __name__ == "__main__":
  _main()