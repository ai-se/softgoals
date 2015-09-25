__author__ = 'george'
import sys,os
sys.path.append(os.path.abspath("."))
from utilities.lib import *
from parser.OMETree import Parser, Edge

def coin_toss():
  return random.choice([t, f])

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
    self.chain = set()


  def generate(self):
    point_map = {}
    for node in self.roots:
      point_map[node.id] = random.choice([t, f])
    return point_map

  def clear_nodes(self):
    for node in self._tree.nodes:
      node.value = None

  def evaluate_score(self, initial_node_map):
    self.clear_nodes()
    for key in initial_node_map.keys():
      node = self._tree.get_node(key)
      node.value = initial_node_map[key]
    return self.score()

  def evaluate_type(self, initial_node_map, node_type):
    self.clear_nodes()
    for key in initial_node_map.keys():
      node = self._tree.get_node(key)
      node.value = initial_node_map[key]
    count = 0
    for node in self._tree.get_nodes(node_type=node_type):
      self.chain = set()
      if self.eval(node) == t:
        count += 1
    return count

  def  scores(self, n=1000, seed=None):
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
      self.chain = set()
      self.recursions = 0
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
    #return shuffle(deps), shuffle(rest)


  def eval(self, node):
    if not node.value is None:
      return node.value
    if node.id in self.chain:
      node.value = coin_toss()
      return node.value
    self.recursions += 1
    self.chain.add(node.id)
    #if (self.recursions > 10) or (not node.from_edges):
    if not node.from_edges:
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
    kids = []
    for edge in edges:
      node = self._tree.get_node(edge.source)
      kids += [Model.soft_goal_val(node.value, edge.value)]
    return choice(kids)

  @staticmethod
  def soft_goal_val(kid, edge):
    """
    Check out src/img/prop_rules.png
    :param kid:
    :param edge:
    :return:
    """
    if edge in ["someplus", "someminus"]:
      return choice([t/2, f/2])
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

