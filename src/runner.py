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
  from utilities.genic import Genic
  model = Model('../GMRepo/CMA12/bCMS_SR_bCMS_exceptional.ood')
  de = DE(model)
  objs = de.run().spit_objectives()
  headers = [obj.__name__.split("_")[-1] for obj in de.settings.obj_funcs]
  cluster_input = [headers] + objs
  g = Genic(k=3)
  g.run(cluster_input)
  g.report()


