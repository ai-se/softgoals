% Eliza's version of lurch
% A modified version of lurch by Dr Menzies
lurch(X) :- once(lurch0(X,Y)), lurch1(Y).

lurch0(X, bad(var,X)) :- var(X). 
lurch0(not not X, Y) :- lurch0(X,Y).
lurch0(not claim2parent(effect(CEffect=Claim),effect(Effect=Goal)), 
    claim2parent(effect(InvC=Claim),effect(Inv=Goal))) :- 
  invert_effect(CEffect, InvC), invert_effect(Effect, Inv).
  
% specific for effects that are randomly picked  
lurch0(not effect(Roulettable=G), effect(InvE=G)) :- 
  roulette(Roulettable, _), 
  lurching_roulette(effect(Roulettable=G),effect(REffect=G)), 
  invert_effect(REffect,InvE).
  
lurch0(not effect(E=G), effect(InvE=G)) :- invert_effect(E,InvE).  

% if X is logic(Blah) and it is negated, de_morgan the logic  
lurch0(not X, logic(DLogic, Terms)) :- 
  lurch0(X, logic(Type, Terms)), 
  check(internal_logics, Type), 
  de_morgan(Type, DLogic). 
  
lurch0(not (X,Y), (not X;not Y)).
lurch0(not (X;Y), (not X,not Y)).
lurch0(not (call(X)), call(not X)). 
  
lurch0(not X, old(not X,Index)) :- 
  choices(not X,Index),   % check that neither X nor not X is memo-ed
  (\+ \+ memo(Index,not X,_); \+ \+ memo(Index,X,_)).
% should NOT have not for pick_one!!!
%lurch0(not X, pick_one_in(not X,List,Pick_one_Index,Index)) :- 
%  choices(not X,Index), \+ clause(X,_), pick_one_in(List), member(X,List), choices(pick_one_in(List),Pick_one_Index). 
lurch0(not X, assume(not X,Index)) :- 
  choices(not X,Index), \+ clause(X,_).
lurch0(not X, new(not, X,Index)) :- choices(not X,Index).

lurch0(claim2parent(A,B),claim2parent(A,B)).
  
% specific for effects that are randomly picked
lurch0(effect(Roulettable=G), effect(REffect=G)):- 
  roulette(Roulettable, _), 
  lurching_roulette(effect(Roulettable=G),effect(REffect=G)).
  
lurch0(effect(E=G), effect(E=G)). % softgoal app specific stuff

lurch0(call(X), call(X)).
lurch0(true, true).
lurch0((X->Y;Z), (X->Y;Z)).
lurch0(once(X), once(X)).
lurch0((X,Y), (X,Y)).
lurch0(X, logic(InferType, Terms)) :-
  X =.. [Logic,Terms],  check(logics, Logic), 
  infer(Logic, InferType).
  
lurch0(X, old(X,Index)) :- 
  choices(X,Index),   % check that neither X nor not X is memo-ed
  (\+ \+ memo(Index,X,_); \+ \+ memo(Index,not X,_)).
lurch0(X, pick_one_in(X,List, Pick_one_Index, Index)) :- choices(X,Index), \+ clause(X,_), 
  pick_one_in(List), member(X,List), choices(pick_one_in(List),Pick_one_Index). 
lurch0(X, assume(X,Index)) :- choices(X,Index), \+ clause(X,_).
lurch0(X, new(X,Index)) :- choices(X,Index). 
lurch0(X, call(X)) :- knownBuiltIn(X).
lurch0(X, sub(X)) :- clause(X,_).  
lurch0(X, bad(unknown, X)).

% lurch1:  processed arg 2 of lurch0
% softgoal specific.  
% first find out whether Claim is true or not
% if Claim is true and it supports the Goal, lurch Goal

%  choices(Claim, Index), bassert(rouletted(Index, Claim, REffect)). 

lurch1(claim2parent(effect(CEffect=Claim), Goal)):- 
  lurch(Claim), good_effect(CEffect), lurch(Goal).  

% if claim refute an effect on goal, and if claim is false, than
% do the goal.  
lurch1(claim2parent(effect(CEffect=Claim),Goal)):- 
  lurch(not Claim), bad_effect(CEffect), lurch(Goal). 

% otherwise, don't ever lurch goal 'cuz it won't have any effect anyways  
lurch1(claim2parent(_,_)).  

%  choices(G, Index), bassert(rouletted(Index, G, R)). 
  
lurch1(effect(E=G)) :- good_effect(E), lurch(G). 
lurch1(effect(E=G)) :- bad_effect(E), lurch(not G).  

