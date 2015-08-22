```python
#### standard support stuff

#imports
import random

# globals
t=True
f=False 

# one-liners
def anything()  : return random.choice([t,f])
def shuffle(lst): random.shuffle(lst); return lst

#### classes
class graph:
   "graphcs have arcs and nodes"
   def __init__(i):
     i.nodes,i.arcs={},{}
   def node(i,name,type):
     i.nodes[name] = node(name,type)
   def edge(i,froms,to,type):
     assert from in i.nodes
     assert to   in i.nodes
     froms, to = i.nodes[froms], i.nodes[to]
     edge = arc(froms,to,type)
     key = (froms.name, to.name)
     i.arcs[key]   = i.args.get(key,[]) + [edge]
     to.kids      += [edge]
     from.parents += [edge]
     
class node:
   "nodes are 'ands' or 'ors'"
   def __init__(i,name,type="or"):
     i.name, i.type = name, type
     i.value = None
     i.kids  = []
     i.parents = []
   def leaf(i): return not i.kids
   def root(i): return not i.parents
   
class arc:
   "arcs connect nodes"
   def __init__(i,froms,to,type="makes"):
     i.froms,i.to,i.type = froms, to, type
   def negative(i):
     return i.type == "breaks" or i.type=="hurst"
   def positive(i):
     return not i.negative(i)

#### support functions

def scores(g,n=1000,seed=None):
   "top-level driver. goal: maximize scores"
   if seed: 
      random.seed(seed)
   roots = [node in g.nodes.values if node.root]
   for _ in xrange(n):
      for node in g.nodes:
        node.value = None
       final += score(g,roots)
   return final/n

def score(g,roots):
  "count how may root nodes are covered"
  for node in shuffle(roots):
      if val(node)== t
        count += 1
  return count

def val(x):
  "If a node value is not known, compute it"
  if not x.value:
         if  not x.kids: 
            x.value = anything()
         else: 
            x.value = valAnd(x,g) if x.type == 'and' else valOr(x,g)
  return x.value

def valAnd(x,g):
   "reason pessimisticaly about ands"
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
      
def valOr(x,g):
   "reason optimisitically about ors"       
   for kid in shuffle(x.kids):
      if val(kid) then 
         arc = g.arcs((kid.name,x.name)) 
         if arc.positive()
            return t
  return f
```   
