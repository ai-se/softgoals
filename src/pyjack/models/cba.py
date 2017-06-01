from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from pyjack.template import *
from pyjack.utils import *
from pyjack.distribution import *
from pyjack.functions import evaluations
import operator

__author__ = "bigfatnoob"

sample_size = 10
m = Model("cba", sample_size)

o1 = m.objective(MAXIMIZE, evaluations["EV"](), "ENB")
o2 = m.objective(MINIMIZE, evaluations["STD"](), "LP")

Benefit = m.decision({
  "As-is" : m.input(NormalCI(1, 9), "a1"),
  "Refactoring": m.input(NormalCI(0.9, 1.1), "r1")
}, "Benefit")

Cost = m.decision({
  "As-is" : m.input(NormalCI(1, 5), "a2"),
  "Refactoring": m.input(NormalCI(0, 0), "r2")
}, "Cost")

NB = m.variable("nb")
m.add_edge(Benefit, NB, operator.sub)
m.add_edge(Cost, NB, operator.sub)

m.add_edge(NB, o1)
m.add_edge(NB, o2)

## TEST
# o1.dfs()
# o1.bfs()

# o1.bfs()
m.test()
