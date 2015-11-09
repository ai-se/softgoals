import os, sys
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from pystar.template import *
__author__ = 'george'

N = Many()
# Nodes
n1 = N + SoftGoal(
  "Provide accurate Information about the crisis to police and firemen",
  "Witnesses"
)
n2 = N + SoftGoal(
  "To know what to do at different stages in the crisis",
  "Witnesses"
)
n3 = N + Task(
  "Follow instructions from firemen and police",
  "Witnesses"
)
n4 = N + Task(
  "Provide crisis related information",
  "Witnesses"
)
n5 = N + Task(
  "Provide to fireman",
  "Witnesses"
)
n6 = N + Task(
  "Provide information to police",
  "Witnesses"
)
n7 = N + HardGoal(
  "Receive instructions",
  "Witnesses"
)
n8 = N + Resource(
  "Crisis-related information(Fire)",
  "Fire Personnel"
)
n9 = N + Resource(
  "Instructions",
  "Fire Personnel"
)
n10 = N + Resource(
  "Instructions(Police)",
  "Police Officer(Policeman)"
)
n11 = N + Task(
  "Crisis-related information",
  "Police Officer(Policeman)"
)

E = Many()
#Edges
e1 = E + SomePlus(
  source = n7,
  target = n2
)
e2 = E + Or(
  source = n7,
  target = n3
)
e3 = E + And(
  source = n5,
  target = n4
)
e4 = E + And(
  source = n6,
  target = n4
)
e5 = E + Dep(
  source = n5,
  target = n8
)
e6 = E + Dep(
  source = n9,
  target = n7
)
e7 = E + Dep(
  source = n10,
  target = n7
)
e8 = E + Dep(
  source = n6,
  target = n11
)


graph = Graph(name="bCMS_SR_Witness", nodes=N.all, edges=E.all)