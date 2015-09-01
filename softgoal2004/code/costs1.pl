costs(X) :- todos(All),length(All,X),!.
costs(0).

todos(All) :- bagof(X,todo(X),All),!.
todo(X) :- memo(_,X,0), 
  \+ clause(node_info(claim, X, _), true), 
  \+ clause(node_info(stakeholder, X, _), true), 
  \+ X=not(_). 
