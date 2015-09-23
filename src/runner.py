from __future__ import print_function
__author__ = 'george'
import sys
sys.path.append(".")
from models.model import Model
from utilities.de import DE

def test_ome_tree():
  model = Model('../GMRepo/CMA12/bCMS_SR_bCMS_exceptional.ood')
  print("Roots : " , len(model.roots))
  model.scores(1000,1)

if __name__ == "__main__":
  #test_ome_tree()
  # lst = []
  # decs1 = {
  #   "a" : 1,
  #   "b" : 2
  # }
  # decs2 = {
  #   "a" : 1,
  #   "b" : 2
  # }
  # pt1 = Point(decs1)
  # pt2 = Point(decs2)
  # lst.append(pt1)
  # print(pt2 in lst)
  model = Model('../GMRepo/CMA12/bCMS_SR_bCMS_exceptional.ood')
  de = DE(model)
  best = sorted(de.run(), key=lambda point: point.objectives[0],reverse=True)
  print(best[:5])


