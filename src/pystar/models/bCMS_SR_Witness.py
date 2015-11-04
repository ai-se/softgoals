import os, sys
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from pystar.template import *
__author__ = 'george'

# Nodes
n1 =SoftGoal(
  name = "Provide accurate Information",
)
n2 = SoftGoal(
  name = "To know what to do",
)
n3 = Task(
  name = "Follow instructions from firemen",
)
n4 = Task(
  name = "Provide crisis related info",
)
n5 = Task(
  name = "Provide to fireman",
)
n6 = Task(
  name = "Provide info to police",
)
n7 = HardGoal(
  name = "Receive instructions",
)
n8 = Resource(
  name = "Crisis-related information(Fire)",
)
n9 = Resource(
  name = "Instructions(Fire)",
)
n10 = Resource(
  name = "Instructions(Police)",
)
n11 = Task(
  name = "Crisis-related information(Police)",
)

#Edges
e1 = SomePlus(
  source = n7,
  target = n2
)
e2 = Or(
  source = n7,
  target = n3
)
e3 = And(
  source = n5,
  target = n4
)
e4 = And(
  source = n6,
  target = n4
)
e5 = Dep(
  source = n5,
  target = n8
)
e6 = Dep(
  source = n9,
  target = n7
)
e7 = Dep(
  source = n10,
  target = n7
)
e8 = Dep(
  source = n6,
  target = n11
)

nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11]
edges = [e1, e2, e3, e4, e5, e6, e7, e8]
graph = Graph(name="bCMS_SR_Witness", nodes=nodes, edges=edges)