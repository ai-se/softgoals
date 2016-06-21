from __future__ import print_function, division

__author__ = 'george'

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from lib import *
from mpl_toolkits.mplot3d import Axes3D


# COLORS = ['indigo', 'gold', 'hotpink', 'firebrick', 'indianred', 'yellow', 'mistyrose',
#           'darkolivegreen', 'olive', 'darkseagreen', 'pink', 'tomato', 'lightcoral',
#           'orangered', 'navajowhite', 'lime', 'palegreen', 'greenyellow', 'burlywood',
#           'seashell', 'mediumspringgreen', 'fuchsia', 'papayawhip', 'blanchedalmond',
#           'chartreuse', 'dimgray', 'black', 'peachpuff', 'springgreen', 'aquamarine',
#           'white', 'orange', 'lightsalmon', 'darkslategray', 'brown', 'ivory',
#           'dodgerblue', 'peru', 'lawngreen', 'chocolate', 'crimson', 'forestgreen',
#           'slateblue', 'lightseagreen', 'cyan', 'mintcream', 'silver', 'antiquewhite',
#           'mediumorchid', 'skyblue', 'gray', 'darkturquoise', 'goldenrod', 'darkgreen',
#           'floralwhite', 'darkviolet', 'darkgray', 'moccasin', 'saddlebrown', 'darkslateblue',
#           'lightskyblue', 'lightpink', 'mediumvioletred', 'red', 'deeppink', 'limegreen',
#           'darkmagenta', 'palegoldenrod', 'plum', 'turquoise', 'lightgoldenrodyellow',
#           'darkgoldenrod', 'lavender', 'maroon', 'yellowgreen', 'sandybrown', 'thistle',
#           'violet', 'navy', 'magenta', 'tan', 'rosybrown', 'olivedrab', 'blue', 'lightblue',
#           'ghostwhite', 'honeydew', 'cornflowerblue', 'linen', 'darkblue', 'powderblue',
#           'seagreen', 'darkkhaki', 'snow', 'sienna', 'mediumblue', 'royalblue', 'lightcyan',
#           'green', 'mediumpurple', 'midnightblue', 'cornsilk', 'paleturquoise', 'bisque',
#           'slategray', 'darkcyan', 'khaki', 'wheat', 'teal', 'darkorchid', 'deepskyblue',
#           'salmon', 'darkred', 'steelblue', 'palevioletred', 'lightslategray', 'aliceblue',
#           'lightgreen', 'orchid', 'gainsboro', 'mediumseagreen', 'lightgray', 'mediumturquoise',
#           'lemonchiffon', 'cadetblue', 'lightyellow', 'lavenderblush', 'coral', 'purple',
#           'aqua', 'whitesmoke', 'mediumslateblue', 'darkorange', 'mediumaquamarine',
#           'darksalmon', 'beige', 'blueviolet', 'azure', 'lightsteelblue', 'oldlace']

COLORS = ['red', 'darkblue', 'darkgreen', 'black', 'yellow', 'lightgreen', 'aqua', 'orange']


def get_colors(n):
  return sample(COLORS, n)

def plot_clusters(clusters, fig_name="temp.png", col_names=None, colors=None, **settings):
  """
  :param clusters: Key value pair of cluster_id and points in them
  :return:
  """
  if len(clusters.values()[0][0]) == 3:
    return plot_3d_clusters(clusters, fig_name, col_names, colors)
  elif len(clusters.values()[0][0]) != 2:
    raise RuntimeError(500, "Only 2 dimensional points supported")
  seed()
  if not col_names:
    col_names = ["Obj 1", "Obj 2"]
  if not colors:
    colors = get_colors(len(clusters.keys()))
  handles=[]
  cluster_labels = []
  size = 0
  for color, key in zip(colors, clusters.keys()):
    points = np.array(clusters.get(key))
    size += len(points)
    handles.append(plt.scatter(points[:,0], points[:,1], c=color, **settings))
    cluster_labels.append("cluster "+str(key))
  plt.xlabel(col_names[0])
  plt.ylabel(col_names[1])
  plt.legend(handles, cluster_labels)
  plt.savefig(fig_name)
  plt.clf()

