% utils.pl
% misc utilities including textual output
% for TAR2

tar2_directory('tar2'). 
%tar2_pencentile_chop('seperate'). 
tar2_pencentile_chop('benefitOverCost'). 

function_param_location(benefitOverCost, [benefit=0, cost=1]).
classify_function(benefitOverCost, [divide, benefit, cost]). % = benefit/cost
%function_param_location(benefitOverCost, [benefit=0, cost=1]).
classify_function(benefitOverCostSq, [divide, benefit, [times, cost, cost]]). %= benefit / (cost * cost)
classify_function(benefitSqOverCost, [divide, [times, benefit, benefit], cost]). %= (benefit*benefit) / cost


divide(A,0,C) :- C is A/0.0001.  
divide(0,B,C) :- C is 0.0001/B. % not much accuracy here
divide(A,B,C) :- C is A/B. 

times(0,B,C) :- C is 0.0001*B. % not much accuracy here, 'cuz values like 0 is just an approximation
times(A,0,C) :- C is A*0.0001.  
times(A,B,C) :- C is A*B. 
% ------------------------- attribute settings --------------------------%
  
att(stakeholder, 'y,n,u'). 
att(claim, 'y,n,u'). 
att(softgoal, 'y,n,u'). 

attribute_type(price=_, continuous). 
attribute_type(cost,continuous).
attribute_type(benefit,continuous).

attribute_type(X,AType) :-
  node_info(Type,X,_), att(Type, AType).  
  
% ------------------------- class settings --------------------------%

% Important!! define benefit from smallest value class to largest value class
class(benefit, V, benefit_vvlow) :- var(V). 
class(benefit, V, benefit_vlow) :- var(V). 
class(benefit, V, benefit_low) :- var(V).  
class(benefit, V, benefit_high) :- var(V). 
class(benefit, V, benefit_vhigh) :- var(V). 
class(benefit, V, benefit_vvhigh) :- var(V). 

class(cost, V, cost_vvlow) :- var(V). 
class(cost, V, cost_vlow) :- var(V). 
class(cost, V, cost_low) :- var(V).  
class(cost, V, cost_high) :- var(V). 
class(cost, V, cost_vhigh) :- var(V). 
class(cost, V, cost_vvhigh) :- var(V). 

class(benefit, V, Class) :- 
  clause(curr_class(benefit, Min, Max, Class), true), ground(V), 
  V>=Min, V=<Max, !. 

class(cost, V, Class) :- 
  clause(curr_class(cost, Min, Max, Class), true), ground(V), 
  V>=Min, V=<Max, !. 

class(Function, V, Class) :- 
  clause(curr_class(Function, M, M, Class), true), ground(V), 
  V=:=M. 
  
class(Function, V, Class) :- 
  clause(curr_class(Function, Min, Max, Class), true), ground(V), 
  V>=Min, V<Max, !. 
  
claims(L) :- nodes(claim, L). 
softgoals(L) :- nodes(softgoal, L). 
stakeholders(L) :- nodes(stakeholder, L). 

% TODO:   after changing the analysis activities to a specific type, change this here!!
priced_leaves(L) :- softgoals(All), unclaused(All, L). 

unclaused(All, Out) :- unclaused(All, [], Out). 
unclaused(A,B,C):- once(unclaused1(A,B,C)). 
unclaused1([],O,O). 
unclaused1([H|T],Tmp,Out):-
  clause(H,_), unclaused1(T,Tmp,Out).
unclaused1([H|T], Tmp, [price=H|Out]):-
  unclaused1(T,Tmp,Out).

classify('seperate', Cost, Benefit, B=C) :-
  class(cost, Cost, C), class(benefit, Benefit, B). 

classify(FunctionName,Cost,Benefit, Name) :-
  number(Cost), number(Benefit), 
  classify_function(FunctionName, List), 
  tar2_analyse_calculate([cost=Cost, benefit=Benefit], List, Out), 
  class(FunctionName, Out, Name). 

classify(_,VC,VB, Name) :-
  class(cost, VC, C), class(benefit, VB, B), 
  tar2_analyse_format_classname([B,C], Name). 
  
nodes(Type, L) :-
  findall(C, A^node_info(Type, C, A), Cs), sort(Cs, L). 
 % don't care about cost, yet
/*
attributes(L) :- 
  softgoals(L1), 
  stakeholders(L2), 
  claims(L3), 
  priced_leaves(L4), 
  append(L1,L2,LA), append(LA,L3,LB), append(LB, L4, L). 
  */
  
attributes(L) :- 
  softgoals(L1), 
  stakeholders(L2), 
  claims(L3), 
  append(L1,L2,LA), append(LA,L3,L).
  
done(price=Node,   Price) :- bagof(Price, jotted_down(price, Node, Price), [Price]).  % make sure only one
done(price=Node,   0) :- findall(Price, jotted_down(price, Node, Price), []).  % make sure only one
done(price=_,_):- complain('price', 'not being signleton!'), abort.
done(Node, n) :-  memo(_,not Node, _). % assumed false
done(Node, y) :-  memo(_,Node, _). % assumed true
done(_, u). % not assumed
