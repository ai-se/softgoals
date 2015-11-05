import os, sys
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from pystar.template import *
__author__ = 'george'

nodes = []

n1 = n = SoftGoal(
  "Increase Resources[Services]",
  container = "CS"
);nodes.append(n)

n2 = n = HardGoal(
  "Services be Bilingual",
  container = "CS"
);nodes.append(n)

n3 = n = SoftGoal(
  "High Quality Service",
  container = "CS"
);nodes.append(n)

n4 = n = Task(
  "Maintain/Implement CS Services",
  container = "CS"
);nodes.append(n)

n5 = n = Task(
  "Maintain Web Services",
  container = "CS"
);nodes.append(n)

n6 = n = Task(
  "Maintain Phone Services",
  container = "CS"
);nodes.append(n)

n7 = n = Task(
  "Maintain/Implement PHL Services",
  container = "CS"
);nodes.append(n)

n8 = n = SoftGoal(
  "Increase Number of Services",
  container = "CS"
);nodes.append(n)

n9 = n = SoftGoal(
  "Efficient Services",
  container = "CS"
);nodes.append(n)

n10 = n = SoftGoal(
  "Available [Services]",
  container = "CS"
);nodes.append(n)

n11 = n = Resource(
  "Service Resources",
  container = "CS"
);nodes.append(n)

n12 = n = SoftGoal(
  "Measure Success of Services",
  container = "CS"
);nodes.append(n)

n13 = n = SoftGoal(
  "Immediacy",
  container = "CS Technology Services"
);nodes.append(n)

n14 = n = HardGoal(
  "Services Be Bilingual",
  container = "CS Technology Services"
);nodes.append(n)

n15 = n = SoftGoal(
  "Increase Resources [Services]",
  container = "CS Technology Services"
);nodes.append(n)

n16 = n = SoftGoal(
  "Anonymity",
  container = "CS Technology Services"
);nodes.append(n)

n17 = n = SoftGoal(
  "Anonymity [Kids]",
  container = "CS Technology Services"
);nodes.append(n)

n18 = n = SoftGoal(
  "Avoid Presence of Pedofiles",
  container = "CS Technology Services"
);nodes.append(n)

n19 = n = SoftGoal(
  "Confidentiality [Kids]",
  container = "CS Technology Services"
);nodes.append(n)

n20 = n = SoftGoal(
  "Increase Web Resources",
  container = "CS Technology Services"
);nodes.append(n)

n21 = n = SoftGoal(
  "Sufficiently Moderated Web Services",
  container = "CS Technology Services"
);nodes.append(n)

n22 = n = SoftGoal(
  "Increased Web Services",
  container = "CS Technology Services"
);nodes.append(n)

n23 = n = SoftGoal(
  "Avoid Bad Advice",
  container = "CS Technology Services"
);nodes.append(n)

n24 = n = SoftGoal(
  "Direct Response to Kids",
  container = "CS Technology Services"
);nodes.append(n)

n25 = n = SoftGoal(
  "Improve Website Content",
  container = "CS Technology Services"
);nodes.append(n)

n26 = n = SoftGoal(
  "Efficient Web Services",
  container = "CS Technology Services"
);nodes.append(n)

n27 = n = SoftGoal(
  "Decrease Response Time",
  container = "CS Technology Services"
);nodes.append(n)

n28 = n = SoftGoal(
  "Increase Phone Resources",
  container = "CS Technology Services"
);nodes.append(n)

n29 = n = Task(
  "Maintain Phone Services",
  container = "CS Technology Services"
);nodes.append(n)

n30 = n = SoftGoal(
  "Available [Services]",
  container = "CS Technology Services"
);nodes.append(n)

n31 = n = Task(
  "Implement Phone Feedback",
  container = "CS Technology Services"
);nodes.append(n)

n32 = n = HardGoal(
  "Counsellors be Professionally Trained",
  container = "CS Technology Services"
);nodes.append(n)

n33 = n = Task(
  "Acquire Feedback",
  container = "CS Technology Services"
);nodes.append(n)

n34 = n = HardGoal(
  "Service Levels Be Met",
  container = "CS Technology Services"
);nodes.append(n)

n35 = n = SoftGoal(
  "Increase Number of Services",
  container = "CS Technology Services"
);nodes.append(n)

n36 = n = SoftGoal(
  "High Quality Services",
  container = "CS Technology Services"
);nodes.append(n)

n37 = n = SoftGoal(
  "Efficient Services",
  container = "CS Technology Services"
);nodes.append(n)

n38 = n = SoftGoal(
  "Confidentiality",
  container = "CS Technology Services"
);nodes.append(n)

n39 = n = SoftGoal(
  "Relevance in Kids Lives",
  container = "CS Technology Services"
);nodes.append(n)

n40 = n = SoftGoal(
  "Efficient Phone Services",
  container = "CS Technology Services"
);nodes.append(n)

n41 = n = SoftGoal(
  "Anonymity [Parents]",
  container = "CS Technology Services"
);nodes.append(n)

n42 = n = SoftGoal(
  "Confidentiality [Parents]",
  container = "CS Technology Services"
);nodes.append(n)

n43 = n = Task(
  "Implement Services",
  container = "CS Technology Services"
);nodes.append(n)

n44 = n = HardGoal(
  "Services be provided for Kids Bullying Line",
  container = "CS Technology Services"
);nodes.append(n)

n45 = n = Task(
  "Implement Feedback Collection",
  container = "CS Technology Services"
);nodes.append(n)

n46 = n = SoftGoal(
  "Connect Back to the Community",
  container = "CS Technology Services"
);nodes.append(n)

n47 = n = SoftGoal(
  "Kids Have Ownership of Services",
  container = "CS Technology Services"
);nodes.append(n)

n48 = n = Task(
  "Maintain/Implement CS Services",
  container = "CS Technology Services"
);nodes.append(n)

n49 = n = Task(
  "Maintain Web Services",
  container = "CS Technology Services"
);nodes.append(n)

n50 = n = Task(
  "Acquire Service Resources",
  container = "CS Technology Services"
);nodes.append(n)

n51 = n = Task(
  "Implement Feedback Form",
  container = "CS Technology Services"
);nodes.append(n)

n52 = n = Task(
  "Maintain/Implement PHL Services",
  container = "CS Technology Services"
);nodes.append(n)

n53 = n = HardGoal(
  "Services be provided for Kids Bullying Line",
  container = "Provincial government"
);nodes.append(n)

n54 = n = SoftGoal(
  "Quality [Services]",
  container = "Parents"
);nodes.append(n)

n55 = n = SoftGoal(
  "Immediacy [Services]",
  container = "Parents"
);nodes.append(n)

n56 = n = SoftGoal(
  "Confidentiality [Services]",
  container = "Parents"
);nodes.append(n)

n57 = n = SoftGoal(
  "Connect Back to the Community",
  container = "Parents"
);nodes.append(n)

n58 = n = SoftGoal(
  "Availability [Services]",
  container = "Parents"
);nodes.append(n)

n59 = n = SoftGoal(
  "Improve Image to Kids",
  container = "CS"
);nodes.append(n)

n60 = n = SoftGoal(
  "Maintain Services above Competition",
  container = "CS"
);nodes.append(n)

n61 = n = SoftGoal(
  "Avoid Presence of Pedofiles",
  container = "CS"
);nodes.append(n)

