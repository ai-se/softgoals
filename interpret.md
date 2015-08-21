```python
def scores(softgoals):
   repeat 1000 times:
       final += score(softgoals)
   return final

def score(softgoals):
  roots =  all nodes with no parents
  for node in shuffle(roots):
      if val(node)== t
        count += 1
 return score

def val(node):
  if a node has no  value then
         if  has not childern, value= any of t,f
         else node.type = and then value = valDown(node)
                  node.tpye = or then value = valUp(node)
         node.value = value
  return node.value

def valDown(node):
   "in the style of fuzzy logic, reason pessimisticaly about ands"
         for kid in shuffle(kids):
             if val(kid) then 
                  add  (node,kid) to active
         using the  active arcs:
            if is has only negative input arcs then pick one at random:
              - if "hurts"    return any of t,f
              - if "breaks"   return  f 
           if it has only positive input arcs
              - if "helps"   return any of t,f
             - if "makes"  return  t
           if there is a mixture of positive and negatives :
              return any of t,f

function valUp(node):
   "in the style of fuzzy logic, reason optimisitically about ors"       
     for kid in shuffle(kids):
             if val(kid) then 
                 if positive arc for kid to node
                     return t
   else return f
```   
