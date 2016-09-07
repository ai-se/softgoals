from __future__ import print_function, division
import sys, os
__author__ = 'george'
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath("."))
from lib import *
import time
from math import exp
from pystar.model import Model, Point
from utilities.de import Generator

def default():
  return O(
    gens = 10,
    candidates = 20,
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


def get_time():
  """
  Get Current Wall clock time in milliseconds
  :return:
  """
  return time.clock()


class NSGA2(O):
  def __init__(self, model, **settings):
    O.__init__(self)
    self.model = model
    self.settings = default().update(candidates=self.assign_frontier_size())
    seed(self.settings.seed)
    self.dominates = self.bdom
    self.model.settings.obj_funcs = self.settings.obj_funcs
    self.model.settings.better = self.settings.better
    self.model.settings.is_percent = self.settings.is_percent
    self.population = None
    self.gen, self.runtime = 0, 0

  def assign_frontier_size(self):
    num_decs = len(self.model.generate().keys())
    return min(int(2 ** num_decs), default().candidates)

  def generate(self, size):
    population = list()
    generator = Generator(self.model)
    while len(population) < size:
      # point = Point(self.model.generate())
      point = Point(generator.generate())
      if not point in population:
        population.append(point)
    return population

  def bdom(self, obj1, obj2):
    """
    Binary Domination
    :param obj1: Objective 1
    :param obj2: Objective 2
    :return: Check objective 1 dominates objective 2
    """
    at_least = False
    for i, (a, b) in enumerate(zip(obj1, obj2)):
      if self.settings.better[i](a, b):
        at_least = True
      elif a == b:
        continue
      else:
        return False
    return at_least

  def run(self):
    """
    Runner function that runs the NSGA2 optimization algorithm
    """
    start = get_time()
    self.population = self.generate(self.settings.pop_size)
    pop_size = len(self.population)
    self.gen = 0
    while self.gen < self.settings.gens:
      say(".")
      self.gen += 1
      population = self.select(population)
      population = self.evolve(population, pop_size)
    self.runtime = get_time() - start
    return population

  def select(self, population):
    kids = [one.clone() for one in population]
    pass


  def binary_tournament_selection(self, population, size):
    """
    Select individual from the population of size
    tourn_size based on tournament evaluation
    :param problem: Problem used for evaluation
    :param population: Population to sample from
    :param size: Size of tournament
    :return: Most dominant individual from the tournament
    """
    tourn = shuffle(random.sample(population, size))
    best = tourn[0]
    best_obj = self.settings.evaluation(best, self.model, self.settings.obj_funcs)
    for i in range(1, len(tourn)):
      this_obj = self.settings.evaluation(tourn[i], self.model, self.settings.obj_funcs)
      if self.bdom(this_obj, best_obj):
        best = tourn[i]
    return best