n62 = n = SoftGoal(
  "Reduce Contagion Effect [Of Harmful Actions]",
  container = "CS"
);nodes.append(n)

n63 = n = SoftGoal(
  "Encourage Kids Using Web Services to Use Phone Services",
  container = "CS"
);nodes.append(n)

n64 = n = SoftGoal(
  "Web Services Self Serve",
  container = "CS"
);nodes.append(n)

n65 = n = SoftGoal(
  "Empowering Kids to Help Themselves",
  container = "CS"
);nodes.append(n)

n66 = n = Resource(
  "Web Server",
  container = "IT Department"
);nodes.append(n)

n67 = n = Resource(
  "Feedback Form Software",
  container = "IT Department"
);nodes.append(n)

n68 = n = Resource(
  "Web Software",
  container = "IT Department"
);nodes.append(n)

n69 = n = HardGoal(
  "Telephony Be Implemented and Managed",
  container = "IT Department"
);nodes.append(n)

n70 = n = Task(
  "Implement Phone Feedback",
  container = "IT Department"
);nodes.append(n)

n71 = n = Task(
  "Put Content Onto Website",
  container = "IT Department"
);nodes.append(n)

n72 = n = Resource(
  "Strategic Blue Print",
  container = "Web Task Force"
);nodes.append(n)

n73 = n = Task(
  "Maintain Implement CS Services",
  container = "CS Service"
);nodes.append(n)

n74 = n = SoftGoal(
  "Connect Back to the Community",
  container = "CS Service"
);nodes.append(n)

n75 = n = Task(
  "Maintain Implement CS Web Services",
  container = "CS Service"
);nodes.append(n)

n76 = n = Task(
  "Maintain CS Phone Services",
  container = "CS Service"
);nodes.append(n)

n77 = n = SoftGoal(
  "Kids Have Ownership of Services",
  container = "CS Service"
);nodes.append(n)

n78 = n = Task(
  "Maintain/Implement CS Services",
);nodes.append(n)

n79 = n = SoftGoal(
  "Connect Back to the Community",
);nodes.append(n)

n80 = n = SoftGoal(
  "Kids Have Ownership of Services",
);nodes.append(n)

n81 = n = SoftGoal(
  "Web Services Self Serve",
  container = "CS Web Services"
);nodes.append(n)

n82 = n = SoftGoal(
  "Web Services Self Serve",
);nodes.append(n)

n83 = n = Task(
  "Maintain/Implement CS Web Services",
);nodes.append(n)

n84 = n = SoftGoal(
  "Immediacy",
);nodes.append(n)

n85 = n = SoftGoal(
  "Easier Navigation [CS Web Services]",
);nodes.append(n)

n86 = n = SoftGoal(
  "Decrease Response Time",
);nodes.append(n)

n87 = n = SoftGoal(
  "Measure Success of Services",
);nodes.append(n)

n88 = n = SoftGoal(
  "Sufficiently Moderated Web Services",
);nodes.append(n)

n89 = n = Task(
  "Implement Feedback Form",
  container = "Web Service"
);nodes.append(n)

n90 = n = Task(
  "Obtain Needed Software",
  container = "Web Service"
);nodes.append(n)

n91 = n = Task(
  "Obtain Web Server",
  container = "Web Service"
);nodes.append(n)

n92 = n = SoftGoal(
  "Web Services Self Serve",
  container = "Web Service"
);nodes.append(n)

n93 = n = SoftGoal(
  "Immediacy",
  container = "Web Service"
);nodes.append(n)

n94 = n = HardGoal(
  "Only Online Request from Canadians Accepted",
  container = "Web Service"
);nodes.append(n)

n95 = n = SoftGoal(
  "Decrease Response Time",
  container = "Web Service"
);nodes.append(n)

n96 = n = SoftGoal(
  "Control [Web Services]",
  container = "Web Service"
);nodes.append(n)

n97 = n = Task(
  "Maintain PHL Web Services",
  container = "Web Service"
);nodes.append(n)

n98 = n = SoftGoal(
  "Available [Services]",
  container = "Web Service"
);nodes.append(n)

n99 = n = SoftGoal(
  "Efficient Web Services",
  container = "Web Service"
);nodes.append(n)

n100 = n = SoftGoal(
  "Improve Website Content",
  container = "Web Service"
);nodes.append(n)

n101 = n = SoftGoal(
  "Avoid Bad Advice",
  container = "Web Service"
);nodes.append(n)

n102 = n = SoftGoal(
  "Increased Web Services",
  container = "Web Service"
);nodes.append(n)

n103 = n = SoftGoal(
  "Sufficiently Moderated Web Services",
  container = "Web Service"
);nodes.append(n)

n104 = n = SoftGoal(
  "Confidentiality [Kids]",
  container = "Web Service"
);nodes.append(n)

n105 = n = SoftGoal(
  "Increase Web Resources",
  container = "Web Service"
);nodes.append(n)

n106 = n = SoftGoal(
  "Anonymity [Kids]",
  container = "Web Service"
);nodes.append(n)

n107 = n = SoftGoal(
  "Measure Success of Services",
  container = "Web Service"
);nodes.append(n)

n108 = n = SoftGoal(
  "Accommodate Web Site Traffic",
  container = "Web Service"
);nodes.append(n)

n109 = n = Task(
  "Maintain Web Services",
  container = "Web Service"
);nodes.append(n)

n110 = n = HardGoal(
  "Web Traffic Be Kept Track of",
  container = "Web Service"
);nodes.append(n)

n111 = n = Task(
  "Maintain/Implement CS Web Services",
  container = "Web Service"
);nodes.append(n)

n112 = n = HardGoal(
  "Web Site Content Be Updated Daily",
  container = "Web Service"
);nodes.append(n)

n113 = n = Task(
  "Obtain Software",
  container = "Web Service"
);nodes.append(n)

n114 = n = SoftGoal(
  "Sufficient Counselling Resources",
  container = "Web Service"
);nodes.append(n)

n115 = n = SoftGoal(
  "Easier Navigation [CS Web Services]",
  container = "Web Service"
);nodes.append(n)

n116 = n = SoftGoal(
  "Anonymity [Kids]",
);nodes.append(n)

n117 = n = SoftGoal(
  "Kids Have Ownership of Services",
);nodes.append(n)

n118 = n = SoftGoal(
  "Confidentiality [Kids]",
);nodes.append(n)

n119 = n = SoftGoal(
  "Increase Web Resources",
);nodes.append(n)

n120 = n = SoftGoal(
  "Sufficiently Moderated Web Services",
);nodes.append(n)

n121 = n = SoftGoal(
  "Increased Web Services",
);nodes.append(n)

n122 = n = SoftGoal(
  "Avoid Bad Advice",
);nodes.append(n)

n123 = n = Task(
  "Maintain Web Services",
);nodes.append(n)

n124 = n = Task(
  "Implement Feedback Form",
);nodes.append(n)

n125 = n = SoftGoal(
  "Improve Website Content",
);nodes.append(n)

n126 = n = SoftGoal(
  "Efficient Web Services",
);nodes.append(n)

n127 = n = SoftGoal(
  "Decrease Response Time",
);nodes.append(n)

n128 = n = SoftGoal(
  "Connect Back to the Community",
);nodes.append(n)

