import os, sys
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from pystar.template import *
__author__ = 'george'

# Nodes
n1 =Node(
  name = "Provide accurate Information",
  type = softgoal
)
n2 = Node(
  name = "To know what to do",
  type = softgoal
)
n3 = Node(
  name = "Follow instructions from firemen",
  type = task
)
n4 = Node(
  name = "Provide crisis related info",
  type = task
)
n5 = Node(
  name = "Provide to fireman",
  type = task
)
n6 = Node(
  name = "Provide info to police",
  type = task
)
n7 = Node(
  name = "Receive instructions",
  type = hardgoal
)
n8 = Node(
  name = "Crisis-related information(Fire)",
  type = resource
)
n9 = Node(
  name = "Instructions(Fire)",
  type = resource
)
n10 = Node(
  name = "Instructions(Police)",
  type = resource
)
n11 = Node(
  name = "Crisis-related information(Police)",
  type = task
)

#Edges
e1 = Edge(
  value = someplus,
  source = n7,
  target = n2
)
e2 = Edge(
  value = OR,
  source = n7,
  target = n3
)
e3 = Edge(
  value = AND,
  source = n5,
  target = n4
)
e4 = Edge(
  value = AND,
  source = n6,
  target = n4
)
e5 = Edge(
  value = dep,
  source = n5,
  target = n8
)
e6 = Edge(
  value = dep,
  source = n9,
  target = n7
)
e7 = Edge(
  value = dep,
  source = n10,
  target = n7
)
e8 = Edge(
  value = dep,
  source = n6,
  target = n11
)

nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11]
edges = [e1, e2, e3, e4, e5, e6, e7, e8]
graph = Graph(nodes=nodes, edges=edges)