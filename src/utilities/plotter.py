from __future__ import print_function, division
from StdSuites.Type_Names_Suite import point

__author__ = 'george'

import matplotlib.pyplot as plt
import numpy as np
from lib import *


COLORS = ['indigo', 'gold', 'hotpink', 'firebrick', 'indianred', 'yellow', 'mistyrose',
          'darkolivegreen', 'olive', 'darkseagreen', 'pink', 'tomato', 'lightcoral',
          'orangered', 'navajowhite', 'lime', 'palegreen', 'greenyellow', 'burlywood',
          'seashell', 'mediumspringgreen', 'fuchsia', 'papayawhip', 'blanchedalmond',
          'chartreuse', 'dimgray', 'black', 'peachpuff', 'springgreen', 'aquamarine',
          'white', 'orange', 'lightsalmon', 'darkslategray', 'brown', 'ivory',
          'dodgerblue', 'peru', 'lawngreen', 'chocolate', 'crimson', 'forestgreen',
          'slateblue', 'lightseagreen', 'cyan', 'mintcream', 'silver', 'antiquewhite',
          'mediumorchid', 'skyblue', 'gray', 'darkturquoise', 'goldenrod', 'darkgreen',
          'floralwhite', 'darkviolet', 'darkgray', 'moccasin', 'saddlebrown', 'darkslateblue',
          'lightskyblue', 'lightpink', 'mediumvioletred', 'red', 'deeppink', 'limegreen',
          'darkmagenta', 'palegoldenrod', 'plum', 'turquoise', 'lightgoldenrodyellow',
          'darkgoldenrod', 'lavender', 'maroon', 'yellowgreen', 'sandybrown', 'thistle',
          'violet', 'navy', 'magenta', 'tan', 'rosybrown', 'olivedrab', 'blue', 'lightblue',
          'ghostwhite', 'honeydew', 'cornflowerblue', 'linen', 'darkblue', 'powderblue',
          'seagreen', 'darkkhaki', 'snow', 'sienna', 'mediumblue', 'royalblue', 'lightcyan',
          'green', 'mediumpurple', 'midnightblue', 'cornsilk', 'paleturquoise', 'bisque',
          'slategray', 'darkcyan', 'khaki', 'wheat', 'teal', 'darkorchid', 'deepskyblue',
          'salmon', 'darkred', 'steelblue', 'palevioletred', 'lightslategray', 'aliceblue',
          'lightgreen', 'orchid', 'gainsboro', 'mediumseagreen', 'lightgray', 'mediumturquoise',
          'lemonchiffon', 'cadetblue', 'lightyellow', 'lavenderblush', 'coral', 'purple',
          'aqua', 'whitesmoke', 'mediumslateblue', 'darkorange', 'mediumaquamarine',
          'darksalmon', 'beige', 'blueviolet', 'azure', 'lightsteelblue', 'oldlace']


def get_colors(n):
  return sample(COLORS, n)

def plot_clusters(clusters, fig_name="temp.png", col_names=None, colors=None, **settings):
  """
  :param clusters: Key value pair of cluster_id and points in them
  :return:
  """
  if len(clusters.values()[0][0]) != 2:
    raise Exception("Only 2 dimensional points supported")
  seed()
  if not col_names:
    col_names = ["Obj 1", "Obj 2"]
  if not colors:
    colors = get_colors(len(clusters.keys()))
  handles=[]
  size = 0
  for color, key in zip(colors, clusters.keys()):
    points = np.array(clusters.get(key))
    size += len(points)
    handles.append(plt.scatter(points[:,0], points[:,1], c=color, **settings))
  plt.xlabel(col_names[0])
  plt.ylabel(col_names[1])
  plt.legend(handles, colors)
  plt.savefig(fig_name)