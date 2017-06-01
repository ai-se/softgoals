from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from pyjack.language.grammar import grammar
from parsimonious.nodes import NodeVisitor
from pyjack.template import Model, O, Decision
from pyjack.utils import MAXIMIZE, MINIMIZE
from pyjack.functions import evaluations, distributions, operations

_max = "Max"
_min = "Min"

class Parser(NodeVisitor):
  def __init__(self, content):
    self.model = None
    self.uninitialized_variables = {}
    self.initialized_variables= {}
    self._content = content

  def process(self):
    ast = grammar.parse(self._content)
    self.visit(ast)
    self.check_undeclared()
    self.update_children()
    return self.model

  def check_undeclared(self):
    if len(self.uninitialized_variables) > 0:
      raise Exception("Uninitialized variables: %s" % self.uninitialized_variables.keys())

  def update_children(self):
    for node_id, node in self.model.nodes.items():
      if isinstance(node, Decision):
        node.options = {child:self.initialized_variables[child] for child in node.children}
      node.children = [self.initialized_variables[child] for child in node.children]
    for node_id, node in self.model.nodes.items():
      self.model.node_edges(node)

  def visit_stmt(self, node, vc):
    pass

  def visit_model(self, node, _):
    name = node.children[-1].text
    self.model = Model(name)

  def visit_samples(self, node, _):
    samples = int(node.children[-1].text)
    self.model.sample_size = samples

  def visit_comment(self, node, vc):
    pass

  def visit_eq(self, node, vc):
    pass

  def visit_var_lhs(self, node, _):
    name = node.text
    self.uninitialized_variables[name] = None
    return name

  def visit_obj_eq(self, _, vc):
    lhs = vc[0]
    rhs = vc[-1]
    args = rhs.args[1:]
    lhs.eval = evaluations[rhs.name](*args)
    lhs.children.append(rhs.args[0])
    del self.uninitialized_variables[lhs.name]
    self.initialized_variables[lhs.name] = lhs

  def visit_obj_lhs(self, node, _):
    direction = MAXIMIZE if node.children[0].text == _max else MINIMIZE
    name = node.children[-1].text
    obj = self.model.objective(direction, name=name)
    self.uninitialized_variables[name] = obj
    return obj

  def visit_dec_eq(self, _, vc):
    lhs = vc[0]
    rhs = vc[-1]
    lhs.children = rhs
    del self.uninitialized_variables[lhs.name]
    self.initialized_variables[lhs.name] = lhs

  def visit_dec_lhs(self, _, vc):
    name = vc[-1]
    dec = self.model.decision({}, name=name)
    self.uninitialized_variables[name] = dec
    return dec

  @staticmethod
  def visit_dec_rhs(_, vc):
    args = [vc[0]]
    if vc[-1]:
      args += vc[-1]
    return args

  @staticmethod
  def visit_dec_rhs1(_, vc):
    return vc[-1]

  def visit_var_eq(self, node, vc):
    lhs = vc[0]
    rhs = vc[-1]
    if rhs in self.initialized_variables:
      rhs_node = self.initialized_variables.pop(rhs)
      rhs_node.name = lhs
      if lhs in self.uninitialized_variables:
        del self.uninitialized_variables[lhs]
      self.initialized_variables[rhs_node.name] = rhs_node
    else:
      raise Exception("Not supporting direct assignment. Statement = %s" % node.text)

  def visit_term(self, _, vc):
    term = vc[0]
    if isinstance(term, O) and term.type == "function":
      inp = self.model.input(distributions[term.name](*term.args))
      inp.name = "%s_%d" % (term.name, inp.id)
      self.initialized_variables[inp.name] = inp
      return inp.name
    elif isinstance(term, str):
      if term not in self.initialized_variables:
        self.uninitialized_variables[term] = None
      return term
    elif isinstance(term, float):
      inp = self.model.input(distributions["constant"](term))
      inp.name = "constant%0.2f_%d" % (term, inp.id)
      self.initialized_variables[inp.name] = inp
      return inp.name
    elif isinstance(term, O) and term.type == "bracketed":
      return term.name

  @staticmethod
  def visit_bracketed(_, vc):
    return O(name=vc[2], type="bracketed")

  def visit_operated(self, _, vc):
    if vc[-1] is None:
      return vc[0]
    else:
      ops = set([o.operation for o in vc[-1]])
      if len(ops) > 1:
        raise Exception("Multiple operations not allowed: % s" % operations)
      op = operations[ops.pop()]
      nodes = [vc[0]] + [o.term for o in vc[-1]]
      var = self.model.variable()
      var.name = "variable_%d" % var.id
      var.operation = op
      for n in nodes:
        if n not in self.initialized_variables:
          self.uninitialized_variables[n] = None
        var.children.append(n)
      self.initialized_variables[var.name] = var
      return var.name

  @staticmethod
  def visit_operated1(_, vc):
    operation = vc[1]
    term = vc[-1]
    return O(operation=operation, term=term, type="operated")

  @staticmethod
  def visit_operator(node, _):
    return node.text

  @staticmethod
  def visit_func_call(_, vc):
    name = vc[0]
    args = vc[-2]
    return O(name=name, args=args, type="function")

  @staticmethod
  def visit_args(_, vc):
    args = [vc[0]]
    if vc[-1]:
      args += vc[-1]
    return args

  @staticmethod
  def visit_args1(_, vc):
    return vc[-1]

  @staticmethod
  def visit_number_token(_, vc):
    return vc[0]

  @staticmethod
  def visit_add(_, vc):
    num = vc[0]
    if vc[-1]:
      op = vc[-1][0].operation
      val = vc[-1][0].value
      num = eval("%f %s %f" % (num, op, val))
    return num

  @staticmethod
  def visit_add1(_, vc):
    return O(operation=vc[0], value=vc[-1])

  @staticmethod
  def visit_mul(_, vc):
    num = vc[0]
    if vc[-1]:
      op = vc[-1][0].operation
      val = vc[-1][0].value
      num = eval("%f %s %f" % (num, op, val))
    return num

  @staticmethod
  def visit_mul1(_, vc):
    return O(operation=vc[0], value=vc[-1])

  @staticmethod
  def visit_add_sub(node, _):
    return node.text

  @staticmethod
  def visit_mul_div(node, _):
    return node.text

  @staticmethod
  def visit_expo(_, vc):
    num = vc[0]
    if vc[-1]:
      num = num ** vc[-1][0]
    return num

  @staticmethod
  def visit_expo1(_, vc):
    return vc[-1]

  @staticmethod
  def visit_number(_, vc):
    return vc[0]

  @staticmethod
  def visit_bracket_number(_, vc):
    return vc[2]

  @staticmethod
  def visit_float(node, _):
    return float(node.text)

  @staticmethod
  def visit_token(node, _):
    return node.text.strip()

  def generic_visit(self, node, vc):
    if vc:
      return vc
    return None

  @staticmethod
  def from_file(file_name):
    with open(file_name) as f:
      s = f.read()
      return Parser(s).process()

_text = """
Model mdl;
Samples 1000;
Max o1 = EV(v1, 10 ^ (1 + 2));
Decision d = uniform(0, 1) , x2 , 100, (z3 + z4 + 60);
v1 = d * v2;
x2 = triangular(0, 0.5, 1);
z3 = normalCI(0, 10);
z4 = 50;
v2 = 1.2;
x1 = 5 + 6.6;
"""

if __name__ == "__main__":
  print("Method 1")
  fdm = Parser.from_file("pyjack/models/fdm.str")
  fdm.test()
  print("Method 2")
  import pyjack.models.fdm
  # mdl = Parser(_text).process()
  # mdl.test()
