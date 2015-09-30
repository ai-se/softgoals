from __future__ import print_function, division
__author__ = 'george'
import sys, os
from utilities.lib import *


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
    self.value = None
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
    self.target = None

  @staticmethod
  def get_value(key):
    edge_map = {
      # Contributions
      "edu.toronto.cs.openome_model:SomePlusContribution" : "someplus",
      "edu.toronto.cs.openome_model:SomeMinusContribution" : "someminus",
      "edu.toronto.cs.openome_model:HelpContribution" : "help",
      "edu.toronto.cs.openome_model:HurtContribution" : "hurt",
      "edu.toronto.cs.openome_model:MakeContribution" : "make",
      "edu.toronto.cs.openome_model:BreakContribution" : "break",
      "edu.toronto.cs.openome_model:ConflictContribution" : "conflict",
      "edu.toronto.cs.openome_model:UnknownContribution" : "unknown",
      # Decompositions
      "edu.toronto.cs.openome_model:AndDecomposition" : "and",
      "edu.toronto.cs.openome_model:OrDecomposition" : "or",
      #Dependency
      "edu.toronto.cs.openome_model:Dependency" : "dependency"
    }
    return edge_map.get(key)


  def __hash__(self):
    if not self.id:
      return 0
    return hash(self.id)

  def __eq__(self, other):
    if not self.id or not other.id:
      return False
    return self.id == other.id

  @staticmethod
  def get_contribution_weight(key):
    if   key == "make":
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


class Parser(O):

  def __init__(self, src):
    """
    Initialize Parser with source file
    :param src:
    :param ns: Namespace with source
    :return:
    """
    O.__init__(self)
    self.src = src
    self.ns = None
    self.nodes = None
    self.edges = None

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

  def remove_actors(self):
    from copy import copy

    def remove_actor(actor):
      edge_ids = []
      if actor.from_edges : edge_ids+= actor.from_edges
      if actor.to_edges   : edge_ids+= actor.to_edges
      for edge_id in edge_ids:
        other_end = self.get_node(self.get_other_end(edge_id, actor.id))
        # Remove edges from "from" and "to" of other end
        if other_end:
          if other_end.from_edges and edge_id in other_end.from_edges:
            other_end.from_edges.remove(edge_id)
          if other_end.to_edges and edge_id in other_end.to_edges:
            other_end.to_edges.remove(edge_id)
        self.edges.remove(self.get_edge(edge_id))
      self.nodes.remove(actor)

    clones = copy(self.nodes)
    for node in clones:
      if node.type in ["agent", "role"]:
        remove_actor(node)

  def dump_json(self, file_path = None):
    if file_path:
      fl = open(file_path, 'w')
      fl.write(self.to_json())
      fl.close()
    else:
      print(self.to_json())

  def store_json(self):
    folder_name = "models/" + self.src.split("/")[-1].split(".")[0]
    if not os.path.exists(folder_name):
      os.makedirs(folder_name)
    self.parse()
    self.remove_actors()
    self.dump_json(folder_name + "/model.json")

  def make_dummy_props(self):
    folder_name = "models/" + self.src.split("/")[-1].split(".")[0]
    if not os.path.exists(folder_name):
      os.makedirs(folder_name)
    self.parse()
    goals = {}
    for node in self.nodes:
      goals[node.id] = choice([-1, 1])
    props = {
      "src"   : self.src,
      "goals" : goals
    }
    fl = open(folder_name + "/properties.json", 'w')
    fl.write(json.dumps(props, indent=4, separators=(',', ': ')))
    fl.close()