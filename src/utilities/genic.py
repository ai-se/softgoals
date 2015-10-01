"""
Genic is a clusterer that allows you to stream data and then cluster it
"""
from __future__ import print_function, division
__author__ = 'george'
import sys
from lib import *

class Genic(O):
  """
  Class Genic
  """
  def __init__(self, **settings):
    """
    Initialize with settings and overloads
    """
    O.__init__(self)
    self.settings = Genic.default_settings(**settings)
    self.names = {}
    self.index = {}
    self.maxs = {}
    self.mins = {}
    self.centroids = []


  @staticmethod
  def default_settings(**settings):
    """

    """
    s = O(
      k = 10,
      era = 1000,
      buffer = 500,
      prune_size = 10,
      seed = 1,
      verbose = True,
      src = "array"
    ).update(**settings)
    return s

  def header(self, row):
    for i, col in enumerate(row):
      self.names[i] = col
      self.index[col] = i


  def update_meta(self, row):
    for i, val in enumerate(row):
      self.mins[i] = min(val, self.mins.get(i, val))
      self.maxs[i] = max(val, self.maxs.get(i, val))


  def table(self, src):
    """
    Create table
    """
    def load_data():
      if self.settings.src == "array":
        for i, line in enumerate(src):
          yield i, line
      elif self.settings.src == "file":
        with open(src, 'r') as fl:
          i=0
          for line in fl:
            yield i, line
            i+=1

    def chunks():
      chunk = []
      for i, line in load_data():
        if i == 0:
          self.header(line)
        else:
          chunk.append(line)
          if len(chunk) > self.settings.buffer:
            yield chunk
            chunk = []
      if chunk:
        yield chunk

    for batch in chunks():
      index = 0
      for row in shuffle(batch):
        self.update_meta(row)
        yield index, row
        index+=1

  def more_centroids(self, n, row):
    """
    Add more centroids
    :param n: Index of the row
    :param row: Row to be added
    """
    self.centroids.append((1, 1, n, row))

  def nearest_cluster(self, row):
    """
    Return nearest cluster
    to a row
    :param row:
    :return:
    """
    def norm(val, col):
      lo, hi = self.mins[col], self.maxs[col]
      return (val - lo) / (hi - lo + 0.00001)

    def dist(cent):
      n, d = 0, 0
      for i, val in enumerate(row):
        n1, n2 = norm(val, i), norm(cent[i], i)
        d += (n1 - n2)**2
        n += 1
      return (d/n)**0.5

    d_lo, closest = sys.maxint, None
    for index, (_, _, _, centroid) in enumerate(self.centroids):
      di = dist(centroid)
      if di < d_lo:
        d_lo = di
        closest = index
    return closest


  def update_clusters(self, row):
    index = self.nearest_cluster(row)
    u0, u, dob, old = self.centroids[index]
    u1 = 1
    out = [None]*len(old)
    for i, (old_val, row_val) in enumerate(zip(old, row)):
      out[i] = (u0*old_val + u1*row_val)/(u0 + u1)
    self.centroids[index] = (u0+u1, u+u1, dob, out)

  def prune_size(self):
      return self.settings.era/self.settings.k/2

  def prune_clusters(self, n):
    """
    Prune the smallest cluster
    :param n: Row id where pruning was initiated
    :return: pruned set of clusters
    """
    b4 = len(self.centroids)
    self.centroids = [(1, u, dob, centroid) for u0, u, dob, centroid in self.centroids
                       if u0 > self.prune_size()]
    if self.settings.verbose:
      print("at n=%s, pruning %s%% of clusters" % (
         n,  int(100*(b4 - len(self.centroids))/b4)))

  def run(self, src):
    seed(self.settings.seed)
    for n, row in self.table(src):
      if len(self.centroids) < self.settings.k:
        self.more_centroids(n, row)
      else:
        self.update_clusters(row)
        if n % self.settings.era == 0:
          self.prune_clusters(n)
    return sorted(self.centroids, reverse=True)

  @staticmethod
  def round_row(row, precision = 3):
    for col,val in enumerate(row):
      if isinstance(val,float):
        val = round(val,precision)
      row[col] = val
    return row

  def report(self):
    clusters = sorted(self.centroids, reverse=True)
    header = sorted(self.index, key=self.index.get)
    matrix = [['cluster_id','caughtLast',
              'caughtAll','dob']+header]
    caught=0
    for m,(u0,u,dob,centroid) in enumerate(clusters):
      caught += u0
      matrix += [[m,u0,u,dob] + Genic.round_row(centroid, 2)]
    print("Cluster Settings: ", self.settings)
    print("")
    printm(matrix)

  def assign_clusters(self, points):
    """
    For each point in points find the
    nearest cluster and create a map of
    cluster id and list of points in it
    :param points: List of points
    :return: Map of cluster id and points in it.
    """
    clusters = {}
    for point in points:
      nearest = self.nearest_cluster(point)
      clusters[nearest] = clusters.get(nearest, []) + [point]
    return clusters