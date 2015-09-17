__author__ = 'george'
import sys,os
sys.path.append(os.path.abspath("."))
from utilities.lib import *
from parser.OMETree import Parser, Edge

t = +1
f = -1

def coin_toss():
  return random.choice([t, f])

def shuffle(lst):
  random.shuffle(lst)
  return lst

class Model(O):
  def __init__(self, src):
    O.__init__(self)
    self.src = src
    self.properties = 'properties.json'
    self._tree = Parser(src)
    self._tree.parse()
    self._tree.remove_actors()
    self.roots = self._tree.get_roots()
    self.recursions = 0


  def generate(self):
    point_map = {}
    for node in self.roots:
      point_map[node.id] = random.choice([node.lo, node.hi])
    return point_map

  def scores(self, n=1000, seed=None):
    """
    Evaluate the graph n times and
    return the average value
    :param n: Number of evals
    :param seed: Random seed to be set
    :return: The average score
    """
    from utilities.sk import rdivDemo
    if not seed is None:
      random.seed(seed)

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
      if self.eval(node) == t:
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
    return deps, rest


  def eval(self, node):
    self.recursions += 1
    if not node.value is None:
      self.recursions = 0
      return node.value
    if self.recursions > 10:
      status = coin_toss()
    elif not node.from_edges:
      # Random generation
      status = coin_toss()
    else:
      # First check for dependencies from the edges and evaluate it
      # Ask @jenhork about it
      deps, rest= self.dep_and_rest(node.from_edges)

      # Check if all dependencies are satisfied
      dep_nodes = [self._tree.get_node(dep.source) for dep in deps]
      status = self.eval_and(dep_nodes)

      if not rest or status == f:
        return status

      # Evaluate the rest. We assume the rest are of same kind
      edge_type = rest[0].type
      if edge_type == "decompositions":
        kids = [self._tree.get_node(edge.source) for edge in rest]
        if rest[0].value == "and":
          # Evaluate all children
          status = self.eval_and(kids)
        elif rest[0].value == "or":
          status = self.eval_or(kids)
      elif edge_type == "contributions":
        status = self.eval_contribs(rest)
    self.recursions = 0
    node.value = status
    return status

  def eval_and(self, nodes):
    """
    Evaluate all the nodes in the tree
    :param nodes: Nodes to be evaluated
    :return: status
    """
    status = t
    for node in nodes:
      if status == f: break
      status = self.eval(node)
    return status

  def eval_or(self, nodes):
    """
    Evaluate all the nodes in the tree
    till a node is evaluated as true
    :param nodes: Nodes to be evaluated
    :return: status
    """
    for node in nodes:
      status = self.eval(node)
      if status == t:
        return t
    return f

  def eval_contribs(self, edges):
    """
    Evaluate cumulative of contributions
    based on the weight.
    :param edges: Nodes to be evaluated
    :return: status
    """
    status_sum = 0
    wt_sum = 0
    for edge in edges:
      node = self._tree.get_node(edge.source)
      wt = Edge.get_contribution_weight(edge.value)
      status_sum += self.eval(node) * wt
      wt_sum += wt
    status = status_sum / wt_sum
    if status > 0:
      return t
    elif status < 0:
      return f
    else:
      # In case of conflict
      return coin_toss()