n129 = n = SoftGoal(
  "Available [Services]",
);nodes.append(n)

n130 = n = SoftGoal(
  "Relevance in Kids Lives",
);nodes.append(n)

n131 = n = SoftGoal(
  "Increased Web Services"
);nodes.append(n)

n132 = n = SoftGoal(
  "Sufficient Counselling Resources"
);nodes.append(n)

n133 = n = SoftGoal(
  "Anonymity [Kids]"
);nodes.append(n)

n134 = n = SoftGoal(
  "Control [Web Services]"
);nodes.append(n)

n135 = n = SoftGoal(
  "Direct Response to Kids"
);nodes.append(n)

n136 = n = SoftGoal(
  "Confidentiality [Kids]"
);nodes.append(n)

n137 = n = SoftGoal(
  "Avoid Bad Advice"
);nodes.append(n)

n138 = n = Task(
  "Maintain CS Phone Services"
);nodes.append(n)

n139 = n = SoftGoal(
  "Immediacy",
  container = "PHL Web Service -> Web Service"
);nodes.append(n)

n140 = n = SoftGoal(
  "Immediacy",
  container = "Phone Service -> Web Service"
);nodes.append(n)

n141 = n = SoftGoal(
  "Increase Phone Resources",
);nodes.append(n)

n142 = n = SoftGoal(
  "Efficient Phone Services",
);nodes.append(n)

n143 = n = SoftGoal(
  "Anonymity [Parents]",
);nodes.append(n)

n145 = n = Task(
  "Maintain Phone Services",
);nodes.append(n)

n146 = n = SoftGoal(
  "Confidentiality [Parents]",
);nodes.append(n)

n147 = n = Task(
  "Implement Phone Feedback",
);nodes.append(n)

n148 = n = HardGoal(
  "Counsellors Be Professionally Trained",
  container = "Counselling Management"
);nodes.append(n)

n149 = n = Resource(
  "Feedback",
  container = "Parents"
);nodes.append(n)

n150 = n = SoftGoal(
  "Anonymity [Parents]",
  container = "Parents"
);nodes.append(n)

n151 = n = SoftGoal(
  "Anonymity [Kids]",
  container = "PHL Web Services"
);nodes.append(n)

n152 = n = SoftGoal(
  "Confidentiality [Parents]",
);nodes.append(n)

n153 = n = SoftGoal(
  "Connect Back to the Community",
);nodes.append(n)

n154 = n = Task(
  "Maintain PHL Web Services",
);nodes.append(n)

n155 = n = Task(
  "Maintain PHL Phone Services",
);nodes.append(n)

n156 = n = Task(
  "Maintain PHL Phone Services",
  container = "Parents"
);nodes.append(n)

n157 = n = Task(
  "Parents use Phone Counselling",
  container = "Parents"
);nodes.append(n)

n158 = n = SoftGoal(
  "Similarity with other parents' problems",
  container = "Parents"
);nodes.append(n)

n159 = n = SoftGoal(
  "Decrease [Phone Waiting Time]",
  container = "Parents"
);nodes.append(n)

n160 = n = SoftGoal(
  "Immediacy",
  container = "Phone Service"
);nodes.append(n)

n161 = n = SoftGoal(
  "Increase Phone Resources",
  container = "Phone Service"
);nodes.append(n)

n162 = n = SoftGoal(
  "Available [Services]",
  container = "Phone Service"
);nodes.append(n)

n163 = n = SoftGoal(
  "Sufficient Counselling Resources",
  container = "Phone Service"
);nodes.append(n)

n164 = n = Task(
  "Maintain CS Phone Services",
  container = "Phone Service"
);nodes.append(n)

n165 = n = SoftGoal(
  "Anonymity [Parents]",
  container = "Phone Service"
);nodes.append(n)

n166 = n = Task(
  "Maintain PHL Phone Services",
  container = "Phone Service"
);nodes.append(n)

n167 = n = SoftGoal(
  "Accommodate Phone Traffic",
  container = "Phone Service"
);nodes.append(n)

n168 = n = Task(
  "Implement Phone Feedback",
  container = "Phone Service"
);nodes.append(n)

n169 = n = SoftGoal(
  "Measure Success of Services",
  container = "Phone Service"
);nodes.append(n)

n170 = n = SoftGoal(
  "Confidentiality [Parents]",
  container = "Phone Service"
);nodes.append(n)

n171 = n = SoftGoal(
  "Efficient Phone Services",
  container = "Phone Service"
);nodes.append(n)

n172 = n = Task(
  "Maintain Phone Services",
  container = "Phone Service"
);nodes.append(n)

n173 = n = Task(
  "Trace Calls",
  container = "Phone Service"
);nodes.append(n)

n174 = n = HardGoal(
  "Telephony Be Implemented and Managed",
  container = "Phone Service"
);nodes.append(n)

n175 = n = SoftGoal(
  "Connect Back to the Community",
  container = "PHL Service"
);nodes.append(n)

n176 = n = Task(
  "Maintain/Implement PHL Services",
  container = "PHL Service"
);nodes.append(n)

n177 = n = Task(
  "Maintain PHL Web Services",
  container = "PHL Service"
);nodes.append(n)

n178 = n = Task(
  "Maintain PHL Phone Services",
  container = "PHL Service"
);nodes.append(n)

n179 = n = Task(
  "Kids Read General Questions and Answers",
  container = "Kids and Youth"
);nodes.append(n)

n180 = n = Task(
  "Implement Polls about Kids",
  container = "Kids and Youth"
);nodes.append(n)

n181 = n = Task(
  "Kids read Polls about Kids",
  container = "Kids and Youth"
);nodes.append(n)

n182 = n = Task(
  "Implement General Questions and Answers",
  container = "Kids and Youth"
);nodes.append(n)

n183 = n = Task(
  "Kids use get Informed Section of Website",
  container = "Kids and Youth"
);nodes.append(n)

n184 = n = Task(
  "Implement Get Informed Section of Website",
  container = "Kids and Youth"
);nodes.append(n)

n185 = n = SoftGoal(
  "Increase Emphasis on Online Feedback Form",
  container = "Counselling"
);nodes.append(n)

n186 = n = SoftGoal(
  "Easier to Find Posts [Web Posting Technology]",
  container = "Counselling"
);nodes.append(n)

n187 = n = Resource(
  "Web Site Content",
  container = "Counselling"
);nodes.append(n)

n188 = n = SoftGoal(
  "Anonymity [Counsellors]",
  container = "Counselling"
);nodes.append(n)

n189 = n = SoftGoal(
  "Reduce Prank Calls ",
  container = "Counselling"
);nodes.append(n)

n190 = n = SoftGoal(
  "Avoid Dialogues",
  container = "Counselling"
);nodes.append(n)

n191 = n = SoftGoal(
  "Correct Interpretation of Counsel",
  container = "Counselling"
);nodes.append(n)

n192 = n = SoftGoal(
  "Reduce Number of Steps [Web Posting Technology]",
  container = "Counselling"
);nodes.append(n)

n193 = n = SoftGoal(
  "Control of Counselling Work",
  container = "Counselling"
);nodes.append(n)

n194 = n = SoftGoal(
  "Anonymity [Kids]",
  container = "CS Web Services"
);nodes.append(n)

n195 = n = Task(
  "Maintain/Implement CS Web Services",
  container = "CS Web Services"
);nodes.append(n)

