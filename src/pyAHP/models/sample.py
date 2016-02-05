import os, sys
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from pyAHP.template import *
__author__ = 'panzer'

N = Many()
# Nodes
n1 = N + HardGoal(
  name = "Modernize"
)
n2 = N + HardGoal(
  name = "Incremental Rewrite"
)
n3 = N + HardGoal(
  name = "Big Bang Rewrite"
)
n4 = N + HardGoal(
  name = "Layer Sequence"
)
n5 = N + HardGoal(
  name = "Support"
)
n6 = N + HardGoal(
  name = "Existing Apps"
)
n7 = N + HardGoal(
  name = "Data Service"
)
n8 = N + HardGoal(
  name = "Data Model"
)
n9 = N + HardGoal(
  name = "App Framework"
)
n10 = N + HardGoal(
  name = "Monitor"
)
n11 = N + HardGoal(
  name = "New Database"
)
n12 = N + HardGoal(
  name = "Pnp Framework"
)
n13 = N + HardGoal(
  name = "Documentation"
)
n14 = N + HardGoal(
  name = "Regression Test"
)
n15 = N + HardGoal(
  name = "Number Tiers"
)
n16 = N + HardGoal(
  name = "Data Service(7)"
)
n17 = N + HardGoal(
  name = "Comprehensive Data Model"
)
n18 = N + HardGoal(
  name = "Extensible Data Model"
)
n19 = N + HardGoal(
  name = "Specific Data Model"
)
n20 = N + HardGoal(
  name = "App Framework(6)"
)
n21 = N + HardGoal(
  name = "Monitor(11)"
)
n22 = N + HardGoal(
  name = "ServiceLayer"
)
n23 = N + HardGoal(
  name = "2 Tier"
)
n24 = N + HardGoal(
  name = "3 Tier"
)
n25 = N + HardGoal(
  name = "Tiers w/ Service"
)

E = Many()
#Edges
e1 = E + Or(
  source = n2,
  target = n1
)
e2 = E + Or(
  source = n3,
  target = n1
)
e3 = E + And(
  source = n5,
  target = n2
)
e4 = E + And(
  source = n6,
  target = n2
)
e5 = E + And(
  source = n7,
  target = n2
)
e6 = E + And(
  source = n8,
  target = n2
)
e7 = E + And(
  source = n9,
  target = n2
)
e8 = E + And(
  source = n10,
  target = n2
)
e9 = E + And(
  source = n4,
  target = n3
)
e10 = E + Or(
  source = n11,
  target = n4
)
e11 = E + Or(
  source = n12,
  target = n4
)
e12 = E + And(
  source = n13,
  target = n5
)
e13 = E + And(
  source = n14,
  target = n5
)
e14 = E + And(
  source = n15,
  target = n6
)
e15 = E + And(
  source = n16,
  target = n7
)
e16 = E + Or(
  source = n17,
  target = n8
)
e17 = E + Or(
  source = n18,
  target = n8
)
e18 = E + Or(
  source = n19,
  target = n8
)
e19 = E + And(
  source = n20,
  target = n9
)
e20 = E + And(
  source = n21,
  target = n10
)
e21 = E + Or(
  source = n22,
  target = n15
)
e22 = E + Or(
  source = n23,
  target = n15
)
e23 = E + Or(
  source = n24,
  target = n15
)
e24 = E + And(
  source = n25,
  target = n22
)

tree = Tree(name="sample", nodes=N.all, edges=E.all, root=n1)

if __name__ == "__main__":
  print(len(tree.get_bases()))
  for base in tree.get_bases():
    print(base.name)