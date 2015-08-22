```python
import random

t=True
f=False
any=random.choose
anything = lambda:  any([t,f])
def shuffle(lst):
   random.shuffle(lst)
   return lst
   
class graph:
   def __init__(i):
     i.nodes,i.arcs={},{}
   def node(i,name,type):
     i.nodes[name] = node(name,type)
   def edge(i,from,to,type):
     assert from in i.nodes
     assert to   in i.nodes
     
     from, to = i.nodes[from], i.nodes[to]
     edge = arc(from,to,type)
     key = (from.name, to.name)
     i.arcs[key]   = i.args.get(key,[]) + [edge]
     to.kids      += [edge]
     from.parents += [edge]
     
class node:
   def __init__(i,name,type="or"):
     i.name, i.type = name, type
     i.value = None
     i.kids  = []
     i.parents = []
   def leaf(i): return not i.kids
   def root(i): return not i.parents
   
class arc:
   def __init__(i,from,to,type="makes"):
     i.from,i.to,i.type = from, to, type
   def negative(i):
     return i.type == "breaks" or i.type=="hurst"
   def positive(i):
     return not i.negative(i)

def scores(g,n=1000,seed=None):
   if seed: 
      random.seed(seed)
   roots = [node in g.nodes.values if node.root]
   for _ in xrange(n):
       final += score(g,roots)
   return final/n

def score(g,roots):
  for node in shuffle(roots):
      if val(node)== t
        count += 1
  return count

def val(x):
  if not x.value:
         if  not x.kids: 
            x.value = anything()
         else: 
            x.value = valDown(x,g) if x.type == 'and' else valUp(x,g)
  return x.value

def valDown(x,g):
   "in the style of fuzzy logic, reason pessimisticaly about ands"
   # just reflect on the arvs to kids that are true
   kids = shuffle([kid for kid in shuffle(x.kids) if  val(kid)])
   arcs = [ arc for arc in g.arcs(kid.name, x.name) for kid in kids]
   negs = [ arc for arc in arcs in arg.negative()]
   pos =  [ arc for arc in arcs in arg.positive()]
   if  not pos
      oracle= any(arcs)
      return f if oracle.type=="breaks"  else anything()
   elif:  not negs
      oracle= any(activeArcs)
      return t if oracle.type=="makes"  else anything()
   else:
      return anything()

def valUp(x,g):
   "in the style of fuzzy logic, reason optimisitically about ors"       
   for kid in shuffle(x.kids):
      if val(kid) then 
         arc = g.arcs((kid.name,x.name)) 
         if arc.positive()
            return t
  return f
```   
