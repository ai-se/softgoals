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
    self.text = None
    self.type = None
    self.container = None
    self.to_edges = None
    self.from_edges = None

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

  def parse_intention(self, element):
    # Create Node here
    print(element.tag, ' ===> ' ,self.get_attribute(element, 'xmi:id'))
    print("\n")


  def parse(self):
    """
    Parse xml tree for the file
    :param ns: Namespace to follow
    :return: XML Tree object
    """
    tree = ET.parse(self.src)
    model = tree.getroot().find("model:Model", self.ns)
    for child in model.findall("intentions"):
      self.parse_intention(child)