lurch1(true). 
lurch1(bad(Type, X))       :- complain(Type, X). % changed barph to complain - just a matter of terminology...
lurch1(call(X))      :- X.
lurch1(sub(X))       :- \+ X=not(_), clause(X,Y), lurch(Y).
lurch1(once(X))      :- once(lurch(X)). 
lurch1(old(X,Index)) :- memo(Index,X,_).

% conjunction:  no logics such as rors, rany etc involved
lurch1((X;Y)):- once(rone([X,Y],Z,[A])), (lurch(Z); lurch(A)). 
lurch1((X,Y)):- once(rone([X,Y],Z,[A])), lurch(Z), lurch(A). 

% Eliza hasn't use this.  
lurch1((X->Y;Z))     :- lurch(X) -> lurch(Y) ; lurch(Z).

lurch1(logic(Logic, Terms)) :- 
  lurch_logic(Logic, Rules), lurching( Rules, Terms).  

lurch1(pick_one_in(X,List, Pick_one_index, Index)) :- 
  select(X,List,Rest), 
  forall(member(One, Rest), 
    (
      (\+ memo(_,One,_)) 
      -> (memo(_, not One, _);bassert(memo(Pick_one_index, not One, 0)))
    )
  ), 
  lurch1(assume(X,Index)). 
  
lurch1(assume(X,Index)) :- bassert(memo(Index,X,0)).
lurch1(new(not, X,Index)) :- 
	oneof(X/Y/R,clause(X,Y,R), X/Y1/R1), 
	brecorda(current_head, R1), %format('lurching not ~w ~n', [X]), 
	lurch(not Y1), %format('lurched not ~w ~n', [X]), 
	recorded(current_head, R1, Ref), erase(Ref),
	bassert(memo(Index,not X,R1)).	
lurch1(new(X,Index)) :- 
	oneof(X/Y/R,clause(X,Y,R), X/Y1/R1), 
	brecorda(current_head, R1), %format('lurching ~w ~n', [X]), 
	lurch(Y1), %format('lurched ~w ~n', [X]), 
	recorded(current_head, R1, Ref), erase(Ref),
	bassert(memo(Index,X,R1)).	

% -------------------------------logics and logics--------------------------------
lurching(Rules, Terms) :- 
  decode_rules(Rules, Sequence, Ys, Ns, YTries, NTries, Terms), 
  lurching0(Sequence, 'y', Ys, YTries, Terms), 
  lurching0(Sequence, 'n', Ns, NTries, Terms). 
  
decode_rules(Rules, S, Y, N, YT, NT, Terms) :- length(Terms, L), 
  maplist(decode(Rules, L), [seq,y,n,ytries,ntries], [S,Y,N,YT,NT]). 
decode(A,B,C,D) :- once(decode1(A,B,C,D)). 
decode1(Rules, Len, A, Len):- memberchk(A=all, Rules). 
decode1(Rules, Len, A, L):- memberchk(A=xc(X), Rules), L is Len - X.  
decode1(Rules, _, A, B):- memberchk(A=B, Rules). 

lurching0(A,B,C,D,E) :- once(lurching1(A,B,C,D,E)). 

lurching1(_,_,Var,_,_) :- not integer(Var).  % do lurching only if we care about the threshold
lurching1(_,_,_,0,_).  % stop lurching when no more tries

lurching1(Seq, YOrN, Threshold, OTries, Terms):- %Seq is either l2r or rone
  GetOne =.. [Seq, Terms, H, T], call(GetOne), 
  lurching2(H, YOrN, Threshold, NThreshold), 
  Tries is OTries - 1, !, 
  lurching0(Seq, YOrN, NThreshold, Tries, T).
  
lurching2(Term, YesOrNo, 0, 0) :- try(lurching3(Term, YesOrNo)).
lurching2(Term, YesOrNo, Th, NTh) :- lurching3(Term, YesOrNo), NTh is Th -1.   
lurching3(Term, 'y') :- lurch(Term). 
lurching3(Term, 'n') :- lurch(not Term). 
% -------------------------------get rouletted effects--------------------------------
lurching_roulette(A,B) :- once(lurching_roulette1(A,B)).  
lurching_roulette1(Key, Rouletted) :- 
  recorded(current_head, H), recorded(H, Key=Rouletted).
lurching_roulette1(Key, Rouletted) :- 
  rouletting(Key, Rouletted), recorded(current_head, H), 
  brecorda(H, Key=Rouletted, Ref), brecorda(roulette,Ref).