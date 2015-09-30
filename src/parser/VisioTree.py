from __future__ import print_function, division
import xml.etree.ElementTree as ET
from parser_utils import *
__author__ = 'george'

def default_ns():
  return {}


class VisioParser(Parser):

  def __init__(self, src, ns=None):
    """
    Initialize Parser with source file
    :param src:
    :param ns: Namespace with source
    :return:
    """
    Parser.__init__(self, src)
    if not ns: ns = default_ns()
    self.ns = ns
    VisioParser.register_namespace(self.ns)


  @staticmethod
  def register_namespace(ns):
    """
    Registers a dictionary of namespace in the parse tree
    :param ns:
    :return:
    """
    for key, val in ns.iteritems():
      ET.register_namespace(key, val)