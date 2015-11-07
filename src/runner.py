from __future__ import print_function
__author__ = 'george'
import os
from models.model import Model
from utilities.de import DE
from utilities.plotter import plot_clusters, bar_plot, med_spread_plot
from utilities.kmeans import KMeans

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
  g = KMeans(k=2)
  clusters = g.run(cluster_input)
  med_spread_plot(data_map, headers, fig_name="img/gen_bin_"+name)
  plot_clusters(clusters,
                fig_name="img/bin_"+name,
                col_names=headers,
                s=50, edgecolors='none')
  print("```")
  print("![1](../../src/img/gen_bin_%s.png)"%name)
  return stat.runtime


def process_Visio(file_name):
  from parser.VisioTree import VisioParser
  parser = VisioParser(file_name)
  parser.parse()

def test_pystar():
  from pystar.models.CSServices import graph
  from pystar.model import Model
  #print(graph.nodes)
  model = Model(graph)
  de = DE(model)
  stat = de.run()
  stat.tiles()
  lastgen = stat.generations[-1]
  maxs = [-1]*len(lastgen[0].objectives)
  bests = [None]*len(lastgen[0].objectives)
  for point in lastgen:
    for i in range(len(maxs)):
      if point.objectives[i] > maxs[i]:
        maxs[i] = point.objectives[i]
        bests[i] = point
  print(maxs)
  columns = ["id", "type", "value", "is_random", "name"]
  stat.tabulate(columns, bests[0])


def test_ome_tree():
  process_OOD('../GMRepo/CMA12/bCMS_SR_Witness.ood')

def test_visio_tree():
  process_Visio('../GMRepo/Counseling Service/Stage1_UnderstandingCS/XML/ParentsSD.vdx')
  #process_Visio('../GMRepo/CMA12/bCMS_SR_CommunicationCompromiser.ood')


def test_ome_trees():
  directory = '../GMRepo/CMA12'
  times = {}
  for file_name in os.listdir(directory):
    if file_name.endswith(".ood"):
      file_name = directory + "/" + file_name
      name = os.path.basename(file_name).split(".")[0]
      try:
        times[name] = process_OOD(file_name)
      except RuntimeError as e:
        if e[0] == 500:
          print(file_name)
          print(e[1])
          print("```")
        else:
          print(e)
          raise Exception()
      print("")
  bar_plot(times, 'img/random_runtimes.png')


if __name__ == "__main__":
  # test_ome_trees()
  # #test_ome_tree()
  # # #test_visio_tree()
  from star1 import star1
  star1.run()
  #test_pystar()


