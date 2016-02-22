from __future__ import print_function, division
__author__ = 'panzer'
import sys,os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
import pydot as dot
from utilities.lib import *
import colorsys

def get_color_ranges_hex(size):
  hsv_tuples = [(x*1.0/size, 0.5, 0.5) for x in range(size)]
  rgb_tuples = map(lambda hsv: colorsys.hsv_to_rgb(*hsv), hsv_tuples)
  rgb_tuples = ['#%02x%02x%02x'%(int(r*255), int(g*255), int(b*255)) for (r,g,b) in rgb_tuples]
  return rgb_tuples

def get_color_ranges(size):
  hsv_tuples = [(x*1.0/size, 0.5, 0.5) for x in range(size)]
  rgb_tuples = map(lambda hsv: colorsys.hsv_to_rgb(*hsv), hsv_tuples)
  rgb_tuples = [(int(r*255), int(g*255), int(b*255)) for (r,g,b) in rgb_tuples]
  return rgb_tuples

class Grapher(O):
  def __init__(self, tree, decisions, folder_path):
    O.__init__(self)
    self.tree = tree
    self.decisions = {}
    self.decision_ranks = {}
    self.colors = {}
    self.rank_decisions(decisions)
    self.folder_path = folder_path

  def rank_decisions(self, decisions):
    colors = get_color_ranges_hex(len(decisions))
    for i, decision in enumerate(decisions):
      self.decision_ranks[decision.id] = i+1
      self.decisions[decision.id] = decision
      self.colors[decision.id] = colors[i]

  def draw_tree(self):
    tree = self.tree
    graph = dot.Dot(graph_type='digraph', graph_name=tree.name, rankdir="BT")
    node_map = {}
    for node_id, node in tree.nodes.items():
      node_map[node_id] = self.make_node(node)
      graph.add_node(node_map[node_id])
    edge_map = {}
    for edge_id, edge in tree.edges.items():
      edge_map[edge.id] = self.make_edge(node_map[edge.source], node_map[edge.target], edge)
      graph.add_edge(edge_map[edge.id])
    graph.write_png("img/"+self.folder_path+"/"+tree.name+"_tree.png")
    return tree.name+"_tree"

  def make_node(self, inp_node):
    if inp_node.type == "task":
      shape = "hexagon"
    elif inp_node.type == "resource":
      shape = "rectangle"
    elif inp_node.type == "softgoal":
      shape = "tripleoctagon"
    else:
      shape = "ellipse"
    rank = self.decision_ranks.get(inp_node.id, None)
    name = inp_node.name
    if rank is not None:
      dec_node = self.decisions[inp_node.id]
      name += "\nRank = %d\nSupport = %f\nValue = %d"%(rank, dec_node.support, dec_node.value)
      node = dot.Node(name=name, fontsize=9, shape=shape, style="filled", fillcolor=self.colors[inp_node.id])
    else:
      node = dot.Node(name=name, fontsize=9, shape=shape)
    return node

  def make_edge(self, source, target, inp_edge):
    if inp_edge.value == "and":
      arrow_type="normal"
    else:
      arrow_type="onormal"
    edge = dot.Edge(source, target, arrowhead=arrow_type)
    return edge

