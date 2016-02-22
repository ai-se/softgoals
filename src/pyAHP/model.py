from __future__ import print_function, division
__author__ = 'panzer'
import sys,os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from template import *
import random
from math import exp

t, f = 1, -1

def coin_toss():
  return random.choice([t, f])

def percent(num, den):
  if den==0:
    return 0
  return round(num*100/den, 2)

def shuffle(lst):
  if not lst:
    return []
  random.shuffle(lst)
  return lst

class Model(O):
  def __init__(self, tree, **settings):
    O.__init__(self)
    self.settings = O().update(**settings)
    self._tree = tree
    self.bases = self._tree.get_bases()

  def get_tree(self):
    return self._tree

  def generate_costs(self):
    """
    Generate random cost for each node
    :return:
    """
    vl, l, m, h, vh = 1, 5, 20, 100, 1000
    cost_map = {}
    for node_id in self._tree.nodes.keys():
      rand = random.random()
      if rand <= 0.2:
        val = vl
      elif rand <= 0.45:
        val = l
      elif rand <= 0.75:
        val = m
      elif rand <= 0.95:
        val = h
      else:
        val = vh
      cost_map[node_id] = val
    return cost_map

  def generate_benefits(self):
    """
    Dummy method that does same as generate benefits
    :return:
    """
    return self.generate_costs()

  def generate(self):
    point_map = {}
    for node in self.bases:
      point_map[node.id] = random.choice([t, f])
    return point_map

  def get_node_base_cost(self, node):
    return node.base_cost
    if node.base_cost == 0:
      return 0
    level = 0
    if hasattr(node, 'level'):
      level = node.level
    return exp(node.base_cost) * exp(self.get_tree().max_level-level)

  def get_node_base_benefit(self, node):
    return node.base_benefit
    if node.base_benefit == 0:
      return 0
    level = 0
    if hasattr(node, 'level'):
      level = node.level
    return exp(node.base_benefit) * exp(self.get_tree().max_level-level)

  def clear_nodes(self):
    for node in self._tree.nodes.values():
      node.value = None
      node.is_random = False
      node.cost = self.get_node_base_cost(node)
      node.benefit = self.get_node_base_benefit(node)
      node.selected = None

  def reset_nodes(self, initial_node_map):
    self.clear_nodes()
    for node in self.bases:
      node.value = initial_node_map[node.id]

  def evaluate_constraints(self, decisions):
    self.clear_nodes()
    for node in self.bases:
      node.value = decisions[node.id]
    root = self.get_tree().root
    self.eval(root)
    if root.cost is None or root.benefit is None:
      return False, 0
    else:
      return True, 0

  def check_constraints(self, point, obj_funcs):
    if not point.objectives:
      Point.evaluate(point, self, obj_funcs)
    root = self.get_tree().root
    return root.cost > 0 and root.benefit > 0

  def eval(self, node):
    if not node.value is None: return
    if not node.from_edges:
      assert False, "No Edges and not a decision."
    edges = [self._tree.get_edge(edge_id) for edge_id in node.from_edges]
    edge_type = edges[0].value
    kids = [self._tree.get_node(edge.source) for edge in edges]
    if edge_type == "and":
      value, cost, benefit = self.eval_and(kids)
      node.value = value
      if value == t:
        node.cost += cost
        node.benefit += benefit
      else:
        node.cost, node.benefit = None, None
    elif edge_type == "or":
      value, selected_node = self.eval_or(kids)
      node.value = value
      node.selected = selected_node
      if node.value == t:
        node.cost += selected_node.cost
        node.benefit += selected_node.benefit
      else:
        node.cost, node.benefit = None, None
    else:
      assert False, "Invalid edge type %s"%edge_type

  def eval_and(self, nodes):
    """
    Evaluate all the nodes in the tree
    :param nodes: Nodes to be evaluated
    :return:
    """
    cost, benefit = 0, 0
    for node in nodes:
      self.eval(node)
      if node.value == f:
        return f, None, None
      cost += node.cost
      benefit += node.benefit
    return t, cost, benefit

  def eval_or(self, nodes):
    """
    Evaluate either of the kids of tree
    :param nodes: Nodes to be evaluated
    :return:
    """
    for node in shuffle(nodes):
      self.eval(node)
      if node.value == t:
        return t, node
    return f, None

  def better(self, one, two):
    """
    Check which of the points are better using bdom
    :param one: Point 1
    :param two: Point 2
    :return:
      0 - Non Dominated
      1 - Point 1 dominates Point 2
      2 - Point 2 dominates Point 1
    """
    def compare(i, j, func):
      if i == j:
        return 0
      return 1 if func(i,j) else -1

    obj1 = one.objectives
    obj2 = two.objectives
    one_at_least_once = False
    two_at_least_once = False
    for index, (a, b) in enumerate(zip(obj1, obj2)):
      status = compare(a, b, self.settings.better[index])
      if status == -1:
        #obj2[i] better than obj1[i]
        two_at_least_once = True
      elif status == 1:
        #obj1[i] better than obj2[i]
        one_at_least_once = True
      if one_at_least_once and two_at_least_once:
        #neither dominates each other
        return 0
    if one_at_least_once:
      return 1
    elif two_at_least_once:
      return 2
    else:
      return 0


class Point(O):
  id = 0
  def __init__(self, decisions, objectives=None):
    O.__init__(self)
    Point.id += 1
    self.id = Point.id
    self.decisions = decisions
    self.objectives = objectives
    self._nodes = None
    # Attributes for NSGA2
    self.dominating = 0
    self.dominated = []
    self.crowd_dist = 0

  def get_nodes(self):
    return self._nodes

  def get_node_by_name(self, name):
    """

    :param name:
    :return:
    """
    for node in self._nodes:
      if node.name == name:
        return node
    return None

  def __hash__(self):
    objs = []
    if self.objectives:
      for obj in self.objectives:
        if obj is None:
          objs.append(0)
        else:
          objs.append(obj)
    if type(self.decisions) == dict:
      return hash(frozenset(self.decisions.items())) + hash(frozenset(objs))
    return hash(frozenset(self.decisions)) + hash(frozenset(objs))

  def __eq__(self, other):
    return cmp(self.decisions, other.decisions) == 0 and self.objectives == other.objectives

  @staticmethod
  def evaluate(point, model, obj_funcs):
    if not point.objectives:
      model.reset_nodes(point.decisions)
      model.eval(model.get_tree().root)
      point.objectives = [func(model) for func in obj_funcs]
      point._nodes = [node.clone() for node in model.get_tree().nodes.values()]
    return point.objectives

  @staticmethod
  def evaluate_cost(model):
    return model.get_tree().root.cost

  @staticmethod
  def evaluate_benefit(model):
    return model.get_tree().root.benefit

  @staticmethod
  def evaluate_softgoals(model):
    softgoals = model.get_tree().get_nodes(node_type="softgoal")
    satisfied = 0
    for node in softgoals:
      model.eval(node)
      if node.value == t:
        satisfied += 1
    return satisfied

  @staticmethod
  def trim(val):
    if val > 0:
      return t
    else:
      return f


def _main():
  from pyAHP.models.sample import tree
  model = Model(tree)
  inps = model.generate()
  model.reset_nodes(inps)
  model.eval(model.get_tree().root)
  print(model.get_tree().root.cost, model.get_tree().root.benefit)

if __name__ == "__main__":
  _main()




