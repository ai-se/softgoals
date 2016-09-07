from __future__ import print_function, division
import sys, os
__author__ = 'george'
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath("."))
from utilities.lib import *
import time
from pystar.model import Model, Point
from utilities.de import Generator

def default():
  return O(
    gens = 250,
    candidates = 100,
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

def loo(points):
  """
  Iterator which generates a
  test case and training set
  :param points:
  :return:
  """
  for i in range(len(points)):
    one = points[i]
    rest = points[:i] + points[i+1:]
    yield one, rest

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
    return min(int((2 ** num_decs)/20), default().candidates)

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

  def nsga_domination(self, obj1, obj2):
    if self.bdom(obj1, obj2):
      return 1
    elif self.bdom(obj2, obj1):
      return 2
    else:
      return 0

  def select(self, population):
    kids = []
    clones = [one.clone() for one in population]
    for _ in range(len(clones)):
      two, three, four = NSGA2.three_others(one, clones)
      random_key = choice(one.decisions.keys())
      mutated_decs = one.decisions.copy()
      crossover_vector = [t if rand() < self.settings.f else f for _ in mutated_decs]
      for i, key in enumerate(one.decisions.keys()):
        if (rand() < self.settings.cr) or (key == random_key):
          mutated_decs[key] = OR(two.decisions[key],
                                 AND(crossover_vector[i], XOR(three.decisions[key], four.decisions[key])))
      kids.append(Point(mutated_decs))
    return clones + kids

  def evolve(self, population, size):
    """
      Mutator Function: Performs crossover and polynomial mutation
      :param population:Population that needs to be evolved
      :param size: Expected size of the result
      :return : The mutated population
      """
    fronts = self.fast_non_dom_sort(population)
    pop_next = []
    for i, front in enumerate(fronts):
      if len(pop_next) + len(fronts[i]) >= size:
        fronts[i] = self.assign_crowd_dist(front)
        pop_next += sorted(fronts[i], key=lambda x: x.crowd_dist, reverse=True)[:(size - len(pop_next))]
        break
      else:
        pop_next += fronts[i]
    return pop_next

  def fast_non_dom_sort(self, population):
    """
    Fast Non Dominated Sort
    :param - Population to sort
    :return - List of Frontiers
    """
    frontiers = []
    front1 = []
    for one in population:
      self.settings.evaluation(one, self.model, self.settings.obj_funcs)
    for one, rest in loo(population):
      for two in rest:
        domination_status = self.nsga_domination(one.objectives, two.objectives)
        if domination_status == 1:
          one.dominated.append(two)
        elif domination_status == 2:
          one.dominating += 1
      if one.dominating == 0:
        one.rank = 1
        front1.append(one)
    current_rank = 1
    frontiers.append(front1)
    while True:
      front2 = []
      for one in front1:
        for two in one.dominated:
          two.dominating -= 1
          if two.dominating == 0:
            two.rank = current_rank + 1
            front2.append(two)
      current_rank += 1
      if len(front2) == 0:
        break
      else:
        frontiers.append(front2)
        front1 = front2
    return frontiers

  def assign_crowd_dist(self, frontier):
    """
    Crowding distance between each point in
    a frontier.
    """
    l = len(frontier)
    for m in range(len(self.settings.obj_funcs)):
      frontier = sorted(frontier, key=lambda x: x.objectives[m])
      frontier[0].crowd_dist = float("inf")
      frontier[-1].crowd_dist = float("inf")
      for i in range(1, l - 1):
        frontier[i].crowd_dist += (frontier[i + 1].objectives[m] - frontier[i - 1].objectives[m])
    return frontier

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

  def run(self):
    """
    Runner function that runs the NSGA2 optimization algorithm
    """
    start = get_time()
    self.population = self.generate(self.settings.candidates)
    pop_size = len(self.population)
    self.gen = 0
    print(self.model._tree.name)
    while self.gen < self.settings.gens:
      say(".")
      self.gen += 1
      self.population = self.select(self.population)
      self.population = self.evolve(self.population, pop_size)
    self.runtime = get_time() - start
    objs = [one.objectives for one in self.population]
    print("")
    for i in range(len(self.settings.obj_funcs)):
      lst = [one[i] for one in objs]
      print(self.settings.obj_funcs[i].__name__, min(lst), median_iqr(lst), max(lst))
    print("Runtime : ", get_time()-start)
    return self.population