n196 = n = SoftGoal(
  "Relevance in Kids Lives",
  container = "CS Web Services"
);nodes.append(n)

n197 = n = HardGoal(
  "Strategic Blue Print for Website Be Followed",
  container = "CS Web Services"
);nodes.append(n)

n198 = n = SoftGoal(
  "Connect Back to the Community",
  container = "CS Web Services"
);nodes.append(n)

n199 = n = SoftGoal(
  "Maintain Services above Competition",
  container = "CS Web Services"
);nodes.append(n)

n200 = n = SoftGoal(
  "Encourage Kids Using Web Services to Use Phone Services",
  container = "CS Web Services"
);nodes.append(n)

n201 = n = SoftGoal(
  "Measure Success of Services",
  container = "CS Web Services"
);nodes.append(n)

n202 = n = SoftGoal(
  "Empowering Kids to Help Themselves",
  container = "CS Web Services"
);nodes.append(n)

n203 = n = SoftGoal(
  "Easier Navigation [CS Web Services]",
  container = "CS Web Services"
);nodes.append(n)

n204 = n = SoftGoal(
  "Avoid Presence of Pedofiles",
  container = "CS Web Services"
);nodes.append(n)

n205 = n = SoftGoal(
  "Reduce Contagion Effect[Of harmful Actions]",
  container = "CS Web Services"
);nodes.append(n)

n206 = n = SoftGoal(
  "Improve Image to Kids",
  container = "CS Web Services"
);nodes.append(n)

n207 = n = SoftGoal(
  "Improve Image to Kids",
  container = "CS Web Services"
);nodes.append(n)

n208 = n = SoftGoal(
  "Immediacy",
  container = "CS Web Services"
);nodes.append(n)

n209 = n = SoftGoal(
  "Increase Emphasis on Online Feedback",
  container = "CS Web Services"
);nodes.append(n)

n210 = n = SoftGoal(
  "Similarity of Problems",
  container = "CS Web Services"
);nodes.append(n)

n211 = n = HardGoal(
  "Kids Use Online Information Provided",
  container = "CS Web Services"
);nodes.append(n)

n212 = n = SoftGoal(
  "Easier to Find Posts [Web Posting Technology]",
  container = "CS Web Services"
);nodes.append(n)

n213 = n = SoftGoal(
  "Effective chat room filters",
  container = "CS Web Services"
);nodes.append(n)

n214 = n = SoftGoal(
  "Avoid Dialogues [Between Kids]",
  container = "CS Web Services"
);nodes.append(n)

n215 = n = SoftGoal(
  "Avoid Bad Advice",
  container = "CS Web Services"
);nodes.append(n)

n216 = n = SoftGoal(
  "Avoid Dialogues Between[Kids and Counsellors on the Web]",
  container = "CS Web Services"
);nodes.append(n)

n217 = n = SoftGoal(
  "Control [Web Services]",
  container = "CS Web Services"
);nodes.append(n)

n218 = n = SoftGoal(
  "Sufficiently Moderated Web Services",
  container = "CS Web Services"
);nodes.append(n)

n219 = n = SoftGoal(
  "Confidentiality [Kids]",
  container = "CS Web Services"
);nodes.append(n)

n220 = n = SoftGoal(
  "Decrease Response Time",
  container = "CS Web Services"
);nodes.append(n)

n221 = n = SoftGoal(
  "Direct Response to Kids",
  container = "CS Web Services"
);nodes.append(n)

n222 = n = SoftGoal(
  "Kids Have Ownership of Services",
  container = "CS Web Services"
);nodes.append(n)

n223 = n = Task(
  "Kids Read Polls about Kids",
  container = "CS Web Services"
);nodes.append(n)

n224 = n = Task(
  "Implement Polls about Kids",
  container = "CS Web Services"
);nodes.append(n)

n225 = n = Task(
  "Implement General Questions and Answers",
  container = "CS Web Services"
);nodes.append(n)

n226 = n = Task(
  "Implement Get Informed Section of Web Site",
  container = "CS Web Services"
);nodes.append(n)

n227 = n = Task(
  "Kids Read General Questions and Answers",
  container = "CS Web Services"
);nodes.append(n)

n228 = n = Task(
  "Kids Read Get Informed Section of Website",
  container = "CS Web Services"
);nodes.append(n)

n229 = n = Task(
  "Kids Get Information through E-Counselling",
  container = "CS Web Services"
);nodes.append(n)

n230 = n = SoftGoal(
  "Control of Counselling Work",
  container = "CS Web Services"
);nodes.append(n)

n231 = n = Task(
  "Put Content onto Website",
  container = "CS Web Services"
);nodes.append(n)

n232 = n = Task(
  "Acquire Web Content",
  container = "CS Web Services"
);nodes.append(n)

n233 = n = SoftGoal(
  "Reduce Number of Steps[Web Posting Technology]",
  container = "CS Web Services"
);nodes.append(n)

n234 = n = SoftGoal(
  "Correct Interpretation of Counsel",
  container = "CS Web Services"
);nodes.append(n)

n235 = n = HardGoal(
  "Technology that Does Not Allow Dialogue Between Kids Be Used",
  container = "CS Web Services"
);nodes.append(n)

n236 = n = HardGoal(
  "Technology that Allows Dialogue Between Kids Be Used",
  container = "CS Web Services"
);nodes.append(n)

n237 = n = HardGoal(
  "Anonymous Technology Be Used",
  container = "CS Web Services"
);nodes.append(n)

n238 = n = HardGoal(
  "Non-Anonymous Technology Be Used",
  container = "CS Web Services"
);nodes.append(n)

n239 = n = HardGoal(
  "Moderated E-Counselling Be Used",
  container = "CS Web Services"
);nodes.append(n)

n240 = n = HardGoal(
  "Non-Confidential Technology Be Used",
  container = "CS Web Services"
);nodes.append(n)

n241 = n = HardGoal(
  "Confidential Technology Be Used",
  container = "CS Web Services"
);nodes.append(n)

n242 = n = HardGoal(
  "Real Time E-Counselling Be Used",
  container = "CS Web Services"
);nodes.append(n)

n243 = n = HardGoal(
  "Non-Real Time E-Counselling Be Used",
  container = "CS Web Services"
);nodes.append(n)

n244 = n = SoftGoal(
  "Increased Web Services",
  container = "CS Web Services"
);nodes.append(n)

n245 = n = SoftGoal(
  "Anonymity [Counsellors]",
  container = "CS Web Services"
);nodes.append(n)

n246 = n = SoftGoal(
  "Friendly Web Site",
  container = "CS Web Services"
);nodes.append(n)

n247 = n = Task(
  "Kids Use Video Counselling",
  container = "CS Web Services"
);nodes.append(n)

n248 = n = Task(
  "Implement Video Counselling",
  container = "CS Web Services"
);nodes.append(n)

n249 = n = Task(
  "Kids Use Voice Counselling",
  container = "CS Web Services"
);nodes.append(n)

n250 = n = Task(
  "Implement Voice Counselling",
  container = "CS Web Services"
);nodes.append(n)

n251 = n = Task(
  "Kids Use Cyber Cafe/Portal/Chat Room",
  container = "CS Web Services"
);nodes.append(n)

