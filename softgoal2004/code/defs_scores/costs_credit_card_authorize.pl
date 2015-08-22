costs(X) :- todos(All),length(All,X),!.
costs(0).

todos(All) :- bagof(X,todo(X),All),!.
todo(X) :- memo(_,X,0), 
  \+ clause(node_info(claim, X, _), true), 
  \+ clause(node_info(stakeholder, X, _), true), 
  \+ X=not(_), 
  \+ X=mainMemory of attributes(card), 
  \+ X=responseTime_i of nonCommonCode(authorize)at layer([4, commonCode]),
  \+ X=secondaryStorage_i of creditRemaining at layer([4, prioritization]).
