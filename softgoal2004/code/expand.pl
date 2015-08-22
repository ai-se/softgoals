expand_relate(Tail depends_on Rest, Tail, depends_on, Rest). 
expand_relate(Parent consists_of Rest, Parent, consists_of, Rest).  
expand_relate(Parent means Rest, Parent, means, Rest). 

expand_nodes(A, B, C) :- once(expand_nodes0(A,B,C)).  

expand_nodes0(Type, Node in Actor is C costed Cost, [cost(Node,Type,Cost)|Out]) :- 
  check(costs, Cost), expand_nodes(Type, Node in Actor is C, Out).  
  
expand_nodes0(Type, Node in Actor is C, [severity(Node,Type,C),Out]) :-
  check(severity, C), expand_nodes(Type, Node in Actor, Out).  
  
expand_nodes0(Type, Node in Actor costed Cost, [cost(Node,Type,Cost),Out]) :-
  check(costs, Cost), expand_nodes(Type, Node in Actor, Out).  
  
expand_nodes0(Type, Node is C costed Cost, [cost(Node,Type,Cost)|Out]) :-
  check(costs, Cost), expand_nodes(Type, Node is C, Out).  
  
expand_nodes0(Type, Node is C, [severity(Node,Type,C),Out]) :-
  check(severity, C), expand_nodes(Type, Node, Out).  
  
expand_nodes0(Type, Node costed C, [cost(Node,Type,C),Out]) :-
  check(costs, C), expand_nodes(Type, Node, Out).  
  
expand_nodes0(Type, Node in Actor, node_info(Type, Node, Actor)).

expand_nodes0(Type, Node, node_info(Type, Node, global)). 
expand_nodes0(_,_,P,_) :- complain(wrongSyntax, node, P).  

term_expansion(A if Blah, Out) :-
  expand_term(everyone says A if Blah, Out). 
term_expansion(Man says Goal if Blah, 
  [(Goal :- Man, Blah)|NEInfo]) :-
  expand0(Goal, contributions, Blah, _, NEInfo).  
term_expansion(R, Out):-
  expand_relate(R, Tail, Type, Rest), 
  expand0(Tail, Type, Rest, _, Out).  
term_expansion(R, Out):- 
  R =.. [NType,Node], check(nodes, NType), 
  expand_nodes(NType, Node, Out).  

expand0(A, B, C, D, E) :- once(expand00(A, B, C, D, E)). 
expand1(A, B, C, D, E) :- once(expand10(A, B, C, D, E)). 
find_junks(A, B, C) :- once(find_junks0(A,B,C)).  

% Node1 depends_on Node2 for Node3...  
expand00(Tail, Type, Mid for Rest, Junks, [O1,O2]):- 
  find_junks(Rest, Head, Junks), 
  expand1(Tail, Type, Head, Junks, O1), 
  expand1(Head, Type, Mid, Junks, O2).  

% Node1 consists_of Node2 all_of Node 3 all_of N..
expand00(Parent, Type, Logical, Junks, Out):- 
  not Type =.. [^|_], has_logic(Logical, Logic,_,_), 
  expand0(Parent, Type^Logic, Logical, Junks, Out).  
expand00(Parent, Type^Logic, Logical, Junks, [O1|O2]):- 
  has_logic(Logical, Logic, Child, Rest),
  expand0(Parent, Type^Logic, Rest, Junks, O2),
  expand1(Parent, Type^Logic, Child, Junks, O1).  

expand00(Tail, Type, Rest, Junks, Out):- 
  find_junks(Rest, Head, Junks), 
  expand1(Tail, Type, Head, Junks, Out). 

has_logic(Child all_of Rest, all_of, Child, Rest). 
has_logic(Child none_of Rest, none_of, Child, Rest). 
has_logic(Child any_of Rest, any_of, Child, Rest). 
has_logic(Child any_one_of Rest, any_one_of, Child, Rest). 
has_logic(Child one_of Rest, one_of, Child, Rest).  

has_logic(Child and Rest, and, Child, Rest).
has_logic(Child or Rest, or, Child, Rest).

find_junks0(Head, Head, [ref="nil", keywords=[all]]):-
  not compound(Head).  
find_junks0(Junks, Head, [JunkShell=JunkMeat|OtherJunks]) :-
  find_junks1(Junks, JunkShell, Head, T), 
  find_junks0(T, JunkMeat, OtherJunks).  
find_junks0(List, List, []) :- is_list(List). 

find_junks1(Head ref T, ref, Head, T). 
find_junks1(Head keywords T, keywords, Head, T). 

expand10(Tail, Type, C1 with C2, Junks, 
    [node_info(intermediate_node, Tail^C1^(intermediate), global), 
    O1,O2,O3]) :-
  expand1(Tail, Type^(intermediate), Tail^C1^(intermediate), Junks, O1),
  expand1(Tail^C1^(intermediate), intermediate, C1, [ref="",keywords=[]], O2),
  expand1(Tail^C1^(intermediate), Type^(with), C2, Junks, O3).  
expand10(Tail, Type, What by Head, Junks, Out) :-
  expand1(Tail, Type^What, Head, Junks, Out).  
expand10(Tail, Type, Head, Junks, Out) :-
  append([edge_info, Type, (Tail), (Head)], Junks, O), 
  Out =.. O. 
  
goal_expansion(A, O) :-
  has_logic(A, Logic, B, Rest), 
  expand_goal(B, Clause), c2l(Clause, NC), 
  expand_my_goal(Rest, Logic, Expanded), 
  flatten([NC|Expanded], E), 
  O =.. [Logic, E]. 
% pass Logic to make sure each clause has only one type of logic

expand_my_goal(Rest,Logic,[NB|Expanded]) :-
  has_logic(Rest, Logic, B, ORest), 
  expand_goal(B, NewB), c2l(NewB, NB), 
  expand_my_goal(ORest, Logic, Expanded).  
expand_my_goal(Rest,_,W):-
  expand_goal(Rest, What), c2l(What, W).  
expand_my_goal(R,_,[]):- print(R), nl.

%goal_expansion(A with B, (claim2parent(B1,A1),A2)):- 
%  expand_goal(A, A1), c2l(A1,A2), 
%  expand_goal(B, B1).  
goal_expansion(A with B, (claim2parent(B1,A1))):- 
  expand_goal(A, A1), 
  expand_goal(B, B1).  
goal_expansion(not X, \+ X).    
goal_expansion(Whatever ref _, Whatever).    
goal_expansion(Whatever keywords _, Whatever).    
%goal_expansion(A by B, (effect(A=B), B)).
goal_expansion(A by B, effect(A=B)).