n252 = n = Task(
  "Implement Cyber Cafe/Portal/Chat Room",
  container = "CS Web Services"
);nodes.append(n)

n253 = n = Task(
  "Implement Filters",
  container = "CS Web Services"
);nodes.append(n)

n254 = n = Task(
  "Block Kids who Display Inappropriate Behaviour",
  container = "CS Web Services"
);nodes.append(n)

n255 = n = Task(
  "Schedule Chat at Specific Times",
  container = "CS Web Services"
);nodes.append(n)

n256 = n = Task(
  "Implement Delay",
  container = "CS Web Services"
);nodes.append(n)

n257 = n = Task(
  "Kids Use Ask a Counsellor Section",
  container = "CS Web Services"
);nodes.append(n)

n258 = n = Task(
  "Maintain Ask a Counsellor Section",
  container = "CS Web Services"
);nodes.append(n)

n259 = n = Task(
  "Kids Use Text Messaging",
  container = "CS Web Services"
);nodes.append(n)

n260 = n = Task(
  "Implement Text Messaging",
  container = "CS Web Services"
);nodes.append(n)

n261 = n = SoftGoal(
  "Easier Access to Post Reply",
  container = "CS Web Services"
);nodes.append(n)

n262 = n = Task(
  "Inform Kids about Anonymity[Kids] of Web Services",
  container = "CS Web Services"
);nodes.append(n)

n263 = n = Task(
  "Kids Use One-On-One Chat Rooms",
  container = "CS Web Services"
);nodes.append(n)

n264 = n = Task(
  "Kids Use One-On-One Chat Rooms",
  container = "CS Web Services"
);nodes.append(n)

n265 = n = Task(
  "Implement One-On-One Chat Rooms",
  container = "CS Web Services"
);nodes.append(n)

n266 = n = Task(
  "Implement One-On-One Chat Rooms",
  container = "CS Web Services"
);nodes.append(n)

n267 = n = Task(
  "Kids Use Bulletin Board with Replies",
  container = "CS Web Services"
);nodes.append(n)

n268 = n = Task(
  "Implement Bulletin Board with Replies",
  container = "CS Web Services"
);nodes.append(n)

n269 = n = Task(
  "Kids Use Email Counselling",
  container = "CS Web Services"
);nodes.append(n)

n270 = n = Task(
  "Implement Email Counselling",
  container = "CS Web Services"
);nodes.append(n)

n271 = n = Task(
  "Kids Use Bulletin Board with Delayed Moderation",
  container = "CS Web Services"
);nodes.append(n)

n272 = n = Task(
  "Implement Bulletin Board with Delayed Moderation",
  container = "CS Web Services"
);nodes.append(n)

n273 = n = SoftGoal(
  "Kids Have Ownership of Services",
  container = "CS Phone Services"
);nodes.append(n)

n274 = n = Task(
  "Kids Use Phone Counselling",
  container = "CS Phone Services"
);nodes.append(n)

n275 = n = SoftGoal(
  "Connect Back to the Community",
  container = "CS Phone Services"
);nodes.append(n)

n276 = n = SoftGoal(
  "Anonymity [Kids]",
  container = "CS Phone Services"
);nodes.append(n)

n277 = n = SoftGoal(
  "Confidentiality [Kids]",
  container = "CS Phone Services"
);nodes.append(n)

n278 = n = Task(
  "Maintain CS Phone Services",
  container = "CS Phone Services"
);nodes.append(n)

n279 = n = SoftGoal(
  "Determine Calls Coming from Web Users",
  container = "CS Phone Services"
);nodes.append(n)

n280 = n = Task(
  "Implement Anti-Pranking Message",
  container = "CS Phone Services"
);nodes.append(n)

n281 = n = SoftGoal(
  "Reduce Prank Calls",
  container = "CS Phone Services"
);nodes.append(n)

n282 = n = SoftGoal(
  "Decrease Phone Waiting Time",
  container = "CS Phone Services"
);nodes.append(n)

n283 = n = HardGoal(
  "Answer 80% of Calls within 30 Seconds of Message Ending",
  container = "CS Phone Services"
);nodes.append(n)

n284 = n = SoftGoal(
  "Connect Back to the Community",
  container = "PHL Phone Services"
);nodes.append(n)

n285 = n = SoftGoal(
  "Anonymity [Parents]",
  container = "PHL Phone Services"
);nodes.append(n)

n286 = n = Task(
  "Parents Use Phone Counselling",
  container = "PHL Phone Services"
);nodes.append(n)

n287 = n = Task(
  "Maintain PHL Phone Services",
  container = "PHL Phone Services"
);nodes.append(n)

n288 = n = Task(
  "Provide Recorded Messages",
  container = "PHL Phone Services"
);nodes.append(n)

n289 = n = SoftGoal(
  "Confidentiality [Parents]",
  container = "PHL Phone Services"
);nodes.append(n)

n290 = n = SoftGoal(
  "Anonymity [Parents]",
  container = "PHL Web Services"
);nodes.append(n)

n291 = n = SoftGoal(
  "Immediacy",
  container = "PHL Web Services"
);nodes.append(n)

n292 = n = SoftGoal(
  "Confidentiality [Parents]",
  container = "PHL Web Services"
);nodes.append(n)

n293 = n = SoftGoal(
  "Similarity with other parents' problems",
  container = "PHL Web Services"
);nodes.append(n)

n294 = n = SoftGoal(
  "Connect Back to the Community",
  container = "PHL Web Services"
);nodes.append(n)

n295 = n = Task(
  "Maintain PHL Web Services",
  container = "PHL Web Services"
);nodes.append(n)

n296 = n = SoftGoal(
  "Avoid Bad Advice",
  container = "PHL Web Services"
);nodes.append(n)

n297 = n = Task(
  "Parent Use Tool to Allow Parents to Talk to Each Other",
  container = "PHL Phone Services"
);nodes.append(n)

n298 = n = Task(
  "Implement Tool to Allow Parents to Talk to Each Other",
  container = "CS Phone Services"
);nodes.append(n)

n299 = n = Task(
  "Parent Use Bulletin Board with Replies",
  container = "PHL Phone Services"
);nodes.append(n)

n300 = n = Task(
  "Implement Board with Replies",
  container = "CS Phone Services"
);nodes.append(n)

n301 = n = Task(
  "Parent Use Information Section",
  container = "PHL Phone Services"
);nodes.append(n)

n302 = n = Task(
  "Implement Information Section",
  container = "CS Phone Services"
);nodes.append(n)

n303 = n = SoftGoal(
  "Easy [Access to Post Reply]",
  container = "CS Phone Services"
);nodes.append(n)

n304 = n = SoftGoal(
  "Friendly [Web Site]",
  container = "CS Phone Services"
);nodes.append(n)

n305 = n = Task(
  "Implement Tool to Allow Parents to Talk to Each Other",
  container = "Parents"
);nodes.append(n)

n306 = n = Task(
  "Parents Use Tool to Allow Parents to Talk to Each Other",
  container = "Parents"
);nodes.append(n)

n307 = n = Task(
  "Implement Board with Replies",
  container = "Parents"
);nodes.append(n)

n309 = n = Task(
  "Parents Use Bulletin Board with Replies",
  container = "Parents"
);nodes.append(n)

n310 = n = Task(
  "Implement Information Section",
  container = "Parents"
);nodes.append(n)

