from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
__author__ = 'george'
sys.dont_write_bytecode = True
from utilities.lib import *
from pystar.models.CSAgentSR import graph as CSAgentSR_graph
from pystar.model import Model
from utilities.de import DE

def default():
  return O(
    k1 = 1000,
    k2 = 1000
  )

class Star1(O):
  def __init__(self, model, settings=None):
    O.__init__(self)
    self.model = model
    self.model.bases.extend(self.get_conflicts())
    self.de = DE(model)
    self.settings = settings

  def get_conflicts(self):
    model = self.model
    graph = model.get_tree()
    nodes = []
    for node in graph.get_nodes():
      if node.type == "softgoal" and len(node.from_edges) > 1:
        toggle = None
        for edge_id in node.from_edges:
          edge = graph.get_edge(edge_id)
          if edge.type == "contribution":
            temp_toggle = sign(edge.get_contribution_weight(edge.value))
            if toggle is None: toggle = temp_toggle
            if temp_toggle != toggle:
              nodes.append(node)
              break
    return nodes


def run():
  model = Model(CSAgentSR_graph)
  print(len(model.bases))
  star = Star1(model)
  print(len(star.model.bases))



