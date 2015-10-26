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
  name = "Reduced Misconceptions",
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
  name = "Provide Resource to Regional Offices",
  type = task,
  container = "CS"
);nodes.append(n)

n133 = n = Node(
  name = "Provide Counselling Resources",
  type = task,
  container = "CS"
);nodes.append(n)

