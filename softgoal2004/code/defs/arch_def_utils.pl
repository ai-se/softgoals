% utils.pl
% misc utilities including textual output
% for TAR2

tar2_directory('tar2'). 
tar2_pencentile_chop('seperate'). 
classify_function(na). % don't need this if set tar2_analyse_pl
% ------------------------- attribute settings --------------------------%
  
att(stakeholder, 'y,n,u'). 
att(claim, 'y,n,u'). 
att(softgoal, 'y,n,u'). 

attribute_type(cost,continuous).
attribute_type(benefit,continuous).

attribute_type(X,AType) :-
  node_info(Type,X,_), att(Type, AType).  
  
% ------------------------- class settings --------------------------%

% Important!! define benefit from smallest value class to largest value class
class(benefit, V, vvlow_benefit) :- var(V). 
class(benefit, V, vlow_benefit) :- var(V). 
class(benefit, V, low_benefit) :- var(V).  
class(benefit, V, high_benefit) :- var(V). 
class(benefit, V, vhigh_benefit) :- var(V). 
class(benefit, V, vvhigh_benefit) :- var(V). 

class(benefit, V, Class) :- 
  clause(curr_class(benefit, Min, Max, Class), true), ground(V), 
 % class(benefit, _, Class), 
  V>=Min, V=<Max, !. 
  
class(cost, 0, zero_cost). 
class(cost, 1, one_cost). 
class(cost, 2, two_cost). 
class(cost, 3, three_cost). 
class(cost, 4, four_cost). 
class(cost, 5, five_cost). 


claims(L) :- nodes(claim, L). 
softgoals(L) :- nodes(softgoal, L). 
stakeholders(L) :- nodes(stakeholder, L). 

classify('seperate', Cost, Benefit, C=B) :-
  class(cost, Cost, C), class(benefit, Benefit, B). 

nodes(Type, L) :-
  findall(C, A^node_info(Type, C, A), Cs), sort(Cs, L). 
attributes(L) :- 
  softgoals(L1), 
  stakeholders(L2), 
  claims(L3), 
  append(L1,L2,L0), append(L0,L3,L). 
  
done(Node, n) :-  memo(_,not Node, _). % assumed false
done(Node, y) :-  memo(_,Node, _). % assumed true
done(_, u). % not assumed
