from __future__ import print_function
__author__ = 'panzer'
import os, sys, json
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

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
    self.is_random = False
    self.weighted_cost = 0
    # For Attributes
    self.benefit = 0
    self.cost = 0
    self.value = None

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

class And(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "and"

class Or(Edge):
  """
  Make Contribution edge.
  """
  def __init__(self, source, target, **kwargs):
    Edge.__init__(self, source, target, **kwargs)
    self.value = "or"

class Many:
  """
  An Array object
  """
  def __init__(self):
    self.all = []

  def __add__(self, other):
    self.all.append(other)
    return other

class Tree(O):
  """
  AHP Tree object
  """
  def __init__(self, name, nodes, edges, root, max_level):
    node_map, edge_map = {}, {}
    for node in nodes: node_map[node.id] = node
    for edge in edges: edge_map[edge.id] = edge
    O.__init__(self, name=name, nodes=node_map,
               edges=edge_map, root = root,
               max_level = max_level)
    self.update_nodes()

  def update_nodes(self):
    """
    Update Source and Targets for each node
    :return:
    """
    for edge in self.edges.values():
      self.nodes[edge.source].add_edge(edge.id, "to")
      self.nodes[edge.target].add_edge(edge.id, "from")

  def get_edge(self, edge_id):
    """
    Retrieve an Edge
    :param edge_id:
    :return:
    """
    return self.edges.get(edge_id, None)

  def get_node(self, node_id):
    """
    Retrieve a Node
    :param node_id:
    :return:
    """
    return self.nodes.get(node_id, None)

  def get_bases(self):
    """
    Get leaves of a Tree
    :return:
    """
    nodes = []
    for node in self.nodes.values():
      if not node.from_edges:
        nodes.append(node)
    return nodes

  def get_nodes(self, node_type=None):
    """
    Get nodes of a certain type
    :param node_type:
    :return:
    """
    if isinstance(node_type, list):
      return [node for node in self.nodes.values() if node.type in node_type]
    elif isinstance(node_type, str):
      return [node for node in self.nodes.values() if node.type in [node_type]]
    else: return self.nodes.values()

  def get_node_by_name(self, name):
    """

    :param name:
    :return:
    """
    nodes = self.nodes.values()
    for node in nodes:
      if node.name == name:
        return node
    return None