n311 = n = Task(
  "Parents Use Information Section",
  container = "Parents"
);nodes.append(n)

n312 = n = SoftGoal(
  "Friendly [Web Site]",
  container = "Parents"
);nodes.append(n)

n313 = n = Task(
  "Easy [Access to Post Reply]",
  container = "Parents"
);nodes.append(n)

n314 = n = Resource(
  "Phone Library of Recorded Messages",
  container = "Parents"
);nodes.append(n)

n315 = n = Task(
  "Kids use Video Counselling",
  container = "Kids and Youth"
);nodes.append(n)

n316 = n = Task(
  "Implement Video Counselling",
  container = "Kids and Youth"
);nodes.append(n)

n317 = n = Task(
  "Provide Web Counselling With Video",
  container = "Kids and Youth"
);nodes.append(n)

n318 = n = Task(
  "Provide Web Counselling With Audio",
  container = "Kids and Youth"
);nodes.append(n)

n319 = n = Task(
  "Kids Use Cyber Cafe/Portal/Chat Room",
  container = "Kids and Youth"
);nodes.append(n)

n320 = n = Task(
  "Implement Cyber Cafe/Portal/Chat Room",
  container = "Kids and Youth"
);nodes.append(n)

n321 = n = Task(
  "Kids Use Voice Counselling",
  container = "Kids and Youth"
);nodes.append(n)

n322 = n = Task(
  "Implement Voice Counselling",
  container = "Kids and Youth"
);nodes.append(n)

n323 = n = Task(
  "Moderate a Chat",
  container = "Kids and Youth"
);nodes.append(n)

n324 = n = SoftGoal(
  "Similarity of Problems",
  container = "Kids and Youth"
);nodes.append(n)

n325 = n = SoftGoal(
  "Connect to Other Kids",
  container = "Kids and Youth"
);nodes.append(n)

n326 = n = Task(
  "Kids use Text Messaging",
  container = "Kids and Youth"
);nodes.append(n)

n327 = n = Task(
  "Kids use Ask a Counsellor Section",
  container = "Kids and Youth"
);nodes.append(n)

n328 = n = Task(
  "Maintain Ask a Counsellor Section",
  container = "Kids and Youth"
);nodes.append(n)

n329 = n = Task(
  "Provide Written Counselling",
  container = "Kids and Youth"
);nodes.append(n)

n330 = n = Task(
  "Easier Access to Post Reply",
  container = "Kids and Youth"
);nodes.append(n)

n331 = n = Task(
  "Inform Kids about Anonymity[Kids] of Web Services",
  container = "Kids and Youth"
);nodes.append(n)

n332 = n = Task(
  "Kids Use One-On-One Chat Rooms",
  container = "Kids and Youth"
);nodes.append(n)

n333 = n = Task(
  "Moderate Discussion Boards",
  container = "Kids and Youth"
);nodes.append(n)

n334 = n = Task(
  "Implement Text Messaging",
  container = "Kids and Youth"
);nodes.append(n)

n335 = n = Task(
  "Implement Bulletin Board With Replies",
  container = "Kids and Youth"
);nodes.append(n)

n336 = n = Task(
  "Implement One-On-ONe Chat Rooms",
  container = "Kids and Youth"
);nodes.append(n)

n337 = n = Task(
  "Create Counselling Posts",
  container = "Kids and Youth"
);nodes.append(n)

n338 = n = Task(
  "Kids Use Bulletin Board with Replies",
  container = "Kids and Youth"
);nodes.append(n)

n339 = n = Task(
  "Implement Email Counselling",
  container = "Kids and Youth"
);nodes.append(n)

n340 = n = Task(
  "Perform Email Counselling",
  container = "Kids and Youth"
);nodes.append(n)

n341 = n = Task(
  "Kids Use Email Counselling",
  container = "Kids and Youth"
);nodes.append(n)

n342 = n = Task(
  "Kids Use Bulletin Board with Delayed Moderation",
  container = "Kids and Youth"
);nodes.append(n)

n343 = n = Task(
  "Implement Bulletin Board with Delayed Moderation",
  container = "Kids and Youth"
);nodes.append(n)

n344 = n = SoftGoal(
  "Friendly Web Site",
  container = "Kids and Youth"
);nodes.append(n)

n345 = n = Task(
  "Kids Use Phone Counselling",
  container = "Kids and Youth"
);nodes.append(n)

n346 = n = SoftGoal(
  "Decrease Phone Waiting Time",
  container = "Kids and Youth"
);nodes.append(n)

n347 = n = Task(
  "Maintain Phone Services",
  container = "Kids and Youth"
);nodes.append(n)

n348 = n = Task(
  "Voice Counselling Be Performed",
  container = "Kids and Youth"
);nodes.append(n)

n349 = n = SoftGoal(
  "Anonymity [Kids]",
  container = "Kids and Youth"
);nodes.append(n)

n350 = n = SoftGoal(
  "Connect Back to the Community",
  container = "Kids and Youth"
);nodes.append(n)

n351 = n = SoftGoal(
  "Kids have Ownership of Services",
  container = "Kids and Youth"
);nodes.append(n)

n352 = n = SoftGoal(
  "Immediacy",
  container = "Kids and Youth"
);nodes.append(n)

n353 = n = SoftGoal(
  "Confidentiality [Kids]",
  container = "Kids and Youth"
);nodes.append(n)

n354 = n = SoftGoal(
  "Available [Services]",
  container = "Kids and Youth"
);nodes.append(n)

n355 = n = SoftGoal(
  "High Quality Services",
  container = "Kids and Youth"
);nodes.append(n)

n356 = n = Resource(
  "Feedback",
  container = "Kids and Youth"
);nodes.append(n)

#EDGES

edges = []
e1 = e = Dep(
  source=n14,
  target=n2
);edges.append(e)

e2 = e = Dep(
  source=n36,
  target=n3
);edges.append(e)

e3 = e = Dep(
  source=n48,
  target=n4
);edges.append(e)

e4 = e = Dep(
  source=n49,
  target=n5
);edges.append(e)

e5 = e = Dep(
  source=n29,
  target=n6
);edges.append(e)

e6 = e = Dep(
  source=n52,
  target=n7
);edges.append(e)

e7 = e = Dep(
  source=n35,
  target=n8
);edges.append(e)

e8 = e = Dep(
  source=n37,
  target=n9
);edges.append(e)

e9 = e = Dep(
  source=n37,
  target=n9
);edges.append(e)

e10 = e = Dep(
  source=n30,
  target=n10
);edges.append(e)

e11 = e = Dep(
  source=n107,
  target=n12
);edges.append(e)

e12 = e = Dep(
  source=n169,
  target=n12
);edges.append(e)

e13 = e = Dep(
  source=n140,
  target=n13
);edges.append(e)

e14 = e = Dep(
  source=n1,
  target=n15
);edges.append(e)

e15 = e = Help(
  source=n20,
  target=n15
);edges.append(e)

e16 = e = Help(
  source=n28,
  target=n15
);edges.append(e)

e17 = e = Help(
  source=n17,
  target=n16
);edges.append(e)

e18 = e = Help(
  source=n41,
  target=n16
);edges.append(e)

e19 = e = Hurt(
  source=n33,
  target=n16
);edges.append(e)

