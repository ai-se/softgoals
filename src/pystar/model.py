from __future__ import print_function, division
__author__ = 'george'
import sys,os, copy
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from template import *
import random

t =  1
f = -1
#wt_delta = 0.1
wt_delta = 0

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
    self.roots = self._tree.get_roots()
    #self.bases = self._tree.get_bases()
    self.bases = self._tree.get_leaves()
    self.chain = set()
    self.recursions = 0
    self.cost_map = {}
    self.assign_costs()

  def assign_costs(self):
    cost_map = {}
    """
    Random Costs Below
    """
    # rands = range(1,6)
    # for base in self.bases:
    #   cost_map[base.id] = random.choice(rands)
    """
    Fixed cost of 1
    """
    for base in self.bases:
      cost_map[base.id] = 1
    self.cost_map = cost_map

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

  def get_tree(self):
    return self._tree

  def generate(self):
    point_map = {}
    for node in self.bases:
      point_map[node.id] = random.choice([t, f])
    return point_map

  def evaluate_constraints(self, decisions):
    return True, 0

  def clear_nodes(self):
    for node in self._tree.nodes:
      node.value = None
      node.is_random = False
      node.cost = 0

  def reset_nodes(self, initial_node_map):
    self.clear_nodes()
    for key in initial_node_map.keys():
      node = self._tree.get_node(key)
      node.value = initial_node_map[key]

  def evaluate_score(self, initial_node_map):
    self.clear_nodes()
    for key in initial_node_map.keys():
      node = self._tree.get_node(key)
      node.value = initial_node_map[key]
    return self.score()

  def evaluate_type(self, node_type, is_percent=False):
    count = 0
    nodes = shuffle(self._tree.get_nodes(node_type=node_type))
    for node in nodes:
      self.chain = set()
      self.eval(node)
      if node.value > 0:
        count += 1
    if is_percent:
      return percent(count, len(nodes))
    else:
      return count

  def evaluate_random(self):
    def check_status():
      for node in self._tree.nodes:
        if node.type in ["goal", "softgoal"] and (not node.value):
          return False
      return True
    for _ in range(len(self._tree.nodes)//2):
      self.chain = set()
      self.eval(random.choice(self._tree.nodes))


  def eval_node(self, node):
    self.chain=set()
    self.eval(node)

  def scores(self, n=1000, seed_val=None):
    """
    Evaluate the graph n times and
    return the average value
    :param n: Number of evals
    :param seed_val: Random seed to be set
    :return: The average score
    """
    from utilities.sk import rdivDemo
    if not seed_val is None:
      random.seed(seed_val)

    final = []
    for _ in xrange(n):
      for node in self._tree.nodes:
        node.value = None
      final.append(self.score())
    final = ["Roots"] + final
    rdivDemo([final])

  def score(self):
    """
    Back Propagation
    Count how many root nodes are covered
    :return: root nodes covered
    """
    count = 0
    for node in self.roots:
      self.chain = set()
      self.recursions = 0
      self.eval(node)
      if node.value > 0:
        count += 1
    return count

  def dep_and_rest(self, edges):
    """
    Split edges into dependencies and the rest
    :param edges:
    :return:
    """
    deps = []
    rest = []
    for edge_id in edges:
      edge = self._tree.get_edge(edge_id)
      if edge.type == "dependency":
        deps.append(edge)
      else:
        rest.append(edge)
    return shuffle(deps), shuffle(rest)

  @staticmethod
  def random_node_val(node):
    """
    Return a random value for a node
    :param node:
    :return:
    """
    if node.type in ["goal", "softgoal"]:
      return t
    return coin_toss()

  def eval(self, node):
    if not (node.value is None): return

    if node.id in self.chain:
      node.value = Model.random_node_val(node)
      node.is_random = True
      if node.value > 0:
        node.cost = 1
      return
    self.recursions += 1
    self.chain.add(node.id)
    if not node.from_edges:
      node.value = Model.random_node_val(node)
      node.is_random = True
      if node.value > 0:
        node.cost = 1
      return
    else:
      # First check for dependencies from the edges and evaluate it
      # Ask @jenhork about it

      deps, rest= self.dep_and_rest(node.from_edges)
      # if rest and rest[0].type == "contribution":
      #   exit()
      # Check if all dependencies are satisfied
      dep_nodes = [self._tree.get_node(dep.source) for dep in deps]


      if not rest:
        node.value, temp_cost = self.eval_and(dep_nodes)
        return

      # Evaluate the rest. We assume the rest are of same kind
      edge_type = rest[0].type
      if edge_type == "decompositions":
        status, cost = self.eval_and(dep_nodes)
        if status < 0:
          node.value = status
          return
        kids = [self._tree.get_node(edge.source) for edge in rest]
        temp_cost = 0
        if rest[0].value == "and":
          # Evaluate all children
          status, temp_cost = self.eval_and(kids)
        elif rest[0].value == "or":
          status, temp_cost = self.eval_or(kids)
        cost += temp_cost
      elif edge_type == "contribution":
        status, cost = self.eval_contribs(rest, deps)
      else:
        raise Exception("Unexpected edge type %s"%edge_type)
      node.value = status
      if node.value > 0:
        node.cost = cost
      return

  def eval_and(self, nodes):
    """
    Evaluate all the nodes in the tree
    :param nodes: Nodes to be evaluated
    :return: status
    """
    status = t
    cost = 0
    for node in nodes:
      self.eval(node)
      status, temp_cost = node.value, node.cost
      cost += temp_cost
      if status <= 0: return status, 0
    return status, cost + 1

  def eval_or(self, nodes):
    """
    Evaluate all the nodes in the tree
    till a node is evaluated as true
    :param nodes: Nodes to be evaluated
    :return: status
    """
    cost = 0
    for node in shuffle(nodes):
      self.eval(node)
      cost += node.cost
      if node.value > 0:
        return node.value, cost + 1
    return f, 0

  def eval_contribs(self, edges, dependencies=None):
    """
    Evaluate cumulative of contributions
    based on the weight.
    :param edges: Nodes to be evaluated
    :return: status
    """
    if dependencies:
      for dep in dependencies:
        dep_node = self._tree.get_node(dep.source)
        self.eval(dep_node)
        val = Model.soft_goal_val(dep_node.value, "make")
        if val <= 0: return val, 0
    val = f
    cost = 0
    for edge in shuffle(edges):
      if edge.type != "contribution":
        continue
      node = self._tree.get_node(edge.source)
      self.eval(node)
      cost += node.cost
      val = Model.soft_goal_val(node.value, edge.value)
      if val > 0:
        return val, cost + 1
    return val, 0

  @staticmethod
  def soft_goal_val(kid, edge):
    """
    Check out src/img/prop_rules.png
    :param kid:
    :param edge:
    :return:
    """
    if edge in ["someplus", "someminus"]:
      rand_val = random.choice([t/2, f/2])
      if rand_val > 0:
        return rand_val
      else:
        return rand_val
    if kid == t:
      if edge == "make"   : return t
      if edge == "help"   : return t/2
      if edge == "hurt"   : return f/2
      if edge == "break"  : return f
    elif kid == t/2:
      if edge == "make"   : return t/2
      if edge == "help"   : return t/2
      if edge == "hurt"   : return f/2
      if edge == "break"  : return f/2
    elif kid == f/2:
      if edge == "make"   : return f/2
      if edge == "help"   : return f/2
      if edge == "hurt"   : return t/2
      if edge == "break"  : return t/2
    elif kid == f:
      if edge == "make"   : return f
      if edge == "help"   : return f/2
      if edge == "hurt"   : return t/2
      if edge == "break"  : return t/2

    raise RuntimeError("Either node value %s or edge %s is unknown"%(kid, edge))


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

  def clone(self):
    new = Point(copy.deepcopy(self.decisions), copy.deepcopy(self.objectives))
    new._nodes = self._nodes
    return new


  def get_nodes(self):
    return self._nodes

  def get_randomness(self):
    count = 0
    for node in self._nodes:
      if node.is_random: count+=1
    return percent(count, len(self._nodes))

  def __hash__(self):
    if type(self.decisions) == dict:
      return hash(frozenset(self.decisions.items()))
    return hash(frozenset(self.decisions))

  def __eq__(self, other):
    return cmp(self.decisions, other.decisions) == 0

  @staticmethod
  def evaluate(point, model, obj_funcs):
    if not point.objectives:
      model.reset_nodes(point.decisions)
      point.objectives = [func(model) for func in obj_funcs]
      point._nodes = [node.clone() for node in model.get_tree().get_nodes()]
    return point.objectives

  @staticmethod
  def evaluate_random(point, model, obj_funcs):
    if point.objectives:
      return point.objectives
    model.reset_nodes(point.decisions)
    model.evaluate_random()
    point.objectives = [func(model) for func in obj_funcs]
    point._nodes = [node.clone() for node in model.get_tree().get_nodes()]
    return point.objectives

  @staticmethod
  def trim(val):
    if val > 0:
      return t
    else:
      return f

  @staticmethod
  def eval_roots(model):
    return model.evaluate_score()

  @staticmethod
  def eval_goals(model):
    return model.evaluate_type(node_type="goal", is_percent=model.settings.is_percent)

  @staticmethod
  def eval_softgoals(model):
    return model.evaluate_type(node_type="softgoal", is_percent=model.settings.is_percent)

  @staticmethod
  def eval_all_goals(model):
    return model.evaluate_type(node_type=["softgoal", "goal"], is_percent=model.settings.is_percent)

  @staticmethod
  def eval_coverage(model):
    covered = len(model.get_tree().get_nodes_covered())
    if model.setttings.is_percent:
      return percent(covered, len(model.get_tree().get_nodes()))
    else:
      return len(model.get_tree().get_nodes_covered())

  @staticmethod
  def eval_costs(model):
    total_cost = 0
    for node in model.bases:
      if node.value and node.value > 0:
        total_cost += model.cost_map[node.id]
    return total_cost

  @staticmethod
  def eval_paths(model):
    total_cost = 0
    for node in model.get_tree().get_nodes(node_type=["softgoal", "goal"]):
      if node.value and node.value > 0:
        total_cost += node.cost
    return total_cost

