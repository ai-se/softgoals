from __future__ import print_function, division
import sys
__author__ = 'george'
sys.dont_write_bytecode = True
from lib import *
import sk

def default():
  return O(
    gens = 100,
    candidates = 50,
    f = 0.75,
    cr = 0.3,
    seed = 1,
    better = gt,
    obj_funcs = [eval_softgoals, eval_goals]
  )

def eval_roots(model, decision_map):
  return model.evaluate_score(decision_map)

def eval_goals(model, decision_map):
  return model.evaluate_type(decision_map, node_type="goal")

def eval_softgoals(model, decision_map):
  return model.evaluate_type(decision_map, node_type="softgoal")


class Statistics(O):
  @staticmethod
  def default_settings():
    return O(
      gen_step = 20
    )
  def __init__(self, settings=None):
    O.__init__(self)
    self.generations = []
    if not settings:
      settings = Statistics.default_settings()
    self.settings = settings

  def insert(self, pop):
    self.generations.append(pop)
    return self

  def tiles(self):
    num_obs = len(self.generations[0][0].objectives)
    for i in range(num_obs):
      obj_gens=[]
      for gen, pop in enumerate(self.generations):
        if gen % self.settings.gen_step != 0:
          continue
        objs = ["gen"+str(gen)+"_f"+str(i+1)]
        for point in pop:
          objs.append(point.objectives[i])
        obj_gens.append(objs)
      sk.rdivDemo(obj_gens)


def dominates(obj1, obj2, better=lt):
  at_least = False
  for a, b in zip(obj1, obj2):
    if better(a,b):
      at_least = True
    elif a == b:
      continue
    else:
      return False
  return at_least


class Point(O):
  id = 0
  def __init__(self, decisions, objectives=None):
    O.__init__(self)
    Point.id += 1
    self.id = Point.id
    self.decisions = decisions
    self.objectives = objectives

  def __hash__(self):
    return hash(self.decisions)

  def __eq__(self, other):
    return cmp(self.decisions, other.decisions) == 0

  def evaluate(self, model, obj_funcs):
    if not self.objectives:
      self.objectives = [func(model, self.decisions) for func in obj_funcs]
      #self.objectives = [model.evaluate(self.decisions)]
    return self.objectives

  @staticmethod
  def trim(val):
    if val > 0:
      return t
    else:
      return f


class DE(O):
  def __init__(self, model, settings=None):
    O.__init__(self)
    self.model = model
    if not settings:
      settings = default()
    self.settings = settings
    seed(self.settings.seed)

  def generate(self, size):
    population = list()
    while len(population) < size:
      point = Point(self.model.generate())
      if not point in population:
        population.append(point)
    return population

  def run(self):
    """
    Runner function to run differential evolution
    :return: Optimal population
    """
    print(self.settings)
    stat = Statistics()
    population = self.generate(self.settings.candidates)
    stat.insert(population)
    for _ in range(self.settings.gens):
      clones = population[:]
      for point in population:
        original_obj = point.evaluate(self.model, self.settings.obj_funcs)
        mutant = self.mutate(point, population)
        mutated_obj = mutant.evaluate(self.model, self.settings.obj_funcs)
        if dominates(mutated_obj, original_obj, better=self.settings.better) and (not mutant in clones):
          clones.remove(point)
          clones.append(mutant)
      population = clones
      stat.insert(population)
    return stat


  def mutate(self, one, pop):
    """
    Function to mutate point using
    DE mutation strategy and return it
    :param one: Point to be mutated
    :param pop: Population to mutate from
    :return: Mutated point
    """
    two, three, four = DE.three_others(one, pop)
    random_key = choice(one.decisions.keys())
    mutated_decs = one.decisions.copy()
    for key in one.decisions.keys():
      if (rand() < self.settings.cr) or (key == random_key):
        mutated_decs[key] = Point.trim(two.decisions[key] + self.settings.f * (three.decisions[key] - four.decisions[key]))
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
