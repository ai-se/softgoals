from __future__ import print_function, division
import sys
__author__ = 'george'
from lib import *

def default():
  return O(
    gens = 100,
    candidates = 50,
    f = 0.75,
    cr = 0.3
  )

class Point(O):
  id = 0
  def __init__(self, decisions, objectives=None):
    Point.id += 1
    self.id = Point.id
    self.decisions = decisions
    self.objectives = objectives

  def __hash__(self):
    return hash(self.decisions)

  def __eq__(self, other):
    return cmp(self.decisions, other.decisions) == 0

  def evaluate(self, model):
    if not self.objectives:
      #TODO - As of now we consider the number of softgoals
      self.objectives = [model.evaluate(self.decisions)]
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
    population = self.generate(self.settings.candidates)
    for _ in range(self.settings.gens):
      clones = population[:]
      for point in population:
        original_obj = point.evaluate(self.model)
        mutant = self.mutate(point, population)
        mutated_obj = mutant.evaluate(self.model)
        if self.better(mutated_obj, original_obj) and (not point in clones):
          clones.remove(point)
          clones.append(mutant)
      population = clones
    return population


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
    mutated_decs = {}
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

  def better(self, obj1, obj2):
    if obj1[0] > obj2[0]:
      return True
    return False



