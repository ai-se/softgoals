

% make sure X fits the input syntax
choices(X,Ref) :-
  choice(X,_,_,Y),
  hash_term(Y,Ref).  

% define types of goals and how they are memo-ed
% choice(Orig, Conjunction, Type, MemoTerm)
% index not terms as same as terms.
% so choices(not X,Ref) with give out hash_term(X, Ref)

% some stakeholders are granted absolute rightness
choice(not X, _, _, _) :- rightness(A), node_info(A, X, _), !, fail.

  
choice(not X, A, B, Y) :- choice(X, A, B, Y).  

choice(X, nil, system_wide, X).  % may print out stuff here
choice(X of Y, of, Y, X of Y).  
  