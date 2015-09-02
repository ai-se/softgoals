from __future__ import print_function, division
from utils.lib import *
import xml.etree.ElementTree as ET
__author__ = 'george'


def default_ns():
  return {
    "xmi" : "http://www.omg.org/XMI",
    "model" : "http:///edu/toronto/cs/openome_model.ecore",
    "notation" : "http://www.eclipse.org/gmf/runtime/1.0.2/notation"
  }

class Node(O):
  def __init__(self):
    """
    Creates a node which can represent a
    a) Actor
    b) Agent
    c) Position
    d) Role
    e) Hard goal
    f) Soft goal
    g) Task
    h) Resource
    :return:
    """
    O.__init__(self)
    self.id = None
    self.name = None
    self.type = None
    self.container = None
    self.to_edges = None
    self.from_edges = None

  @staticmethod
  def get_type(key):
    node_map = {
      "edu.toronto.cs.openome_model:Goal"     : "goal",
      "edu.toronto.cs.openome_model:Resource" : "resource",
      "edu.toronto.cs.openome_model:Task"     : "task",
      "edu.toronto.cs.openome_model:Softgoal" : "softgoal",
      "edu.toronto.cs.openome_model:Actor"    : "actor",
      "edu.toronto.cs.openome_model:Agent"    : "agent",
      "edu.toronto.cs.openome_model:Position" : "position",
      "edu.toronto.cs.openome_model:Role"     : "role",
    }
    return node_map.get(key)

  def __hash__(self):
    if not self.id:
      return 0
    return hash(self.id)

  def __eq__(self, other):
    if not self.id or not other.id:
      return False
    return self.id == other.id


class Edge(O):
  def __init__(self):
    """
    Creates an edge which can represent
    a) Dependency
    b) Decomposition
      - AND
      - OR
    c) Contribution
      - Help
      - Hurt
      - Make
      - Break
      - Some Plus
      - Some Minus
      - Conflict
      - Unknown
    :return:
    """
    O.__init__(self)
    self.id = None
    self.type = None
    self.value = None
    self.source = None
    self.destination = None

  @staticmethod
  def get_type(key):
    edge_map = {

    }


  def __hash__(self):
    if not self.id:
      return 0
    return hash(self.id)

  def __eq__(self, other):
    if not self.id or not other.id:
      return False
    return self.id == other.id

class Parser(O):

  def __init__(self, src, ns = None):
    """
    Initialize Parser with source file
    :param src:
    :param ns: Namespace with source
    :return:
    """
    O.__init__(self)
    self.src = src
    if not ns:
      ns = default_ns()
    self.ns = ns
    Parser.register_namespace(self.ns)
    self.nodes = None
    self.edges = None

  @staticmethod
  def register_namespace(ns):
    """
    Registers a dictionary of namespace in the parse tree
    :param ns:
    :return:
    """
    for key, val in ns.iteritems():
      ET.register_namespace(key, val)

  def add_node(self, node):
    """
    Add a node to list of nodes for graph
    :param node: Node to be added
    :return:
    """
    if not self.nodes:
      self.nodes = set()
    self.nodes.add(node)

  def add_edge(self, edge):
    """
    Add an edge to set of edges for graph
    :param edge: Edge to be added
    :return:
    """
    if not self.edges:
      self.edges = set()
    self.edges.add(edge)

  def get_attribute(self, element, key):
    """
    Retrieve and attribute from an element of xml
    :param element:
    :param key:
    :return:
    """
    parts = key.split(":")
    if len(parts) == 2:
      val = self.ns[parts[0]]
      if not val:
        raise RuntimeError(key + " not found in namespace.")
      attrib_key = "{" + val + "}" + parts[-1]
    else:
      attrib_key = parts[-1]
    return element.attrib.get(attrib_key, None)

  def parse_node(self, element, container=None):
    """
    Method to parse a node element and create an object
    :param element: Node Element
    :param container: Its parent container
    """
    node = Node()
    node.id = self.get_attribute(element, 'xmi:id')
    node.name = self.get_attribute(element, 'name')
    node.type = Node.get_type(self.get_attribute(element, 'xmi:type'))
    from_edges = []
    froms = self.get_attribute(element, 'contributesFrom')
    if froms:
      from_edges += froms.split(" ")
    froms = self.get_attribute(element, 'dependencyFrom')
    if froms:
      from_edges += froms.split(" ")
    froms = self.get_attribute(element, 'parentDecompositions')
    if froms:
      from_edges += froms.split(" ")
    node.from_edges = from_edges
    # Means - Ends From
    to_edges = []
    tos = self.get_attribute(element, 'contributesTo')
    if tos:
      to_edges += tos.split(" ")
    tos = self.get_attribute(element, 'dependencyTo')
    if tos:
      to_edges += tos.split(" ")
    tos = self.get_attribute(element, 'decompositions')
    if tos:
      to_edges += tos.split(" ")
    node.to_edges = to_edges
    # Means - Ends To
    if container:
      node.container = container
    self.add_node(node)

  def parse_edge(self, element):
    edge = Edge()
    edge.id = self.get_attribute(element, 'xmi:id')


  def parse(self):
    """
    Parse xml tree for the file
    :param ns: Namespace to follow
    :return: XML Tree object
    """
    tree = ET.parse(self.src)
    model = tree.getroot().find("model:Model", self.ns)
    for child in model.findall("intentions"):
      self.parse_node(child)

    print(self)
