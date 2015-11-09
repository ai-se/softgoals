"""
K-means algorithm
"""
from __future__ import print_function, division
__author__ = 'george'
from lib import *
from sklearn.cluster import KMeans as km

class KMeans(O):
  """
  Class K-Means
  """
  def __init__(self, **settings):
    """
    Initaialize with settings and overrides
    :param settings: Settigns to be overridden
    """
    O.__init__(self)
    self.settings = KMeans.default_settings(**settings)
    self.names = {}
    self.index = {}
    self.centroids = []

  @staticmethod
  def default_settings(**settings):
    return O(
      name = "K-Means",
      k = "auto",
      seed = 1,
      src = "array"
    ).update(**settings)

  def header(self, row):
    for i, col in enumerate(row):
      self.names[i] = col
      self.index[col] = i

  def table(self, src):
    if self.settings.src == "array":
      self.header(src[0])
      return src[1:]
    else:
      raise RuntimeError("Have to implement for other sources")


  def run(self, src):
    x = self.table(src)
    k = self.settings.k
    if k == "auto":
      raise RuntimeError("Have to implement auto parser")
    cl = km(n_clusters=k)
    y = cl.fit_predict(x)
    clusters = {}
    for x_i, y_i in zip(x, y):
      clusters[y_i] = clusters.get(y_i, []) + [x_i]
    return clusters
