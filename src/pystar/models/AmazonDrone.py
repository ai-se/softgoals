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
  "Quick delivery achieved",
  "Shopper"
)

n2 = N + SoftGoal(
  "Safety",
  "Shopper"
)

n3 = N + HardGoal(
  "Service be signed up for",
  "Shopper"
)

n4 = N + HardGoal(
  "Buy Product",
  "Shopper"
)

n5 = N + HardGoal(
  "Package unlocked",
  "Shopper"
)

n6 = N + Task(
  "Use drone service",
  "Shopper"
)

n7 = N + Task(
  "Traditional delivery",
  "Shopper"
)

n8 = N + Task(
  "Make prime air order",
  "Shopper"
)

n9 = N + Task(
  "Go to location",
  "Shopper"
)

n10 = N + Task(
  "Collect package",
  "Shopper"
)

n11 = N + Task(
  "Select Date TIme Loc",
  "Shopper"
)

n12 = N + Resource(
  "Order Code",
  "Shopper"
)

# Edges
e1 = E + Make(
  source=n6,
  target=n1
)

e2 = E + Hurt(
  source=n7,
  target=n1
)

e3 = E + Hurt(
  source=n6,
  target=n2
)

e4 = E + Or(
  source=n6,
  target=n4
)

e5 = E + Or(
  source=n7,
  target=n4
)

e6 = E + And(
  source=n3,
  target=n6
)

e7 = E + And(
  source=n8,
  target=n6
)

e8 = E + And(
  source=n9,
  target=n6
)

e9 = E + And(
  source=n10,
  target=n6
)

e10 = E + And(
  source=n11,
  target=n8
)

e11 = E + And(
  source=n12,
  target=n10
)

e12 = E + And(
  source=n5,
  target=n10
)

graph = Graph(name="AmazonDrone", nodes=N.all, edges=E.all)

if __name__ == "__main__":
  from pystar.model import Model
  from utilities.de import DE
  from star1.star1 import run
  run(graph, "miniature")