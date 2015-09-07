__author__ = 'george'
from parser.OMETree import *


def test_ome_tree():
  parser = Parser('../GMRepo/CMA12/bCMS_SR_bCMS_AuthenticationVariation.ood')
  parser.parse()
  parser.dump_json("tmp.json")

if __name__ == "__main__":
  test_ome_tree()

