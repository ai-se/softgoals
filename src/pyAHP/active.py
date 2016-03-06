from __future__ import print_function, division
import sys,os
sys.path.append(os.path.abspath("."))
from utilities.lib import *
from pyAHP.de import DE
from pyAHP.model import Model
__author__ = 'panzer'


# TODO - Select cost and benefit from triangular functions
# TODO - Run an MOEA to select top decisions that yield lowest cost and highest benefit.
# TODO - Somehow find values of cost and benefit that change the decisions selected.

def default_settings():
  return O(
    gens = 1000
  )

class Active(O):
  """
  Identifying the importance of decisions
  """
  def __init__(self, model, **settings):
    """
    Initialize the Active Learner
    :param model:
    :return:
    """
    O.__init__(self)
    self.de = DE(model)
    self.settings = default_settings().update(**settings)


  def learn(self):
    best_points = []
    for _ in range(self.settings.gens):
      say(".")
      self.de.model.generate_costs_benefits()
      stat = self.de.run()
      last_gen = stat.generations[-1]
      gen_best_costs = set()
      gen_best_benefits = set()
      best_cost = sys.maxint
      best_benefit = -sys.maxint
      for point in last_gen:
        if point.objectives[1] > best_benefit:
          gen_best_benefits = set()
          gen_best_benefits.add(point)
        elif point.objectives[1] == best_benefit:
          gen_best_benefits.add(point)
        if point.objectives[0] < best_cost:
          gen_best_costs = set()
          gen_best_costs.add(point)
        elif point.objectives[0] == best_cost:
          gen_best_costs.add(point)
      best_points += list(gen_best_costs)
      best_points += list(gen_best_benefits)
    return best_points

def _main():
  from pyAHP.models.sample import tree
  model = Model(tree, generation_mode = "triangular")
  active = Active(model)
  active.learn()


if __name__ == "__main__":
  _main()

