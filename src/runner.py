from __future__ import print_function
__author__ = 'george'
import os
from models.model import Model
from utilities.de import DE
from utilities.plotter import plot_clusters, bar_plot, med_spread_plot
from utilities.genic import Genic
from utilities.kmeans import KMeans
from utilities.dbscan import DBSCAN

def process_OOD(file_name):
  name = os.path.basename(file_name).split(".")[0]
  print("### " + name)
  print("```")
  model = Model(file_name)
  de = DE(model)
  stat = de.run()
  print("Time Taken : ", stat.runtime)
  stat.tiles()
  data_map = stat.median_spread()
  objs = stat.spit_objectives()
  headers = [obj.__name__.split("_")[-1] for obj in de.settings.obj_funcs]
  cluster_input = [headers] + objs
  print("")
  #g = DBSCAN(eps=0.1, min_pts=2)
  g = KMeans(k=2)
  clusters = g.run(cluster_input)
  med_spread_plot(data_map, headers, fig_name="img/gen_"+name)
  plot_clusters(clusters,
                fig_name="img/"+name,
                col_names=headers,
                s=50, edgecolors='none')
  print("```")
  print("![1](../../src/img/gen_%s.png)"%name)
  return stat.runtime


def _test():
  meds = [31.814999999999998, 40.905, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 45.45, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55, 54.55]
  iqrs = [18.189999999999998, 9.099999999999994, 9.099999999999994, 9.099999999999994, 9.099999999999994, 9.099999999999994, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 18.189999999999998, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003, 9.090000000000003]
  data_map = {
    "meds" : meds,
    "iqrs" : iqrs
  }
  data =[data_map]*4
  med_spread_plot(data)

def process_Visio(file_name):
  from parser.VisioTree import VisioParser
  parser = VisioParser(file_name)
  parser.parse()

def test_pystar():
  from pystar.models.bCMS_SR_Witness import graph
  #print(graph.nodes)
  model = Model("", tree=graph)
  de = DE(model)
  stat = de.run()
  stat.tiles()

def test_ome_tree():
  process_OOD('../GMRepo/CMA12/bCMS_SR_bCMS_AuthenticationVariation.ood')

def test_visio_tree():
  process_Visio('../GMRepo/Counseling Service/Stage1_UnderstandingCS/XML/ParentsSD.vdx')
  #process_Visio('../GMRepo/CMA12/bCMS_SR_CommunicationCompromiser.ood')

if __name__ == "__main__":
  # directory = '../GMRepo/CMA12'
  # times = {}
  # for file_name in os.listdir(directory):
  #   if file_name.endswith(".ood"):
  #     file_name = directory + "/" + file_name
  #     name = os.path.basename(file_name).split(".")[0]
  #     try:
  #       times[name] = process_OOD(file_name)
  #     except RuntimeError as e:
  #       if e[0] == 500:
  #         print(file_name)
  #         print(e[1])
  #         print("```")
  #       else:
  #         print(e)
  #         raise Exception()
  #     print("")
  # bar_plot(times, 'img/random_runtimes.png')
  #test_ome_tree()
  #test_visio_tree()
  #_test()
  test_pystar()


