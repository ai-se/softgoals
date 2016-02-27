from __future__ import print_function
__author__ = 'george'
import os, sys
from models.model import Model
from pystar.model import Model as Py_Model
from utilities.de import DE
from utilities.plotter import plot_clusters, bar_plot, med_spread_plot
from utilities.kmeans import KMeans

def process_ood(file_name):
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


def process_visio(file_name):
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
  last_gen = stat.generations[-1]
  maxs = [-1]*len(last_gen[0].objectives)
  bests = [None]*len(last_gen[0].objectives)
  for point in last_gen:
    for i in range(len(maxs)):
      if point.objectives[i] > maxs[i]:
        maxs[i] = point.objectives[i]
        bests[i] = point
  print(maxs)
  columns = ["id", "type", "value", "is_random", "name"]
  stat.tabulate(columns, bests[0])


def test_ome_tree():
  process_ood('../GMRepo/CMA12/bCMS_SR_Witness.ood')

def test_visio_tree():
  process_visio('../GMRepo/Counseling Service/Stage1_UnderstandingCS/XML/ParentsSD.vdx')
  #process_visio('../GMRepo/CMA12/bCMS_SR_CommunicationCompromiser.ood')


def test_ome_trees():
  directory = '../GMRepo/CMA12'
  times = {}
  for file_name in os.listdir(directory):
    if file_name.endswith(".ood"):
      dir_file_name = directory + "/" + file_name
      name = os.path.basename(dir_file_name).split(".")[0]
      try:
        times[name] = process_ood(dir_file_name)
      except RuntimeError as e:
        if e[0] == 500:
          print(dir_file_name)
          print(e[1])
          print("```")
        else:
          print(e)
          raise Exception()
      print("")
  bar_plot(times, 'img/random_runtimes.png')

def test_star1(model_name, show_optimal_index = True):
  from pystar.models.dot_models import modelers, optimal_indices
  from star1 import star1
  for model in modelers:
    if model.__name__ == model_name:
      optimal_index = optimal_indices.get(model_name, None) if show_optimal_index else None
      star1.run(model(), SUB_FOLDER, optimal_index=optimal_index)


def main():
  # test_ome_trees()
  # #test_ome_tree()
  # # #test_visio_tree()
  #test_pystar()
  args = sys.argv
  if len(args) <= 2:
    print("Invalid args")
    exit()
  show_optimal_index = True if args[2] is not None and args[2] == 'y' else False
  test_star1(args[1], show_optimal_index)
  #_test()

SUB_FOLDER = "induced_softgoals"

if __name__ == "__main__":
  main()