e20 = e = Dep(
  source=n116,
  target=n17
);edges.append(e)

e21 = e = Dep(
  source=n60,
  target=n18
);edges.append(e)

e22 = e = Dep(
  source=n118,
  target=n19
);edges.append(e)

e23 = e = Dep(
  source=n88,
  target=n21
);edges.append(e)

e24 = e = Dep(
  source=n121,
  target=n22
);edges.append(e)

e25 = e = Dep(
  source=n122,
  target=n23
);edges.append(e)

e26 = e = Dep(
  source=n125,
  target=n25
);edges.append(e)

e27 = e = Dep(
  source=n126,
  target=n26
);edges.append(e)

e28 = e = Dep(
  source=n145,
  target=n29
);edges.append(e)

e29 = e = Or(
  source=n50,
  target=n29
);edges.append(e)

e30 = e = Dep(
  source=n129,
  target=n30
);edges.append(e)

e31 = e = Dep(
  source=n147,
  target=n31
);edges.append(e)

e32 = e = Dep(
  source=n148,
  target=n32
);edges.append(e)

e33 = e = Dep(
  source=n149,
  target=n33
);edges.append(e)

e34 = e = Help(
  source=n102,
  target=n35
);edges.append(e)

e35 = e = Help(
  source=n13,
  target=n36
);edges.append(e)

e36 = e = Help(
  source=n16,
  target=n36
);edges.append(e)

e37 = e = Help(
  source=n19,
  target=n36
);edges.append(e)

e38 = e = Help(
  source=n21,
  target=n36
);edges.append(e)

e39 = e = Help(
  source=n47,
  target=n36
);edges.append(e)

e40 = e = Help(
  source=n23,
  target=n36
);edges.append(e)

e41 = e = Help(
  source=n24,
  target=n36
);edges.append(e)

e42 = e = Help(
  source=n25,
  target=n36
);edges.append(e)

e43 = e = Help(
  source=n46,
  target=n36
);edges.append(e)

e44 = e = Help(
  source=n32,
  target=n36
);edges.append(e)

e45 = e = Help(
  source=n37,
  target=n36
);edges.append(e)

e46 = e = Help(
  source=n34,
  target=n36
);edges.append(e)

e47 = e = Help(
  source=n27,
  target=n37
);edges.append(e)

e48 = e = Help(
  source=n40,
  target=n37
);edges.append(e)

e49 = e = Help(
  source=n34,
  target=n37
);edges.append(e)

e50 = e = Help(
  source=n19,
  target=n38
);edges.append(e)

e51 = e = Help(
  source=n42,
  target=n38
);edges.append(e)

e52 = e = Hurt(
  source=n33,
  target=n38
);edges.append(e)

e53 = e = Help(
  source=n36,
  target=n39
);edges.append(e)

e54 = e = Dep(
  source=n142,
  target=n40
);edges.append(e)

e55 = e = Dep(
  source=n143,
  target=n41
);edges.append(e)

e56 = e = Dep(
  source=n146,
  target=n42
);edges.append(e)

e57 = e = Or(
  source=n48,
  target=n43
);edges.append(e)

e58 = e = Or(
  source=n49,
  target=n43
);edges.append(e)

e59 = e = Or(
  source=n29,
  target=n43
);edges.append(e)

e60 = e = Or(
  source=n52,
  target=n43
);edges.append(e)

e61 = e = Or(
  source=n49,
  target=n44
);edges.append(e)

e62 = e = Or(
  source=n31,
  target=n45
);edges.append(e)

e63 = e = Or(
  source=n51,
  target=n45
);edges.append(e)

e64 = e = Or(
  source=n31,
  target=n45
);edges.append(e)

e65 = e = Dep(
  source=n128,
  target=n46
);edges.append(e)

e66 = e = Dep(
  source=n80,
  target=n47
);edges.append(e)

e67 = e = Dep(
  source=n351,
  target=n47
);edges.append(e)

e68 = e = Or(
  source=n50,
  target=n48
);edges.append(e)

e69 = e = Dep(
  source=n78,
  target=n48
);edges.append(e)

e70 = e = Or(
  source=n50,
  target=n49
);edges.append(e)

e71 = e = Dep(
  source=n123,
  target=n49
);edges.append(e)

e72 = e = Dep(
  source=n11,
  target=n50
);edges.append(e)

e73 = e = Dep(
  source=n124,
  target=n51
);edges.append(e)

e74 = e = Or(
  source=n50,
  target=n52
);edges.append(e)

e75 = e = Dep(
  source=n176,
  target=n52
);edges.append(e)

e76 = e = Dep(
  source=n44,
  target=n53
);edges.append(e)

e77 = e = Dep(
  source=n36,
  target=n54
);edges.append(e)

e78 = e = Dep(
  source=n13,
  target=n55
);edges.append(e)

e79 = e = Dep(
  source=n42,
  target=n56
);edges.append(e)

e80 = e = Dep(
  source=n46,
  target=n57
);edges.append(e)

e81 = e = Dep(
  source=n30,
  target=n58
);edges.append(e)

e82 = e = Dep(
  source=n206,
  target=n59
);edges.append(e)

e83 = e = Dep(
  source=n199,
  target=n60
);edges.append(e)

e84 = e = Dep(
  source=n205,
  target=n62
);edges.append(e)

e85 = e = Dep(
  source=n200,
  target=n63
);edges.append(e)

e86 = e = Dep(
  source=n202,
  target=n65
);edges.append(e)

e87 = e = Dep(
  source=n231,
  target=n71
);edges.append(e)

e88 = e = Or(
  source=n75,
  target=n73
);edges.append(e)

e89 = e = Or(
  source=n76,
  target=n73
);edges.append(e)

e90 = e = Dep(
  source=n79,
  target=n74
);edges.append(e)

e91 = e = Dep(
  source=n83,
  target=n75
);edges.append(e)

e92 = e = Dep(
  source=n138,
  target=n76
);edges.append(e)

e93 = e = Dep(
  source=n80,
  target=n77
);edges.append(e)

e94 = e = Dep(
  source=n73,
  target=n78
);edges.append(e)

e95 = e = Dep(
  source=n275,
  target=n79
);edges.append(e)

e96 = e = Dep(
  source=n273,
  target=n80
);edges.append(e)

e97 = e = Help(
  source=n223,
  target=n81
);edges.append(e)

e98 = e = Help(
  source=n227,
  target=n81
);edges.append(e)

e99 = e = Help(
  source=n228,
  target=n81
);edges.append(e)

e100 = e = Dep(
  source=n81,
  target=n82
);edges.append(e)

e101 = e = Dep(
  source=n195,
  target=n83
);edges.append(e)

e102 = e = Dep(
  source=n195,
  target=n83
);edges.append(e)

e103 = e = Dep(
  source=n203,
  target=n85
);edges.append(e)

e104 = e = Dep(
  source=n220,
  target=n86
);edges.append(e)

e105 = e = Dep(
  source=n201,
  target=n87
);edges.append(e)

e106 = e = Dep(
  source=n218,
  target=n88
);edges.append(e)

e107 = e = Or(
  source=n90,
  target=n89
);edges.append(e)

e108 = e = Dep(
  source=n67,
  target=n90
);edges.append(e)

e109 = e = Dep(
  source=n66,
  target=n91
);edges.append(e)

