from __future__ import print_function
__author__ = 'george'
import os, sys, json
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

# Edge Values
# make = "make"
# help = "help"
# someplus = "someplus"
# someminus = "someminus"
# hurt = "hurt"
# destroy = "break"
# conflict = "conflict"
# AND = "and"
# OR = "or"
# dep = dependency = "dependency"
#
# # Node Types
# softgoal = "softgoal"
# hardgoal = "goal"
# task = "task"
# resource = "resource"
# agent = "agent"
# role = "role"


class O(object):
  """
  Default class that gives
  kwargs properties
  """
  def __init__(self,**d): self.has().update(**d)
  def has(self): return self.__dict__
  def update(self,**d): self.has().update(d); return self
  def __repr__(self)   :
    def _name(val):
      if isinstance(val, list):
        return [v for v in val]
      if hasattr(val, '__call__'):
        return val.__name__
      return val
    show=[':%s %s' % (k,_name(self.has()[k]))
      for k in sorted(self.has().keys() )
      if k[0] is not "_"]
    txt = ' '.join(show)
    if len(txt) > 60:
      show=map(lambda x: '\t'+x+'\n',show)
    return '{'+' '.join(show)+'}'
  def __getitem__(self, item):
    return self.has().get(item, None)
  def __getattr__(self, item):
    return self.has().get(item, None)
  def to_json(self):
    def dflt(obj):
      if isinstance(obj, set): return list(obj)
      return obj.__dict__
    return json.dumps(self, default=dflt, sort_keys=True, indent=4)
  def clone(self):
    cloned = O()
    for key, val in self.has().iteritems():
      cloned.__dict__[key] = val
    return cloned

class Component(O):
  """
  All components of graph
  should extend this class
  """
  id = 0
  def __init__(self, component, **kwargs):
    O.__init__(self, **kwargs)
    self.id = Component.id
    self.component = component
    Component.id += 1

  def __hash__(self):
    if not self.id:
      return 0
    return hash(self.id)

  def __eq__(self, other):
    if not self.id or not other.id:
      return False
    return self.id == other.id

class Node(Component):
  """
  Node of a graph
  """
  def __init__(self, name, type, **kwargs):
    Component.__init__(self, "node", name=name, type=type, **kwargs)
    self.from_edges = []
    self.to_edges = []

  def add_edge(self, edge_id, type):
    if type == "from":
      self.from_edges.append(edge_id)
    else:
      self.to_edges.append(edge_id)

class Task(Node):
  """
  A Task node.
  """
  def __init__(self, name, container=None, **kwargs):
    Node.__init__(self, name, "task", container=container, **kwargs)

class Resource(Node):
  """
  A resource node
  """
  def __init__(self, name, container=None, **kwargs):
    Node.__init__(self, name, "resource", container=container, **kwargs)

class SoftGoal(Node):
  """
  A Soft goal node
  """
  def __init__(self, name, container=None, **kwargs):
    Node.__init__(self, name, "softgoal", container=container, **kwargs)

class HardGoal(Node):
  """
  A Hard Goal Node
  """
  def __init__(self, name, container=None, **kwargs):
    Node.__init__(self, name, "goal", container=container, **kwargs)

class Edge(Component):
  """
  Edge of a graph
  """
  def __init__(self, source, target, **kwargs):
    Component.__init__(self, "edge", **kwargs)
    self.source = source.id
    self.target = target.id

  @staticmethod
  def get_contribution_weight(key):
    if key == "make":
      return +3
    elif key == "help":
      return +2
    elif key == "someplus":
      return +1
    elif key == "someminus":
      return -1
    elif key == "hurt":
      return -2
    elif key == "break":
      return -3
    raise RuntimeError("Invalid contribution type %s"%key)

class Make(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "make"
    self.type = "contribution"

class Help(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "help"
    self.type = "contribution"

class SomePlus(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "someplus"
    self.type = "contribution"

class SomeMinus(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "someminus"
    self.type = "contribution"

class Hurt(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "hurt"
    self.type = "contribution"

class Break(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "break"
    self.type = "contribution"

class Conflict(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "conflict"
    self.type = "contribution"

class And(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "and"
    self.type = "decompositions"

class Or(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "or"
    self.type = "decompositions"

class Dep(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "dependency"
    self.type = "dependency"

class Many:
  """
  An Array object
  """
  def __init__(self):
    self.all = []

  def __add__(self, other):
    self.all.append(other)
    return other

class Graph(O):
  """
  Graph object
  """
  def __init__(self, name, nodes, edges):
    O.__init__(self, name=name, nodes=nodes, edges=edges)
    self.update_nodes()

  def update_nodes(self):
    node_map = {}
    for node in self.nodes:
      node_map[node.id] = node
    for edge in self.edges:
      node_map[edge.source].add_edge(edge.id, "to")
      node_map[edge.target].add_edge(edge.id, "from")

  def get_edge(self, edge_id):
    for edge in self.edges:
      if edge.id == edge_id:
        return edge
    return None

  def get_node(self, node_id):
    for node in self.nodes:
      if node.id == node_id:
        return node
    return None

  def get_bases(self):
    """
    Get the base decisions of the graph
    :return:
    """
    nodes = []
    for node in self.nodes:
      if node.type in ['task', 'resource']:
        # We assume that decisions are either tasks or resources
        if not node.from_edges:
          nodes.append(node)
    return nodes

  def get_roots(self):
    """
    Get roots of the tree
    :return:
    """
    nodes = []
    for node in self.nodes:
      if not node.to_edges:
        nodes.append(node)
    return nodes

  def get_nodes_covered(self):
    return [node for node in self.get_nodes() if node.value]

  def get_nodes(self, node_type=None):
    """
    Get nodes of a certain type
    :param node_type:
    :return:
    """
    if isinstance(node_type, list):
      return [node for node in self.nodes if node.type in node_type]
    elif isinstance(node_type, str):
      return [node for node in self.nodes if node.type in [node_type]]
    else: return self.nodes


