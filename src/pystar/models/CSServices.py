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
  "Maintain Phone Resources",
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
  "Avoid Bad Advice [Kids]"
);nodes.append(n)

n138 = n = Task(
  "Maintain CS Phone Services",
  container = "CS Phone Services"
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
  "Anonymity[Kids]",
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