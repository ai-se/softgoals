from __future__ import print_function
__author__ = 'george'
import os
from models.model import Model
from utilities.de import DE
from utilities.plotter import plot_clusters, bar_plot
from utilities.genic import Genic

def process_OOD(file_name):
  name = os.path.basename(file_name).split(".")[0]
  print("### " + name)
  print("```")
  model = Model(file_name)
  de = DE(model)
  stat = de.run()
  print("Time Taken : ", stat.runtime)
  stat.tiles()
  objs = stat.spit_objectives()
  headers = [obj.__name__.split("_")[-1] for obj in de.settings.obj_funcs]
  cluster_input = [headers] + objs
  g = Genic(k=3)
  g.run(cluster_input)
  g.report()
  clusters = g.assign_clusters(objs)
  try:
    plot_clusters(clusters,
                fig_name="img/"+name,
                col_names=headers, colors=["red", "blue", "green"],
                s=50, edgecolors='none')
  except RuntimeError as e:
    if e[0] == 500:
      print(e[1])
    else:
      raise Exception(e)
  print("```")
  return stat.runtime


def process_Visio(file_name):
  from parser.VisioTree import VisioParser
  parser = VisioParser(file_name)
  parser.parse()

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
  #         raise Exception()
  #     print("")
  # x=times
  # bar_plot(x, 'img/runtimes.png')
  test_ome_tree()
  #test_visio_tree()

