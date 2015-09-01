% calculation of benefits


benefit(X,Y) :- b(X,Y0), Y is Y0.

b(X,Y) :- once(b0(X,What)), b1(What,Y).%, format('~w becomes ~w and benefits ~w ~n', [X, What, Y]). 

b0(X,      oops(var))    :- var(X).

b0(claim2parent(A,B), claim2parent(A,B)).  
  
b0(effect(Roulette=G), Out):-
  roulette(Roulette,_), rouletted(effect(Roulette=G), Out).
  
b0(effect(E=G), effect(E=G)). 

b0(true,  true). 
b0((A,B), (A,B)).  
b0((A;B), (A;B)).  

b0(X, Op/V/Terms) :-
  X =.. [Logic,Terms],  check(logics, Logic), score(Logic,Op,V). 

b0(not A, stakeholder(not A)) :- node_info(stakeholder, A, _).  
b0(A, stakeholder(A)) :- node_info(stakeholder, A, _).  

b0(A,     abduced(not A) )  :- choices(A,Ind), memo(Ind,not A,0).
b0(A,     abduced(A) )  :- choices(A,Ind), memo(Ind,A,0).

b0(not A,     claused(not A,R)) :- choices(not A,Ind), memo(Ind,A,R).
b0(A,     claused(not A,R)) :- choices(not A,Ind), memo(Ind,not A,R).
b0(A,     claused(A,R)) :- choices(A,Ind), memo(Ind,A,R).
b0(A,     clause_not_lurched(A,_)) :- clause(A,_). 
b0(A,     unclaused(A)).  
       
b1(true,Value) :- score(default, Value). 
b1((X,Y), O) :- b(X,O1), b(Y,O2), combine(O1,O2,O).  

% without support of claim, effect of child softgoal to parent is 
b1(claim2parent(effect(_=Claim), _),V):- 
  memo(_,not Claim,_), score(wout_claim_support, V). 
b1(claim2parent(Claim, Goal),WWW):- 
  b(Goal, W), b(Claim, WW), 
  scoring(claim2parent, Arith, V), 
  do(Arith, [W,WW], O), do(multiply,[V,O],WWW). 
  
b1(effect(E=G),Out) :-
  scoring(E,Arith,Val), b(G,V), do(Arith,[Val,V],Out).  
  
b1(claused(not A,_), W) :- score(not_done,W), not (var(A), complain('node is not bounded', A)).  
b1(claused(A,R), WW) :- 
  weighting(A,W), 
  clause(A,B,R), 
  brecorda(current_head, R),
  b(B,X), 
  recorded(current_head, R, Ref), erase(Ref),  
  scoring(c2p, Arith, V), 
  do(Arith, [W,X], O), 
  do(multiply,[V,O],WW). 
  
b1(clause_not_lurched(_A,_), W) :- score(not_lurched, W).

b1(Op/V/L0,Y) :- maplist(b,L0,L), do(Op,L,Y0), do(multiply,[V,Y0],Y).
b1(stakeholder(_), V):- score(stakeholder, V).  
b1(abduced(not _),Y) :- score(not_done,Y).  
b1(abduced(A),   Y) :- 
  weighting(abduced, A, Y).  
b1(unclaused(_), Y) :- score(not_done,Y).  
b1(oops(X),      _) :- complain('Something is wrong at calculating benefit',X).

scoring(A,B,D) :-
  score(A,B,C), callable(C), !, call(C,D).
scoring(A,B,C) :- score(A,B,C).

weighting(abduced,A,V) :- !, once(weighting1(abduced,A,V)).
weighting(A,C) :- 
  (severity(A,_,S);S=normal), 
  once(weighting1(S,A,C)).  
weighting1(S,A,C) :- 
  weight(S,A,W), callable(W), !, call(W,C).  
weighting1(S,B,C) :- weight(S,B,C).  

pricing(A,B,D) :-
  price(A,B,C), callable(C), !, call(C,D), jot_down(price,B,D).  
pricing(A,B,C) :- price(A,B,C), jot_down(price,B,C).    
  
combine(V1,V2, Out) :- 
  score(combine, C), 
  do(C, [V1,V2], Out).  

do(add, L, Sum) :- sum(L, Sum).  
do(min,L,Min)    :- min(L,Min).
do(max,L,Max)    :- max(L,Max).
do(average,L,Av) :- average(L,Av).
do(multiply,L,O) :- multiply(L, O). 

rouletted(A,B) :- once(rouletted1(A,B)).%, format('roulette: ~w  ~w ~n', [A,B]).
rouletted1(Roulette, Out) :-
  recorded(current_head, Head), 
  recorded(Head, Roulette=Out). 
rouletted1(A, clause_not_lurched(A,_)).  

jot_down(A,B,C):- once(jot_down1(A,B,C)).  
jot_down1(Key, Node, Info) :-
  enable_jot_down(Key),  
  bassert(jotted_down(Key, Node, Info)).  
jot_down1(_,_,_).