import os, sys
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from pyAHP.template import *
__author__ = 'panzer'

N = Many()
# Nodes
n1 = N + HardGoal(
  name = "Modernize",
  base_cost = 0,
  base_benefit = 0
)
n2 = N + HardGoal(
  name = "Incremental Rewrite",
  base_cost = 0,
  base_benefit = 0
)
n3 = N + HardGoal(
  name = "Big Bang Rewrite",
  base_cost = 0,
  base_benefit = 0
)
n4 = N + HardGoal(
  name = "Layer Sequence",
  base_cost = 0,
  base_benefit = 0
)
n5 = N + HardGoal(
  name = "Support",
  base_cost = 0,
  base_benefit = 0
)
n6 = N + HardGoal(
  name = "Existing Apps",
  base_cost = 0,
  base_benefit = 0
)
n7 = N + HardGoal(
  name = "Data Service",
  base_cost = 0,
  base_benefit = 0
)
n8 = N + HardGoal(
  name = "Data Model",
  base_cost = 0,
  base_benefit = 0
)
n9 = N + HardGoal(
  name = "App Framework",
  base_cost = 0,
  base_benefit = 0
)
n10 = N + HardGoal(
  name = "Monitor",
  base_cost = 0,
  base_benefit = 0
)
n11 = N + HardGoal(
  name = "New Database",
  base_cost = 6,
  base_benefit = 5
)
n12 = N + HardGoal(
  name = "Pnp Framework",
  base_cost = 5,
  base_benefit = 5
)
n13 = N + HardGoal(
  name = "Documentation",
  base_cost = 3,
  base_benefit = 5
)
n14 = N + HardGoal(
  name = "Regression Test",
  base_cost = 3,
  base_benefit = 5
)
n15 = N + HardGoal(
  name = "Number Tiers",
  base_cost = 0,
  base_benefit = 0
)
n16 = N + HardGoal(
  name = "Data Service(7)",
  base_cost = 3,
  base_benefit = 5
)
n17 = N + HardGoal(
  name = "Comprehensive Data Model",
  base_cost = 0,
  base_benefit = 0
)
n18 = N + HardGoal(
  name = "Extensible Data Model(16/19)",
  base_cost = 0,
  base_benefit = 0
)
n19 = N + HardGoal(
  name = "Specific Data Model",
  base_cost = 0,
  base_benefit = 0
)
n20 = N + HardGoal(
  name = "App Framework(6)",
  base_cost = 5,
  base_benefit = 5
)
n21 = N + HardGoal(
  name = "Monitor(11)",
  base_cost = 1,
  base_benefit = 5
)
n22 = N + HardGoal(
  name = "ServiceLayer",
  base_cost = 0,
  base_benefit = 0
)
n23 = N + HardGoal(
  name = "2 Tier",
  base_cost = 5,
  base_benefit = 5
)
n24 = N + HardGoal(
  name = "3 Tier",
  base_cost = 5,
  base_benefit = 5
)
n25 = N + HardGoal(
  name = "Tiers w/ Service",
  base_cost = 0,
  base_benefit = 0
)
n26 = N + Task(
  name = "Choose Doc Tool",
  base_cost = 0,
  base_benefit = 0
)
n27 = N + Task(
  name = "J2EE Specification",
  base_cost = 0,
  base_benefit = 0
)
n28 = N + Task(
  name = "Access Control Assessed",
  base_cost = 0,
  base_benefit = 0
)
n29 = N + Task(
  name = "Access Control Pilot",
  base_cost = 0,
  base_benefit = 0
)
n30 = N + Task(
  name = "Monitoring Pilot",
  base_cost = 0,
  base_benefit = 0
)
n31 = N + Resource(
  name = "Documentation Tool",
  base_cost = 0,
  base_benefit = 0
)
n32 = N + Task(
  name = "Create Test Environment",
  base_cost = 0,
  base_benefit = 0
)
n33 = N + Task(
  name = "Choose Candidate System",
  base_cost = 0,
  base_benefit = 0
)
n34 = N + Task(
  name = "Data Service Spec",
  base_cost = 0,
  base_benefit = 0
)
n35 = N + Task(
  name = "Data Service Pilot",
  base_cost = 0,
  base_benefit = 0
)
n36 = N + HardGoal(
  name = "Svc layer w/ extracted biz logic in DB(12)",
  base_cost = 3,
  base_benefit = 5
)
n37 = N + HardGoal(
  name = "Svc layer w/ extracted biz logic(13)",
  base_cost = 5,
  base_benefit = 3
)
n38 = N + Task(
  name = "DB Vendor Test Env",
  base_cost = 0,
  base_benefit = 0
)
n39 = N + Task(
  name = "General Test Env",
  base_cost = 0,
  base_benefit = 0
)
n40 = N + Task(
  name = "Bakeoff Result",
  base_cost = 0,
  base_benefit = 0
)
n41 = N + HardGoal(
  name = "Provide logical data scheme internally(8)",
  base_cost = 3,
  base_benefit = 3
)
n42 = N + HardGoal(
  name = "Define data model for all shared data(15)",
  base_cost = 3,
  base_benefit = 3
)
n43 = N + HardGoal(
  name = "Define ext mandatory data std(18)",
  base_cost = 3,
  base_benefit = 5
)
n44 = N + HardGoal(
  name = "External clients get exactly what they request(10)",
  base_cost = 4,
  base_benefit = 3
)
n45 = N + HardGoal(
  name = "XXX coordinates and internal client does whatever(17)",
  base_cost = 3,
  base_benefit = 3
)
n46 = N + HardGoal(
  name = "XXX coordinates and external client does whatever(20)",
  base_cost = 5,
  base_benefit = 3
)
n47 = N + HardGoal(
  name = "Build internal extensible data model(16)",
  base_cost = 2,
  base_benefit = 3
)
n48 = N + HardGoal(
  name = "External data model can be extended(19)",
  base_cost = 4,
  base_benefit = 5
)
n49 = N + Task(
  name = "Data Model Pilot",
  base_cost = 0,
  base_benefit = 0
)
n50 = N + SoftGoal(
  name = "Quick Feature Delivery",
  base_cost = 0,
  base_benefit = 0
)
n51 = N + SoftGoal(
  name = "Good Example of Agile Government development",
  base_cost = 0,
  base_benefit = 0
)
n52 = N + SoftGoal(
  name = "Easily Share Data W/ Partners",
  base_cost = 0,
  base_benefit = 0
)
n53 = N + SoftGoal(
  name = "Easily Share Data Internally",
  base_cost = 0,
  base_benefit = 0
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
  source = n33,
  target = n6
)
e16 = E + And(
  source = n16,
  target = n7
)
e17 = E + Or(
  source = n17,
  target = n8
)
e18 = E + Or(
  source = n18,
  target = n8
)
e19 = E + Or(
  source = n19,
  target = n8
)
e20 = E + And(
  source = n20,
  target = n9
)
e21 = E + And(
  source = n21,
  target = n10
)
e22 = E + And(
  source = n26,
  target = n13
)
e23 = E + And(
  source = n32,
  target = n14
)
e24 = E + Or(
  source = n22,
  target = n15
)
e25 = E + Or(
  source = n23,
  target = n15
)
e26 = E + Or(
  source = n24,
  target = n15
)
e27 = E + Or(
  source = n34,
  target = n16
)
e28 = E + Or(
  source = n35,
  target = n16
)
e29 = E + And(
  source = n41,
  target = n17
)
e30 = E + And(
  source = n42,
  target = n17
)
e31 = E + And(
  source = n43,
  target = n17
)
e32 = E + And(
  source = n47,
  target = n18
)
e33 = E + And(
  source = n48,
  target = n18
)
e34 = E + And(
  source = n44,
  target = n19
)
e35 = E + And(
  source = n45,
  target = n19
)
e36 = E + And(
  source = n46,
  target = n19
)
e37 = E + And(
  source = n27,
  target = n20
)
e38 = E + And(
  source = n28,
  target = n21
)
e39 = E + And(
  source = n29,
  target = n21
)
e40 = E + And(
  source = n30,
  target = n21
)
e41 = E + And(
  source = n25,
  target = n22
)
e42 = E + Or(
  source = n36,
  target = n25
)
e43 = E + Or(
  source = n37,
  target = n25
)
e44 = E + And(
  source = n31,
  target = n26
)
e45 = E + And(
  source = n38,
  target = n32
)
e46 = E + And(
  source = n39,
  target = n32
)
e47 = E + And(
  source = n40,
  target = n33
)
e48 = E + And(
  source = n49,
  target = n47
)
e49 = E + And(
  source = n5,
  target = n50
)
e50 = E + And(
  source = n9,
  target = n50
)
e51 = E + And(
  source = n50,
  target = n51
)
e52 = E + And(
  source = n52,
  target = n51
)
e53 = E + And(
  source = n7,
  target = n52
)
e54 = E + And(
  source = n8,
  target = n52
)
e55 = E + And(
  source = n6,
  target = n53
)
e56 = E + And(
  source = n7,
  target = n53
)
e57 = E + And(
  source = n8,
  target = n53
)

tree = Tree(name="sample", nodes=N.all, edges=E.all, root=n1)

if __name__ == "__main__":
  print(len(tree.get_bases()))
  # for base in tree.get_bases():
  #   print(base.name)
  print(n43.base_cost)
  print(n43.base_benefit)