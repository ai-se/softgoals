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
    O.__init__(self)
    self.id = None
    self.text = None
    self.type = None
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

  @staticmethod
  def register_namespace(ns):
    for key, val in ns.iteritems():
      ET.register_namespace(key, val)

  def get_attribute(self, element, key):
    parts = key.split(":")
    if len(parts) == 2:
      val = self.ns[parts[0]]
      if not val:
        raise RuntimeError(key + " not found in namespace.")
      attrib_key = "{" + val + "}" + parts[-1]
    else:
      attrib_key = parts[-1]
    return element.attrib.get(attrib_key, None)


  def parse(self):
    """
    Parse xml tree for the file
    :param ns: Namespace to follow
    :return: XML Tree object
    """
    tree = ET.parse(self.src)
    for child in tree.getroot().find("model:Model", self.ns):
      print(child.tag, ' ==> ',self.get_attribute(child, 'xmi:id'))



