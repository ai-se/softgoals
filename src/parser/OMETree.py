from __future__ import print_function, division
import xml.etree.ElementTree as ET
from parser_utils import *
__author__ = 'george'

def default_ns():
  return {
    "xmi" : "http://www.omg.org/XMI",
    "model" : "http:///edu/toronto/cs/openome_model.ecore",
    "notation" : "http://www.eclipse.org/gmf/runtime/1.0.2/notation"
  }


class OMEParser(Parser):

  def __init__(self, src, ns = None):
    """
    Initialize Parser with source file
    :param src:
    :param ns: Namespace with source
    :return:
    """
    Parser.__init__(self, src)
    if not ns: ns = default_ns()
    self.ns = ns
    OMEParser.register_namespace(self.ns)

  @staticmethod
  def register_namespace(ns):
    """
    Registers a dictionary of namespace in the parse tree
    :param ns:
    :return:
    """
    for key, val in ns.iteritems():
      ET.register_namespace(key, val)


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

  def parse_edge(self, element, edge_type):
    """
    Method to parse an edge element and create an object
    :param element: Edge Element
    :param edge_type: type of the edge
    """
    edge = Edge()
    edge.id = self.get_attribute(element, 'xmi:id')
    edge.type = edge_type
    edge.value = Edge.get_value(self.get_attribute(element, 'xmi:type'))
    source = self.get_attribute(element, 'source')
    if not source:
      source = self.get_attribute(element, 'dependencyFrom')
    edge.source = source
    target = self.get_attribute(element, 'target')
    if not target:
      target = self.get_attribute(element, 'dependencyTo')
    edge.target = target
    self.add_edge(edge)

  def parse(self):
    """
    Parse xml tree for the file
    """
    tree = ET.parse(self.src)
    model = tree.getroot().find("model:Model", self.ns)
    for child in model.findall("intentions"):
      self.parse_node(child)
    for child in model.findall("contributions"):
      self.parse_edge(child, "contribution")
    for child in model.findall("dependencies"):
      self.parse_edge(child, "dependency")
    for child in model.findall("decompositions"):
      self.parse_edge(child, "decompositions")
    for container in model.findall("containers"):
      self.parse_node(container)
      container_id = self.get_attribute(container, 'xmi:id')
      for child in container.findall("intentions"):
        self.parse_node(child, container_id)


  def get_other_end(self, edge_id, one_end):
    for edge in self.edges:
      if edge.id == edge_id:
        if edge.source == one_end:
          return edge.target
        elif edge.target == one_end:
          return edge.source
        else:
          return None

  @staticmethod
  def from_json(json_obj):
    #TODO implement method to load from json
    pass