from __future__ import print_function, division
import os, sys
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from pystar.template import *
__author__ = 'panzer'

N = Many()
E = Many()


# Nodes
n1 = N + SoftGoal(
  "Enhance local area",
  "Garden Bridge Trust"
)

n2 = N + SoftGoal(
  "Tourism",
  "Garden Bridge Trust"
)

n3 = N + SoftGoal(
  "Educate",
  "Garden Bridge Trust"
)

n4 = N + SoftGoal(
  "Promote Green London",
  "Garden Bridge Trust"
)

n5 = N + SoftGoal(
  "Encourage walking",
  "Garden Bridge Trust"
)

n6 = N + SoftGoal(
  "Showcase British Design",
  "Garden Bridge Trust"
)

n7 = N + Task(
  "Build Structure",
  "Garden Bridge Trust"
)

n8 = N + Task(
  "Plant Flora",
  "Garden Bridge Trust"
)

n9 = N + Task(
  "Build Garden Bridge",
  "Garden Bridge Trust"
)

n10 = N + SoftGoal(
  "Faster Commute",
  "Garden Bridge User"
)

n11 = N + SoftGoal(
  "More Pleasant Commute",
  "Garden Bridge User"
)

n12 = N + SoftGoal(
  "Good Health",
  "Garden Bridge User"
)

n13 = N + SoftGoal(
  "Enjoy Greenspace",
  "Garden Bridge User"
)

n14 = N + Task(
  "Commute",
  "Garden Bridge User"
)

n15 = N + Task(
  "Visit Park",
  "Garden Bridge User"
)

n16 = N + HardGoal(
  "Make us of Bridge",
  "Garden Bridge User"
)

#Edges
e1 = E + Help(
  source=n8,
  target=n4
)

e2 = E + Help(
  source=n9,
  target=n5
)

e3 = E + Help(
  source=n9,
  target=n6
)

e4 = E + And(
  source=n7,
  target=n9
)

e5 = E + And(
  source=n8,
  target=n9
)

e6 = E + Hurt(
  source=n14,
  target=n10
)

e7 = E + Help(
  source=n14,
  target=n11
)

e8 = E + Help(
  source=n13,
  target=n12
)

e9 = E + Help(
  source=n15,
  target=n13
)

e10 = E + Or(
  source=n14,
  target=n16
)

e11 = E + Or(
  source=n15,
  target=n16
)

graph = Graph(name="GardenBridge", nodes=N.all, edges=E.all)

if __name__ == "__main__":
  from pystar.model import Model
  from utilities.de import DE
  from star1.star1 import run
  run(graph, "miniature")
