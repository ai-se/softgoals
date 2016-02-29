from __future__ import print_function, division
__author__ = 'panzer'
import sys,os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from template import *
from copy import deepcopy
from pyAHP.model import Point, Model
import numpy as np

class MaximumSubset(O):
  """
  Maximum Subset of a tree
  """
  def __init__(self, tree):
    O.__init__(self)
    self.tree = tree

  def generate(self):
    subsets = sorted(self.estimate(self.tree.root, []), key=lambda x: len(x), reverse=True)
    max_length = len(subsets[0])
    maximal_subsets = []
    for subset in subsets:
      if len(subset) < max_length:
        return maximal_subsets
      else:
        maximal_subsets.append(subset)

  def estimate(self, node, subsets):
    kids, edge_type = self.tree.get_children(node)
    if kids is None:
      if len(subsets) == 0:
        subsets.append([node.id])
      else:
        for decision_set in subsets:
          decision_set.append(node.id)
      return subsets
    if edge_type == "and":
      for kid in kids:
        subsets = self.estimate(kid, subsets)
    elif edge_type == "or":
      resultant = []
      for kid in kids:
        subset_copy = deepcopy(subsets)
        resultant += self.estimate(kid, subset_copy)
      subsets = resultant
    return subsets

  def evaluate(self):
    def stats(a):
      mean = sorted(a)[len(a)//2]
      q75, q25 = np.percentile(a, [75 ,25])
      iqr = q75 - q25
      return [mean, iqr, max(a), min(a)]
    maximal_subsets = self.generate()
    points = []
    bases = self.tree.get_bases()
    model = Model(self.tree)
    objs = []
    for subset in maximal_subsets:
      decisions = {}
      decision_cost = 0
      for base in bases:
        if base.id in subset:
          decisions[base.id] = t
          decision_cost += base.base_cost
        else:
          decisions[base.id] = f
      point = Point(decisions)
      self.tree.evaluate(model, point)
      objs.append(point.objectives+[decision_cost])
      points.append(Point)
    print(map(stats, zip(*objs)))
    return points

def _main():
  from pyAHP.models.sample import tree
  subsets = MaximumSubset(tree).evaluate()

if __name__ == "__main__":
  _main()