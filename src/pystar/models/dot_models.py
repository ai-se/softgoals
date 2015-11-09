__author__ = 'george'
from pystar.template import Graph

def CSServices():
  resources = ["Service Resources", "Web Server", "Feedback Form Software", "Web Software",
                 "Strategic Blue Print", "Feedback", "Web Site Content", "Phone Library of Recorded Messages",
                 "Feedback1"]
  containers = ["CS", "Fund Development and Marketing", "Provincial government",
                "CS Technology Services", "CS Service", "Web Service", "Phone Service",
                "Counselling Management", "PHL Service", "Parents", "IT Department",
                "Web Task Force", "CS Web Services", "CS Phone Services", "PHL Phone Services",
                "PHL Web Services", "Counselling", "Kids and Youth"]
  graph = Graph.from_dot("CSServices", "pystar/graphviz/CSServices.gv", resources, containers)
  Graph.json(graph, "pystar/json/%s.json"%graph.name)
  return graph

def OOOChatRooms():
  resources = []
  containers = ["CS Technology Services", "CS Service", "Web Service", "CS Web Services",
                "Counselling", "Counselling Employee", "Web Counselling"]
  graph = Graph.from_dot("OOOChatRooms", "pystar/graphviz/chat_room.gv", resources, containers)
  Graph.json(graph, "pystar/json/%s.json"%graph.name)
  return graph