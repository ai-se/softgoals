__author__ = 'george'
from parser.OMETree import *
import sys
sys.path.append("../../optima")
import utils.constants as constants

def test_ome_tree():
  parser = Parser('../GMRepo/CMA12/bCMS_SR_bCMS_AuthenticationVariation.ood')
  parser.store_json()
  parser.make_dummy_props()

if __name__ == "__main__":
  #test_ome_tree()
  print(constants.EPS)

