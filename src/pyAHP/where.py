from __future__ import print_function, division
import sys,os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from utilities.lib import *

__author__ = 'panzer'

def default_settings():
  return O(
    min_size = 8,
    max_depth = 10,
    prefix = "|.. "
  )


class Row(O):
  """
  Row Of a Binary Tree Node
  """
  def __init__(self, decisions):
    O.__init__(self)
    self.decisions = decisions
    self.normalized = None

class TreeNode(O):
  """
  Node of a binary Tree
  """
  id_counter = 0
  def __init__(self, rows, parent, level):
    """
    :param parent: Node's parent
    :param level: Level of a node. Starts from 0
    :return:
    """
    O.__init__(self)
    self.id = TreeNode.id_counter
    self._parent = parent
    self.level = level
    self.kids = None
    self._rows = rows
    TreeNode.id_counter += 1

  def add_kid(self, kid):
    """
    Add a child to the node
    :param kid:
    :return:
    """
    if self.kids is None:
      self.kids = []
    self.kids.append(kid)

  def get_rows(self):
    return self._rows


class Where(O):
  """
  Fastmap based clusterer
  """
  def __init__(self, rows, **settings):
    """
    :param rows: Rows to be clustered
    :param settings:
    :return:
    """
    O.__init__(self)
    self.rows = rows
    self.limits = self.set_limits()
    self.settings = default_settings().update(**settings)

  def set_limits(self):
    """
    Assign max and min values based on all the data
    :return:
    """
    maxs = [-sys.maxint]*len(self.rows[0].decisions)
    mins = [sys.maxint]*len(self.rows[0].decisions)
    for row in self.rows:
      for i, decision in enumerate(row.decisions):
        if decision > maxs[i]: maxs[i] = decision
        if decision < mins[i]: mins[i] = decision
    return O(maxs = maxs, mins = mins)

  def too_deep(self, level):
    """
    Check if the tree is too deep
    :param level:
    :return:
    """
    return level > self.settings.max_depth

  def too_few(self, rows):
    """
    Check if a cluster contains the minimal rows
    :param rows:
    :return:
    """
    return len(rows) < self.settings.min_size

  def get_furthest(self, row, rows):
    """
    Get furthest row from a set of rows wrt a current row
    :param row:
    :param rows:
    :return:
    """
    furthest, dist = None, 0
    for one in rows:
      if row.id == one.id: continue
      tmp = self.euclidean(row, one)
      if tmp > dist:
        furthest, dist = one, dist
    return furthest

  def euclidean(self, one, two):
    """
    Compute Euclidean distance
    :param one:
    :param two:
    :return:
    """
    one_normalized = self.normalize(one)
    two_normalized = self.normalize(two)
    dist = 0
    for one_i, two_i in zip(one_normalized, two_normalized):
      dist += (one_i - two_i) ** 2
    return dist

  def normalize(self, one):
    """
    Normalize row
    :param one:
    :return:
    """
    if one.normalized is None:
      normalized = []
      for i, decision in enumerate(one.decisions):
        if self.limits.mins[i] == self.limits.maxs[i]:
          value = 0
        else:
          value = (decision - self.limits.mins[i]) / (self.limits.maxs[i] - self.limits.mins[i])
        normalized.append(value)
      one.normalized = normalized
    return one.normalized

  def get_furthest2(self, rows):
    """
    Get furthest extreme rows from a list of rows
    :param rows:
    :return:
    """
    east, west, dist = None, None, -1
    for i in range(len(rows)-1):
      for j in range(i+1, len(rows)):
        temp_dist = self.euclidean(rows[i], rows[j])
        if temp_dist > dist:
          east, west, dist = rows[i], rows[j], temp_dist
    return east, west

  def fastmap(self, node):
    """
    Fastmap projection
    :param node:
    :return:
    """
    def second(iterable): return iterable[1]
    rows = shuffle(node.get_rows())
    east, west = self.get_furthest2(rows)
    c = self.euclidean(east, west)
    lst = []
    for one in rows:
      a = self.euclidean(one, west)
      b = self.euclidean(one, east)
      if c == 0:
        x = 0
      else:
        x = (a**2 + c**2 - b**2)/(2*c)
      lst += [(x, one)]
    lst = sorted(lst)
    mid = len(lst)//2
    wests = map(second, lst[:mid])
    easts = map(second, lst[mid:])
    west = wests[0]
    east = easts[-1]
    return wests, west, easts, east

  def show(self, rows, node, level, has_kids = True):
    """
    Print Node
    :param rows:
    :param node:
    :param level:
    :param has_kids:
    :return:
    """
    if not has_kids:
      print(self.settings.prefix*level, len(rows), ' ; ', node.id)
    else:
      print(self.settings.prefix*level, len(rows))

  def cluster(self, rows = None, level = 0, parent = None, verbose = False):
    """
    Cluster rows
    :param rows:
    :param level:
    :param parent:
    :param verbose:
    :return:
    """
    if rows is None:
      rows = self.rows
    node = TreeNode(rows, parent, level)
    if not self.too_deep(level) and not self.too_few(rows):
      if verbose: self.show(rows, node, level, has_kids=True)
      wests, west, easts, east = self.fastmap(node)
      node.west, node.east = west, east
      node.add_kid(self.cluster(wests, level=level+1, parent=node, verbose=verbose))
      node.add_kid(self.cluster(easts, level=level+1, parent=node, verbose=verbose))
    else:
      if verbose: self.show(rows, node, level, has_kids=False)
      east, west = self.get_furthest2(rows)
      node.west, node.east = west, east
    return node




