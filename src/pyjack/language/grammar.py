from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from parsimonious.grammar import Grammar

definition = """
  program = (nl* stmt (nl+ stmt)* nl*)
  stmt = comment / ((eq / expr ) sc)
  comment = (hash space all)
  all = ~r".+"
  eq = obj_eq / dec_eq / var_eq
  var_eq = var_lhs space* eq_sign space* var_rhs
  var_lhs = token
  var_rhs = operated
  obj_eq = obj_lhs space* eq_sign space* obj_rhs
  obj_lhs = direction space+ token
  obj_rhs = func_call
  dec_eq = dec_lhs space* eq_sign space* dec_rhs
  dec_lhs = Decision space* token
  dec_rhs = term space* dec_rhs1*
  dec_rhs1 = space* "," space* term
  expr = model / samples
  samples = ("Samples" space* number)
  model = ("Model" space token)
  term = func_call / number_token / bracketed
  bracketed = '(' space* operated space* ')'
  operated = term operated1*
  operated1 = space* operator space* term
  func_call = token space* '(' args ')'
  args = number_token space* args1*
  args1 = ',' space* number_token
  decision_args = term space* (',' space* term)*
  mul_div = "*" / "/"
  add_sub = "+" / "-"
  operator = "+" / "-" / "*" / "/"
  Decision = "Decision"
  direction = "Max" / "Min"
  number_token = number / token
  sign = "+" / "-"
  number = sign? space* int ("." int)?
  int = ~r"[0-9]+"
  token = ~r"[a-zA-Z0-9]+"
  eq_sign = "="
  nl = "\\n"
  space = ~r" +"
  hash = "#"
  sc = ";"
"""

grammar = Grammar(definition)