def plot_3d_clusters(clusters, fig_name = "temp.png", col_names=None, colors=None, **settings):
  mins = [10**32]*3
  maxs = [-10**32]*3
  def update_limits(pts):
    for i, (less, more) in enumerate(zip(mins, maxs)):
      if min(pts[:,i]) < less : mins[i] = min(pts[:,i])
      if max(pts[:,i]) > more : maxs[i] = max(pts[:,i])

  seed()
  if not col_names:
    col_names = ["Obj 1", "Obj 2", "Obj 3"]
  if not colors:
    colors = get_colors(len(clusters.keys()))
  handles=[]
  cluster_labels = []
  fig = plt.figure()
  ax = fig.add_subplot(111, projection="3d")
  for color, key in zip(colors, clusters.keys()):
    points = np.array(clusters.get(key))
    update_limits(points)
    handles.append(
      ax.scatter(points[:,0],
                  points[:,1],
                  zs = points[:,2],
                  c=color,
                  **settings))
    cluster_labels.append("cluster "+str(key))
  ax.set_xlabel(col_names[0])
  ax.set_ylabel(col_names[1])
  ax.set_zlabel(col_names[2])
  ax.set_xlim3d(mins[0]-1, maxs[0]+1)
  ax.set_ylim3d(mins[1]-1, maxs[1]+1)
  ax.set_zlim3d(mins[2]-1, maxs[2]+1)
  plt.legend(handles, cluster_labels)
  plt.savefig(fig_name)
  plt.clf()

def bar_plot(vals, fig_name="temp.png", label=None, **settings):
  ind = np.arange(len(vals.keys()))
  width = 0.35
  fig = plt.figure()
  fig.subplots_adjust(left=0.35)
  ax = fig.add_subplot(111)
  ax.barh(ind, vals.values(), width, color='r')
  if not label:
    label = "Time (in seconds)"
  ax.set_xlabel(label)
  ax.set_ylabel("Models")
  ax.set_yticks(ind)
  ax.set_yticklabels(vals.keys())
  # We change the font size of minor ticks label
  ax.tick_params(axis='both', which='major', labelsize=8)
  ax.tick_params(axis='both', which='minor', labelsize=7)
  plt.savefig(fig_name)
  plt.clf()

def line_plot(x_axis, y_axes, fig_name="temp.png"):
  keys = y_axes.keys()
  for y_axis in y_axes.values():
    plt.plot(x_axis, y_axis)
  plt.legend(keys, loc="upper right")
  plt.xlabel("Ranked Decision")
  plt.ylabel("Score")
  plt.savefig(fig_name)

def med_spread_plot(data, obj_names, fig_name="temp.png", **settings):
  fig = plt.figure(1)
  fig.subplots_adjust(hspace=0.5)
  directory = fig_name.rsplit("/", 1)[0]
  mkdir(directory)
  for i, data_map in enumerate(data):
    meds = data_map["meds"]
    iqrs = data_map.get("iqrs", None)
    if iqrs:
      x = range(len(meds))
      index = int(str(len(data))+"1"+str(i+1))
      plt.subplot(index)
      plt.title(obj_names[i])
      plt.plot(x, meds, 'b-', x, iqrs, 'r-')
      plt.ylim((min(iqrs)-1, max(meds)+1))
    else:
      x = range(len(meds))
      index = int(str(len(data))+"1"+str(i+1))
      plt.subplot(index)
      plt.title(obj_names[i])
      plt.plot(x, meds, 'b-')
      plt.ylim((min(meds)-1, max(meds)+1))
  blue_line = mlines.Line2D([],[], color='blue', label='Median')
  red_line = mlines.Line2D([],[], color='red', label='IQR')
  plt.figlegend((blue_line, red_line), ('Median', 'IQR'), loc=9, bbox_to_anchor=(0.5, 0.075), ncol=2)
  plt.savefig(fig_name)
  plt.clf()

def point_plot(x_axis, y_axes, styles, fig_name="temp.png"):
  keys = y_axes.keys()
  y_min = sys.maxint
  y_max = -y_min
  for index, y_axis in enumerate(y_axes.values()):
    y_max = max(max(y_axis), y_max)
    y_min = min(min(y_axis), y_min)
    plt.plot(x_axis, y_axis, styles[index])
  plt.legend(keys, loc="upper left")
  plt.xlabel("Number of Decisions")
  plt.ylabel("Count")
  plt.xlim([min(x_axis)-1, max(x_axis)+1])
  plt.ylim([y_min-1, y_max+1])
  plt.savefig(fig_name)
  plt.clf()

def point_plot_3d(x_axis, y_axis, z_axis,
                  color, marker, file_name,
                  x_label, y_label, z_label):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(x_axis, y_axis, z_axis, c=color, marker=marker)
  ax.set_xlabel(x_label)
  ax.set_ylabel(y_label)
  ax.set_zlabel(z_label)
  ax.set_xlim3d(left=min(x_axis)-1, right=max(x_axis)+1)
  ax.set_ylim3d(bottom=min(y_axis)-1, top=max(y_axis)+1)
  ax.set_zlim3d(bottom=min(z_axis)-1, top=max(z_axis)+1)
  plt.savefig(file_name)
  plt.clf()