e110 = e = Dep(
  source=n82,
  target=n92
);edges.append(e)

e111 = e = Dep(
  source=n84,
  target=n93
);edges.append(e)

e112 = e = Dep(
  source=n86,
  target=n95
);edges.append(e)

e113 = e = Help(
  source=n114,
  target=n95
);edges.append(e)

e114 = e = Dep(
  source=n134,
  target=n96
);edges.append(e)

e115 = e = Help(
  source=n114,
  target=n96
);edges.append(e)

e116 = e = Dep(
  source=n154,
  target=n97
);edges.append(e)

e117 = e = Hurt(
  source=n109,
  target=n98
);edges.append(e)

e118 = e = Help(
  source=n115,
  target=n99
);edges.append(e)

e119 = e = Help(
  source=n108,
  target=n99
);edges.append(e)

e120 = e = Help(
  source=n108,
  target=n99
);edges.append(e)

e121 = e = Help(
  source=n112,
  target=n100
);edges.append(e)

e122 = e = Help(
  source=n105,
  target=n100
);edges.append(e)

e123 = e = Dep(
  source=n137,
  target=n101
);edges.append(e)

e124 = e = Dep(
  source=n114,
  target=n103
);edges.append(e)

e125 = e = Dep(
  source=n119,
  target=n105
);edges.append(e)

e126 = e = Help(
  source=n94,
  target=n105
);edges.append(e)

e127 = e = Dep(
  source=n133,
  target=n106
);edges.append(e)

e128 = e = Dep(
  source=n87,
  target=n107
);edges.append(e)

e129 = e = Help(
  source=n89,
  target=n107
);edges.append(e)

e130 = e = Help(
  source=n92,
  target=n108
);edges.append(e)

e131 = e = Make(
  source=n114,
  target=n108
);edges.append(e)

e132 = e = Or(
  source=n111,
  target=n109
);edges.append(e)

e133 = e = Or(
  source=n113,
  target=n109
);edges.append(e)

e134 = e = Or(
  source=n97,
  target=n109
);edges.append(e)

e135 = e = Dep(
  source=n83,
  target=n111
);edges.append(e)

e136 = e = Dep(
  source=n83,
  target=n111
);edges.append(e)

e137 = e = Dep(
  source=n68,
  target=n113
);edges.append(e)

e138 = e = Dep(
  source=n132,
  target=n114
);edges.append(e)

e139 = e = Dep(
  source=n85,
  target=n115
);edges.append(e)

e140 = e = Dep(
  source=n106,
  target=n116
);edges.append(e)

e141 = e = Dep(
  source=n77,
  target=n117
);edges.append(e)

e142 = e = Dep(
  source=n104,
  target=n118
);edges.append(e)

e143 = e = Dep(
  source=n20,
  target=n119
);edges.append(e)

e144 = e = Dep(
  source=n103,
  target=n120
);edges.append(e)

e145 = e = Dep(
  source=n102,
  target=n121
);edges.append(e)

e146 = e = Dep(
  source=n101,
  target=n122
);edges.append(e)

e147 = e = Dep(
  source=n109,
  target=n123
);edges.append(e)

e148 = e = Dep(
  source=n89,
  target=n124
);edges.append(e)

e149 = e = Dep(
  source=n100,
  target=n125
);edges.append(e)

e150 = e = Dep(
  source=n99,
  target=n126
);edges.append(e)

e151 = e = Dep(
  source=n27,
  target=n127
);edges.append(e)

e152 = e = Dep(
  source=n74,
  target=n128
);edges.append(e)

e153 = e = Dep(
  source=n98,
  target=n129
);edges.append(e)

e154 = e = Dep(
  source=n196,
  target=n130
);edges.append(e)

e155 = e = Dep(
  source=n244,
  target=n131
);edges.append(e)

e156 = e = Dep(
  source=n276,
  target=n133
);edges.append(e)

e157 = e = Dep(
  source=n194,
  target=n133
);edges.append(e)

e158 = e = Dep(
  source=n217,
  target=n134
);edges.append(e)

e159 = e = Dep(
  source=n221,
  target=n135
);edges.append(e)

e160 = e = Dep(
  source=n219,
  target=n136
);edges.append(e)

e161 = e = Dep(
  source=n215,
  target=n137
);edges.append(e)

e162 = e = Dep(
  source=n296,
  target=n137
);edges.append(e)

e163 = e = Dep(
  source=n278,
  target=n138
);edges.append(e)

e164 = e = Dep(
  source=n291,
  target=n139
);edges.append(e)

e165 = e = Dep(
  source=n160,
  target=n140
);edges.append(e)

e166 = e = Dep(
  source=n28,
  target=n141
);edges.append(e)

e167 = e = Dep(
  source=n171,
  target=n142
);edges.append(e)

e168 = e = Dep(
  source=n165,
  target=n143
);edges.append(e)

e169 = e = Dep(
  source=n172,
  target=n145
);edges.append(e)

e170 = e = Dep(
  source=n170,
  target=n146
);edges.append(e)

e171 = e = Dep(
  source=n168,
  target=n147
);edges.append(e)

e172 = e = Dep(
  source=n41,
  target=n150
);edges.append(e)

e173 = e = Dep(
  source=n290,
  target=n151
);edges.append(e)

e174 = e = Dep(
  source=n289,
  target=n152
);edges.append(e)

e175 = e = Dep(
  source=n292,
  target=n152
);edges.append(e)

e176 = e = Dep(
  source=n284,
  target=n153
);edges.append(e)

e177 = e = Dep(
  source=n294,
  target=n153
);edges.append(e)

e178 = e = Dep(
  source=n295,
  target=n154
);edges.append(e)

e179 = e = Dep(
  source=n287,
  target=n155
);edges.append(e)

e180 = e = Dep(
  source=n286,
  target=n157
);edges.append(e)

e181 = e = Dep(
  source=n293,
  target=n158
);edges.append(e)

e182 = e = Dep(
  source=n167,
  target=n159
);edges.append(e)

e183 = e = Help(
  source=n172,
  target=n160
);edges.append(e)

e184 = e = Dep(
  source=n141,
  target=n161
);edges.append(e)

e185 = e = Make(
  source=n172,
  target=n162
);edges.append(e)

e186 = e = Dep(
  source=n132,
  target=n163
);edges.append(e)

e187 = e = Dep(
  source=n138,
  target=n164
);edges.append(e)

e188 = e = Break(
  source=n173,
  target=n165
);edges.append(e)

e189 = e = Dep(
  source=n151,
  target=n165
);edges.append(e)

e190 = e = Dep(
  source=n155,
  target=n166
);edges.append(e)

e191 = e = Help(
  source=n163,
  target=n167
);edges.append(e)

e192 = e = Help(
  source=n161,
  target=n167
);edges.append(e)

e193 = e = Dep(
  source=n70,
  target=n168
);edges.append(e)

e194 = e = Help(
  source=n168,
  target=n169
);edges.append(e)

e195 = e = Hurt(
  source=n173,
  target=n170
);edges.append(e)

e196 = e = Hurt(
  source=n167,
  target=n171
);edges.append(e)

e197 = e = Or(
  source=n164,
  target=n172
);edges.append(e)

e198 = e = Or(
  source=n166,
  target=n172
);edges.append(e)

e199 = e = Dep(
  source=n69,
  target=n174
);edges.append(e)