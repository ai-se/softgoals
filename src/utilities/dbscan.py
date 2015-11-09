from __future__ import print_function, division
__author__ = 'george'
from lib import *
from sklearn.cluster import DBSCAN as dbscan

class DBSCAN(O):
  """
  class DB-Scan
  """
  def __init__(self, **settings):
    O.__init__(self)
    self.settings = DBSCAN.default_settings(**settings)
    self.names = {}
    self.index = {}
    self.centroids = []

  @staticmethod
  def default_settings(**settings):
    return O(
      name = "DB-Scan",
      eps = 1,
      min_pts = 3,
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
    settings = self.settings
    print(settings)
    cl = dbscan(eps=settings.eps, min_samples=settings.min_pts, algorithm="brute")
    y = cl.fit_predict(x)
    clusters = {}
    for x_i, y_i in zip(x, y):
      clusters[y_i] = clusters.get(y_i, []) + [x_i]
    return clusters
