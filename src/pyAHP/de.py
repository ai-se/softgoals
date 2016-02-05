from __future__ import print_function, division
import sys, os
__author__ = 'panzer'
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath("."))
from utilities.lib import *
import time
from math import exp
from pyAHP.model import Model, Point

MIN_FRONTIER_SIZE=10

def default():
  return O(
    gens = 20,
    candidates = 50,
    f = 0.75,
    cr = 0.3,
    seed = 1,
    better = [lt, gt],
    obj_funcs = [Point.evaluate_cost, Point.evaluate_benefit],
    evaluation = Point.evaluate,
    is_percent = True,
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
    """
    Set Limit for each objectives
    :return:
    """
    size = len(self.model.get_tree().nodes.keys())
    mins = [1*size, 1*size]
    maxs = [1000*size, 1000*size]
    wts  = [-1, 1]
    return O(mins=mins, maxs=maxs, weights=wts)

  def assign_frontier_size(self):
    """
    Decide number of points for frontier
    :return:
    """
    num_decs = len(self.model.generate().keys())
    return min(int(2**num_decs), default().candidates)

  def generate(self, size):
    population = set()
    while len(population) < size:
      point = Point(self.model.generate())
      if (not point in population) and self.model.evaluate_constraints(point.decisions)[0]:
        population.add(point)
    return list(population)

  def run(self):
    """
    DE runner
    :return:
    """
    settings = self.settings
    stat = Statistics()
    start = time.time()
    if settings.candidates < MIN_FRONTIER_SIZE:
      print("```")
      print("### Possible candidates = %s lesser than minimum frontier size = %s"%(settings.candidates, MIN_FRONTIER_SIZE))
      exit()
    population = self.generate(settings.candidates)
    stat.insert(population)
    for _ in range(self.settings.gens):
      say(".")
      clones = population[:]
      for point in population:
        original_obj = settings.evaluation(point, self.model, settings.obj_funcs)
        mutant = self.mutate(point, population)
        mutated_obj = settings.evaluation(mutant, self.model, settings.obj_funcs)
        if None in mutated_obj: continue
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

def _main():
  from pyAHP.models.sample import tree
  model = Model(tree)
  de = DE(model)
  stat = de.run()
  stat.settings.gen_step = 4
  stat.tiles()

if __name__ == "__main__":
  _main()