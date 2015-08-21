```python
t=True
f=False
any=random.choose
def anything() return any([t,f])

def scores(softgoals,n=1000):
   for _ in xrange(n):
       final += score(softgoals)
   return final/n

def score(softgoals):
  for node in shuffle(all nodes with no parents):
      if val(node)== t
        count += 1
 return cout

def val(x):
  if not x.value:
         if  not x.kids: 
            x.value = anything()
         else: 
            x.value = valDown(x) if x.type == 'and' else valUp(x)
  return x.value

def valDown(x):
   "in the style of fuzzy logic, reason pessimisticaly about ands"
         # just reflect on the arvs to kids that are true
         kids = shuffle([kid for kid in shuffle(x.kids) if  val(kid)])
         if kids have only negative  arcs  to x then:
            oracle= any(activeArcs)
            return f if oralce.type=="breaks"  else anything()
         elif:  kids have only positive input arcs
             oracle= any(activeArcs)
            return t if oracle.type=="makes"  else anything()
         else:
            return anything()

def valUp(x):
   "in the style of fuzzy logic, reason optimisitically about ors"       
    for kid in shuffle(x):
         if val(kid) then 
            if positive arc from kid to x # makes or helps
               return t
  return f
```   
