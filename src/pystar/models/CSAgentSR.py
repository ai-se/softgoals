import os, sys
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from pystar.template import *
__author__ = 'george'

nodes = []

n1 = n = Node(
  name = "CS Be Not for Profit",
  type = hardgoal,
  container = "IT Department"
);nodes.append(n)

n2 = n = Node(
  name = "Properly and Suitably equipped in IT",
  type = softgoal,
  container = "IT Department"
);nodes.append(n)

n3 = n = Node(
  name = "Increase IT Resources",
  type = softgoal,
  container = "IT Department"
);nodes.append(n)

n4 = n = Node(
  name = "IT Resources",
  type = resource,
  container = "IT Department"
);nodes.append(n)

n5 = n = Node(
  name = "Web Services Self Serve",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n6 = n = Node(
  name = "Encourage Kids Using Web Services to Use Phone Services",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n7 = n = Node(
  name = "Maintain Services above Competition",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n8 = n = Node(
  name = "Empowering Kids to Help Themselves",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n9 = n = Node(
  name = "Increase Development of Public Education Program",
  type = softgoal,
  container = "Public Education Program"
);nodes.append(n)

n10 = n = Node(
  name = "Measure Success of Services",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n11 = n = Node(
  name = "Services Be Bilingual",
  type = hardgoal,
  container = "CS Services"
);nodes.append(n)

n12 = n = Node(
  name = "Reduce Contagion Effect [Of Harmful Actions]",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n13 = n = Node(
  name = "Success Be Tracked in Community Resources",
  type = hardgoal,
  container = "Community Resource"
);nodes.append(n)

n14 = n = Node(
  name = "Avoid Presence of Pedofiles",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n15 = n = Node(
  name = "Increase Resources [Services]",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n16 = n = Node(
  name = "*High Quality Services",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n17 = n = Node(
  name = "Improve Image to Kids",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n18 = n = Node(
  name = "Maintain/Implement CS Services",
  type = task,
  container = "CS Services"
);nodes.append(n)

n19 = n = Node(
  name = "Maintain Web Services",
  type = task,
  container = "CS Services"
);nodes.append(n)

n20 = n = Node(
  name = "*Maintain Phone Services",
  type = task,
  container = "CS Services"
);nodes.append(n)

n21 = n = Node(
  name = "Maintain/ Implement PHL Services",
  type = task,
  container = "CS Services"
);nodes.append(n)

n22 = n = Node(
  name = "*Increase Number of Services",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n23 = n = Node(
  name = "Efficient Services",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n24 = n = Node(
  name = "Available [Services]",
  type = softgoal,
  container = "CS Services"
);nodes.append(n)

n25 = n = Node(
  name = "Service Resources",
  type = resource,
  container = "CS Services"
);nodes.append(n)

n26 = n = Node(
  name = "Regional Office Resources",
  type = resource,
  container = "Regional Offices"
);nodes.append(n)

n27 = n = Node(
  name = "Improve Image to Kids",
  type = softgoal,
  container = "SA Program"
);nodes.append(n)

n28 = n = Node(
  name = "Increased SA Resources",
  type = softgoal,
  container = "SA Program"
);nodes.append(n)

n29 = n = Node(
  name = "Trust [of Kids]",
  type = softgoal,
  container = "SA Program"
);nodes.append(n)

n30 = n = Node(
  name = "Quality SA Services",
  type = softgoal,
  container = "SA Program"
);nodes.append(n)

n31 = n = Node(
  name = "Reduce Misconceptions",
  type = softgoal,
  container = "SA Program"
);nodes.append(n)

n32 = n = Node(
  name = "Improve Image to Kids",
  type = softgoal,
  container = "Marketing"
);nodes.append(n)

n33 = n = Node(
  name = "Counselling Resources",
  type = resource,
  container = "Counselling Management"
);nodes.append(n)

n34 = n = Node(
  name = "Positive Internal Opinion",
  type = softgoal,
  container = "Counselling Management"
);nodes.append(n)

n35 = n = Node(
  name = "Increase Counselling Resource",
  type = softgoal,
  container = "Counselling Management"
);nodes.append(n)

n36 = n = Node(
  name = "Increase Funding for Training",
  type = softgoal,
  container = "Counselling Management"
);nodes.append(n)

n37 = n = Node(
  name = "Reduce Cost of Counselling HR",
  type = softgoal,
  container = "Counselling Management"
);nodes.append(n)

n38 = n = Node(
  name = "Accountability of services",
  type = softgoal,
  container = "Counselling Management"
);nodes.append(n)

n39 = n = Node(
  name = "*Help as many kids as possible",
  type = softgoal,
  container = "Counselling Management"
);nodes.append(n)

n40 = n = Node(
  name = "Research on kids be required",
  type = hardgoal,
  container = "Research Partners"
);nodes.append(n)

n41 = n = Node(
  name = "*High Quality Counselling",
  type = softgoal,
  container = "Counselling"
);nodes.append(n)

n42 = n = Node(
  name = "Help Kids",
  type = softgoal,
  container = "Counselling"
);nodes.append(n)

n43 = n = Node(
  name = "Avoid Liability Problems",
  type = softgoal,
  container = "Counselling"
);nodes.append(n)

n44 = n = Node(
  name = "Reduce Contagion Effect [Of Harmful Actions]",
  type = softgoal,
  container = "Counselling"
);nodes.append(n)

n45 = n = Node(
  name = "Responsible Usage [Sponsor Funds]",
  type = softgoal,
  container = "Counselling"
);nodes.append(n)

n46 = n = Node(
  name = "Funds",
  type = resource,
  container = "Fund Development"
);nodes.append(n)

n47 = n = Node(
  name = "Counsellor Experience",
  type = resource,
  container = "Counselling"
);nodes.append(n)

n48 = n = Node(
  name = "Caller Statistics",
  type = resource,
  container = "Counselling"
);nodes.append(n)

n49 = n = Node(
  name = "Accountability of services",
  type = softgoal,
  container = "Individual donor"
);nodes.append(n)

n50 = n = Node(
  name = "Demonstrable services",
  type = softgoal,
  container = "Corporate Sponsors"
);nodes.append(n)

n51 = n = Node(
  name = "Increase Volunteers",
  type = softgoal,
  container = "Fund Development"
);nodes.append(n)

n52 = n = Node(
  name = "Increase [Awareness]",
  type = softgoal,
  container = "Marketing"
);nodes.append(n)

n53 = n = Node(
  name = "Avoid Over-Marketing Services",
  type = softgoal,
  container = "Marketing"
);nodes.append(n)

n54 = n = Node(
  name = "Positive[Reputation of CS]",
  type = softgoal,
  container = "Marketing"
);nodes.append(n)

n55 = n = Node(
  name = "Match Fundraising Targets",
  type = softgoal,
  container = "Marketing"
);nodes.append(n)

n56 = n = Node(
  name = "Follow Highest Ethical Guidelines",
  type = softgoal,
  container = "Corporate Sponsors"
);nodes.append(n)

n57 = n = Node(
  name = "Credibility [CS Brand]",
  type = softgoal,
  container = "Corporate Sponsors"
);nodes.append(n)

n58 = n = Node(
  name = "Long Term Funding",
  type = softgoal,
  container = "Fund Development"
);nodes.append(n)

n59 = n = Node(
  name = "Information",
  type = resource,
  container = "General Public"
);nodes.append(n)

n60 = n = Node(
  name = "Services Be Free",
  type = hardgoal,
  container = "Parents, Kids & Youth"
);nodes.append(n)

n61 = n = Node(
  name = "Collaborate with Not for Profit Partners on Services",
  type = hardgoal,
  container = "Not For Profit Partners"
);nodes.append(n)

n62 = n = Node(
  name = "Involve CS in Events",
  type = hardgoal,
  container = "Not For Profit Partners"
);nodes.append(n)

#### INNERS
# TODO
n63 = n = Node(
  name = "CS Be Not for Profit",
  type = hardgoal,
  container = "CS"
);nodes.append(n)

n64 = n = Node(
  name = "Properly and Suitably equipped in IT",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n65 = n = Node(
  name = "Increase IT Resources",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n66 = n = Node(
  name = "Web Services Self Serve",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n67 = n = Node(
  name = "Encourage Kids Using Web Services to Use Phone Services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n68 = n = Node(
  name = "Maintain Services above Competition",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n69 = n = Node(
  name = "Empowering Kids to Help Themselves",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n70 = n = Node(
  name = "Increase Development of Public Education Program",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n71 = n = Node(
  name = "Measure Success of Services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n72 = n = Node(
  name = "Services Be Bilingual",
  type = hardgoal,
  container = "CS"
);nodes.append(n)

n73 = n = Node(
  name = "Reduce Contagion Effect [Of Harmful Actions]",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n74 = n = Node(
  name = "Success Be Tracked in Community Resources",
  type = hardgoal,
  container = "CS"
);nodes.append(n)

n75 = n = Node(
  name = "Avoid Presence of Pedofiles",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n76 = n = Node(
  name = "Increase Resources [Services]",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n77 = n = Node(
  name = "*High Quality Services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n78 = n = Node(
  name = "Improve Image to Kids",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n79 = n = Node(
  name = "Maintain/Implement CS Services",
  type = task,
  container = "CS"
);nodes.append(n)

n80 = n = Node(
  name = "Maintain Web Services",
  type = task,
  container = "CS"
);nodes.append(n)

n81 = n = Node(
  name = "*Maintain Phone Services",
  type = task,
  container = "CS"
);nodes.append(n)

n82 = n = Node(
  name = "Maintain/ Implement PHL Services",
  type = task,
  container = "CS"
);nodes.append(n)

n83 = n = Node(
  name = "*Increase Number of Services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n84 = n = Node(
  name = "Efficient Services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n85 = n = Node(
  name = "Available [Services]",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n86 = n = Node(
  name = "Acquire Funds",
  type = task,
  container = "CS"
);nodes.append(n)

n87 = n = Node(
  name = "Increased SA Resources",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n88 = n = Node(
  name = "Trust [of Kids]",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n89 = n = Node(
  name = "Quality SA Services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n90 = n = Node(
  name = "Reduce Misconceptions",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n91 = n = Node(
  name = "Sufficient Counselling Resource",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n92 = n = Node(
  name = "Increase Funding for Training",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n93 = n = Node(
  name = "Reduce Cost of Counselling HR",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n94 = n = Node(
  name = "Accountability of services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n95 = n = Node(
  name = "Research on Kids Be Acquired",
  type = hardgoal,
  container = "CS"
);nodes.append(n)

n96 = n = Node(
  name = "*High Quality Counselling",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n97 = n = Node(
  name = "Avoid Liability Problems",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n98 = n = Node(
  name = "Responsible Usage[Sponsor Funds]",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n99 = n = Node(
  name = "Demonstrable Services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n100 = n = Node(
  name = "Increase Volunteers",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n101 = n = Node(
  name = "Increase [Awareness]",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n102 = n = Node(
  name = "Avoid Over-Marketing Services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n103 = n = Node(
  name = "Positive [Reputation of CS]",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n104 = n = Node(
  name = "Match Fundraising Targets",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n105 = n = Node(
  name = "Follow Highest Ethical Guidelines",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n106 = n = Node(
  name = "Credibility [CS Brand]",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n107 = n = Node(
  name = "Long Term Funding",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n108 = n = Node(
  name = "Provide Information to General Public",
  type = task,
  container = "CS"
);nodes.append(n)

n109 = n = Node(
  name = "Services Be Free",
  type = hardgoal,
  container = "Parents, Kids & Youth"
);nodes.append(n)

n110 = n = Node(
  name = "Collaborate with Not for Profit Partners on Services",
  type = hardgoal,
  container = "CS"
);nodes.append(n)

n111 = n = Node(
  name = "Be Involved in Not for Profit Partners Events",
  type = hardgoal,
  container = "CS"
);nodes.append(n)

n112 = n = Node(
  name = "Help Kids",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n113 = n = Node(
  name = "Help Parents",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n114 = n = Node(
  name = "*Help As Many Kids as Possible",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n115 = n = Node(
  name = "Ability to Move Forward",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n116 = n = Node(
  name = "Sustainable Services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n117 = n = Node(
  name = "Externally Unique[Services]",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n118 = n = Node(
  name = "Avoid Scandal",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n119 = n = Node(
  name = "Positive Internal Opinion",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n120 = n = Node(
  name = "Increase Funds",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n121 = n = Node(
  name = "Avoid Travel Spending",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n122 = n = Node(
  name = "Avoid Entertainment Spending",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n123 = n = Node(
  name = "Accessibility of Services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n124 = n = Node(
  name = "Reduce Cost",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n125 = n = Node(
  name = "Safety Kids",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n126 = n = Node(
  name = "Increase Call/Web Volumes",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n127 = n = Node(
  name = "Find Needs and Wants of Kids",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n128 = n = Node(
  name = "Provide Resources",
  type = task,
  container = "CS"
);nodes.append(n)

n129 = n = Node(
  name = "Avoid Internal Duplication of Services",
  type = softgoal,
  container = "CS"
);nodes.append(n)

n130 = n = Node(
  name = "Provide IT Resources",
  type = task,
  container = "CS"
);nodes.append(n)

n131 = n = Node(
  name = "Provide Service Resources",
  type = task,
  container = "CS"
);nodes.append(n)

n132 = n = Node(
  name = "Provide Resources to Regional Offices",
  type = task,
  container = "CS"
);nodes.append(n)

n133 = n = Node(
  name = "Provide Counselling Resources",
  type = task,
  container = "CS"
);nodes.append(n)

n134 = n = Node(
  name = "Service is National",
  type = softgoal,
  container = "CS"
);nodes.append(n)


# EDGES
edges = []

e1 = e = Edge(
  value = dep,
  source = n63,
  target = n1
); edges.append(e)

e2 = e = Edge(
  value = dep,
  source = n65,
  target = n3
); edges.append(e)

e3 = e = Edge(
  value = dep,
  source = n130,
  target = n4
); edges.append(e)

e4 = e = Edge(
  value = dep,
  source = n70,
  target = n9
); edges.append(e)

e5 = e = Edge(
  value = dep,
  source = n76,
  target = n15
); edges.append(e)

e6 = e = Edge(
  value = dep,
  source = n131,
  target = n25
); edges.append(e)

e7 = e = Edge(
  value = dep,
  source = n132,
  target = n26
); edges.append(e)

e8 = e = Edge(
  value = dep,
  source = n91,
  target = n35
); edges.append(e)

e9 = e = Edge(
  value = dep,
  source = n92,
  target = n36
); edges.append(e)

e10 = e = Edge(
  value = dep,
  source = n133,
  target = n33
); edges.append(e)

e11 = e = Edge(
  value = dep,
  source = n73,
  target = n44
); edges.append(e)

e12 = e = Edge(
  value = dep,
  source = n98,
  target = n45
); edges.append(e)

e13 = e = Edge(
  value = dep,
  source = n99,
  target = n50
); edges.append(e)

e14 = e = Edge(
  value = dep,
  source = n100,
  target = n51
); edges.append(e)

e15 = e = Edge(
  value = dep,
  source = n94,
  target = n49
); edges.append(e)

e16 = e = Edge(
  value = dep,
  source = n103,
  target = n54
); edges.append(e)

e17 = e = Edge(
  value = dep,
  source = n105,
  target = n56
); edges.append(e)

e18 = e = Edge(
  value = dep,
  source = n106,
  target = n57
); edges.append(e)

e19 = e = Edge(
  value = dep,
  source = n108,
  target = n59
); edges.append(e)

e20 = e = Edge(
  value = dep,
  source = n109,
  target = n60
); edges.append(e)

e21 = e = Edge(
  value = dep,
  source = n111,
  target = n62
); edges.append(e)

e22 = e = Edge(
  value = dep,
  source = n2,
  target = n64
); edges.append(e)

e23 = e = Edge(
  value = dep,
  source = n5,
  target = n66
); edges.append(e)

e24 = e = Edge(
  value = dep,
  source = n6,
  target = n67
); edges.append(e)

e25 = e = Edge(
  value = dep,
  source = n7,
  target = n68
); edges.append(e)

e26 = e = Edge(
  value = help,
  source = n64,
  target = n68
); edges.append(e)

e27 = e = Edge(
  value = help,
  source = n117,
  target = n68
); edges.append(e)

e28 = e = Edge(
  value = dep,
  source = n8,
  target = n69
); edges.append(e)

e29 = e = Edge(
  value = help,
  source = n127,
  target = n69
); edges.append(e)

e30 = e = Edge(
  value = help,
  source = n79,
  target = n69
); edges.append(e)

e31 = e = Edge(
  value = help,
  source = n80,
  target = n69
); edges.append(e)

e32 = e = Edge(
  value = dep,
  source = n10,
  target = n71
); edges.append(e)

e33 = e = Edge(
  value = help,
  source = n74,
  target = n71
); edges.append(e)

e34 = e = Edge(
  value = dep,
  source = n11,
  target = n72
); edges.append(e)

e35 = e = Edge(
  value = dep,
  source = n12,
  target = n73
); edges.append(e)

e36 = e = Edge(
  value = dep,
  source = n13,
  target = n74
); edges.append(e)

e37 = e = Edge(
  value = dep,
  source = n14,
  target = n75
); edges.append(e)

e38 = e = Edge(
  value = dep,
  source = n16,
  target = n77
); edges.append(e)

e39 = e = Edge(
  value = help,
  source = n127,
  target = n77
); edges.append(e)

e40 = e = Edge(
  value = dep,
  source = n17,
  target = n78
); edges.append(e)

e41 = e = Edge(
  value = help,
  source = n77,
  target = n78
); edges.append(e)

e42 = e = Edge(
  value = help,
  source = n117,
  target = n78
); edges.append(e)

e43 = e = Edge(
  value = help,
  source = n96,
  target = n78
); edges.append(e)

e44 = e = Edge(
  value = help,
  source = n90,
  target = n78
); edges.append(e)

e45 = e = Edge(
  value = dep,
  source = n18,
  target = n79
); edges.append(e)

e46 = e = Edge(
  value = dep,
  source = n19,
  target = n80
); edges.append(e)

e47 = e = Edge(
  value = dep,
  source = n20,
  target = n81
); edges.append(e)

e48 = e = Edge(
  value = dep,
  source = n21,
  target = n82
); edges.append(e)

e49 = e = Edge(
  value = dep,
  source = n22,
  target = n83
); edges.append(e)

e50 = e = Edge(
  value = dep,
  source = n23,
  target = n84
); edges.append(e)

e51 = e = Edge(
  value = dep,
  source = n24,
  target = n85
); edges.append(e)

e52 = e = Edge(
  value = dep,
  source = n28,
  target = n87
); edges.append(e)

e53 = e = Edge(
  value = dep,
  source = n29,
  target = n88
); edges.append(e)

e54 = e = Edge(
  value = dep,
  source = n30,
  target = n89
); edges.append(e)

e55 = e = Edge(
  value = dep,
  source = n31,
  target = n90
); edges.append(e)

e56 = e = Edge(
  value = hurt,
  source = n126,
  target = n91
); edges.append(e)

e57 = e = Edge(
  value = help,
  source = n120,
  target = n91
); edges.append(e)

e58 = e = Edge(
  value = dep,
  source = n37,
  target = n93
); edges.append(e)

e59 = e = Edge(
  value = dep,
  source = n38,
  target = n94
); edges.append(e)

e60 = e = Edge(
  value = dep,
  source = n40,
  target = n95
); edges.append(e)

e61 = e = Edge(
  value = dep,
  source = n41,
  target = n96
); edges.append(e)

e62 = e = Edge(
  value = dep,
  source = n43,
  target = n97
); edges.append(e)

e63 = e = Edge(
  value = help,
  source = n121,
  target = n98
); edges.append(e)

e64 = e = Edge(
  value = help,
  source = n122,
  target = n98
); edges.append(e)

e65 = e = Edge(
  value = help,
  source = n71,
  target = n99
); edges.append(e)

e66 = e = Edge(
  value = help,
  source = n126,
  target = n99
); edges.append(e)

e67 = e = Edge(
  value = help,
  source = n80,
  target = n99
); edges.append(e)

e68 = e = Edge(
  value = help,
  source = n118,
  target = n100
); edges.append(e)

e69 = e = Edge(
  value = help,
  source = n70,
  target = n100
); edges.append(e)

e70 = e = Edge(
  value = help,
  source = n106,
  target = n100
); edges.append(e)

e71 = e = Edge(
  value = help,
  source = n103,
  target = n100
); edges.append(e)

e72 = e = Edge(
  value = help,
  source = n108,
  target = n101
); edges.append(e)

e73 = e = Edge(
  value = help,
  source = n111,
  target = n101
); edges.append(e)

e74 = e = Edge(
  value = dep,
  source = n54,
  target = n102
); edges.append(e)

e75 = e = Edge(
  value = help,
  source = n96,
  target = n103
); edges.append(e)

e76 = e = Edge(
  value = help,
  source = n95,
  target = n103
); edges.append(e)

e77 = e = Edge(
  value = help,
  source = n94,
  target = n103
); edges.append(e)

e78 = e = Edge(
  value = help,
  source = n118,
  target = n103
); edges.append(e)

e79 = e = Edge(
  value = help,
  source = n105,
  target = n103
); edges.append(e)

e80 = e = Edge(
  value = help,
  source = n107,
  target = n103
); edges.append(e)

e81 = e = Edge(
  value = help,
  source = n71,
  target = n103
); edges.append(e)

e82 = e = Edge(
  value = help,
  source = n123,
  target = n103
); edges.append(e)

e83 = e = Edge(
  value = dep,
  source = n55,
  target = n104
); edges.append(e)

e84 = e = Edge(
  value = help,
  source = n63,
  target = n105
); edges.append(e)

e85 = e = Edge(
  value = help,
  source = n105,
  target = n106
); edges.append(e)

e86 = e = Edge(
  value = help,
  source = n103,
  target = n106
); edges.append(e)

e87 = e = Edge(
  value = help,
  source = n118,
  target = n106
); edges.append(e)

e88 = e = Edge(
  value = help,
  source = n107,
  target = n106
); edges.append(e)

e89 = e = Edge(
  value = help,
  source = n108,
  target = n106
); edges.append(e)

e90 = e = Edge(
  value = help,
  source = n63,
  target = n106
); edges.append(e)

e91 = e = Edge(
  value = dep,
  source = n58,
  target = n107
); edges.append(e)

e92 = e = Edge(
  value = dep,
  source = n47,
  target = n108
); edges.append(e)

e93 = e = Edge(
  value = dep,
  source = n48,
  target = n108
); edges.append(e)

e94 = e = Edge(
  value = dep,
  source = n61,
  target = n110
); edges.append(e)

e95 = e = Edge(
  value = help,
  source = n111,
  target = n112
); edges.append(e)

e96 = e = Edge(
  value = help,
  source = n64,
  target = n112
); edges.append(e)

e97 = e = Edge(
  value = help,
  source = n113,
  target = n112
); edges.append(e)

e98 = e = Edge(
  value = help,
  source = n67,
  target = n112
); edges.append(e)

e99 = e = Edge(
  value = help,
  source = n69,
  target = n112
); edges.append(e)

e100 = e = Edge(
  value = help,
  source = n70,
  target = n112
); edges.append(e)

e101 = e = Edge(
  value = help,
  source = n125,
  target = n112
); edges.append(e)

e102 = e = Edge(
  value = help,
  source = n77,
  target = n112
); edges.append(e)

e103 = e = Edge(
  value = help,
  source = n79,
  target = n112
); edges.append(e)

e104 = e = Edge(
  value = help,
  source = n88,
  target = n112
); edges.append(e)

e105 = e = Edge(
  value = help,
  source = n116,
  target = n112
); edges.append(e)

e106 = e = Edge(
  value = help,
  source = n96,
  target = n112
); edges.append(e)

e107 = e = Edge(
  value = help,
  source = n90,
  target = n112
); edges.append(e)

e108 = e = Edge(
  value = help,
  source = n82,
  target = n113
); edges.append(e)

e109 = e = Edge(
  value = help,
  source = n64,
  target = n114
); edges.append(e)

e110 = e = Edge(
  value = help,
  source = n134,
  target = n114
); edges.append(e)

e111 = e = Edge(
  value = help,
  source = n70,
  target = n114
); edges.append(e)

e112 = e = Edge(
  value = help,
  source = n72,
  target = n114
); edges.append(e)

e113 = e = Edge(
  value = help,
  source = n78,
  target = n114
); edges.append(e)

e114 = e = Edge(
  value = help,
  source = n123,
  target = n114
); edges.append(e)

e115 = e = Edge(
  value = help,
  source = n84,
  target = n114
); edges.append(e)

e116 = e = Edge(
  value = help,
  source = n85,
  target = n114
); edges.append(e)

e117 = e = Edge(
  value = help,
  source = n89,
  target = n114
); edges.append(e)

e118 = e = Edge(
  value = help,
  source = n101,
  target = n114
); edges.append(e)

e119 = e = Edge(
  value = help,
  source = n132,
  target = n134
); edges.append(e)

e120 = e = Edge(
  value = help,
  source = n64,
  target = n115
); edges.append(e)

e121 = e = Edge(
  value = help,
  source = n68,
  target = n115
); edges.append(e)

e122 = e = Edge(
  value = help,
  source = n83,
  target = n115
); edges.append(e)

e123 = e = Edge(
  value = help,
  source = n120,
  target = n115
); edges.append(e)

e124 = e = Edge(
  value = help,
  source = n116,
  target = n115
); edges.append(e)

e125 = e = Edge(
  value = help,
  source = n117,
  target = n116
); edges.append(e)

e126 = e = Edge(
  value = help,
  source = n77,
  target = n116
); edges.append(e)

e127 = e = Edge(
  value = hurt,
  source = n83,
  target = n116
); edges.append(e)

e128 = e = Edge(
  value = help,
  source = n84,
  target = n116
); edges.append(e)

e129 = e = Edge(
  value = help,
  source = n124,
  target = n116
); edges.append(e)

e130 = e = Edge(
  value = help,
  source = n102,
  target = n116
); edges.append(e)

e131 = e = Edge(
  value = help,
  source = n104,
  target = n116
); edges.append(e)

e132 = e = Edge(
  value = help,
  source = n107,
  target = n116
); edges.append(e)

e133 = e = Edge(
  value = help,
  source = n110,
  target = n117
); edges.append(e)

e134 = e = Edge(
  value = help,
  source = n85,
  target = n117
); edges.append(e)

e135 = e = Edge(
  value = help,
  source = n105,
  target = n118
); edges.append(e)

e136 = e = Edge(
  value = help,
  source = n94,
  target = n118
); edges.append(e)

e137 = e = Edge(
  value = help,
  source = n97,
  target = n118
); edges.append(e)

e138 = e = Edge(
  value = help,
  source = n98,
  target = n118
); edges.append(e)

e139 = e = Edge(
  value = help,
  source = n117,
  target = n119
); edges.append(e)

e140 = e = Edge(
  value = help,
  source = n118,
  target = n119
); edges.append(e)

e141 = e = Edge(
  value = help,
  source = n126,
  target = n119
); edges.append(e)

e142 = e = Edge(
  value = hurt,
  source = n108,
  target = n120
); edges.append(e)

e143 = e = Edge(
  value = help,
  source = n104,
  target = n120
); edges.append(e)

e144 = e = Edge(
  value = help,
  source = n118,
  target = n120
); edges.append(e)

e145 = e = Edge(
  value = help,
  source = n124,
  target = n120
); edges.append(e)

e146 = e = Edge(
  value = help,
  source = n83,
  target = n120
); edges.append(e)

e147 = e = Edge(
  value = help,
  source = n86,
  target = n120
); edges.append(e)

e148 = e = Edge(
  value = help,
  source = n80,
  target = n123
); edges.append(e)

e149 = e = Edge(
  value = help,
  source = n81,
  target = n123
); edges.append(e)

e150 = e = Edge(
  value = hurt,
  source = n65,
  target = n124
); edges.append(e)

e151 = e = Edge(
  value = help,
  source = n66,
  target = n124
); edges.append(e)

e152 = e = Edge(
  value = hurt,
  source = n76,
  target = n124
); edges.append(e)

e153 = e = Edge(
  value = help,
  source = n129,
  target = n124
); edges.append(e)

e154 = e = Edge(
  value = hurt,
  source = n83,
  target = n124
); edges.append(e)

e155 = e = Edge(
  value = help,
  source = n84,
  target = n124
); edges.append(e)

e156 = e = Edge(
  value = hurt,
  source = n128,
  target = n124
); edges.append(e)

e157 = e = Edge(
  value = hurt,
  source = n87,
  target = n124
); edges.append(e)

e158 = e = Edge(
  value = hurt,
  source = n91,
  target = n124
); edges.append(e)

e159 = e = Edge(
  value = hurt,
  source = n92,
  target = n124
); edges.append(e)

e160 = e = Edge(
  value = help,
  source = n93,
  target = n124
); edges.append(e)

e161 = e = Edge(
  value = help,
  source = n73,
  target = n125
); edges.append(e)

e162 = e = Edge(
  value = help,
  source = n75,
  target = n125
); edges.append(e)

e163 = e = Edge(
  value = help,
  source = n101,
  target = n126
); edges.append(e)

e164 = e = Edge(
  value = hurt,
  source = n102,
  target = n126
); edges.append(e)

e165 = e = Edge(
  value = help,
  source = n103,
  target = n126
); edges.append(e)

e166 = e = Edge(
  value = help,
  source = n77,
  target = n126
); edges.append(e)

e167 = e = Edge(
  value = help,
  source = n88,
  target = n126
); edges.append(e)

e168 = e = Edge(
  value = help,
  source = n90,
  target = n126
); edges.append(e)

e169 = e = Edge(
  value = help,
  source = n96,
  target = n126
); edges.append(e)

e170 = e = Edge(
  value = help,
  source = n95,
  target = n127
); edges.append(e)

e171 = e = Edge(
  value = OR,
  source = n130,
  target = n128
); edges.append(e)

e172 = e = Edge(
  value = OR,
  source = n131,
  target = n128
); edges.append(e)

e173 = e = Edge(
  value = OR,
  source = n132,
  target = n128
); edges.append(e)

e174 = e = Edge(
  value = OR,
  source = n133,
  target = n128
); edges.append(e)

e175 = e = Edge(
  value = hurt,
  source = n80,
  target = n129
); edges.append(e)

e176 = e = Edge(
  value = OR,
  source = n86,
  target = n130
); edges.append(e)

e177 = e = Edge(
  value = OR,
  source = n86,
  target = n131
); edges.append(e)

e178 = e = Edge(
  value = OR,
  source = n86,
  target = n132
); edges.append(e)

e179 = e = Edge(
  value = OR,
  source = n86,
  target = n133
); edges.append(e)

graph = Graph(nodes=nodes, edges=edges)