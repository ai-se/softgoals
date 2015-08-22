

d2l((X;Y),[X|Rest]) :- !,d2l(Y,Rest).
d2l(X,    [X]).

c2l((X,Y),[X|Rest]) :- !,c2l(Y,Rest).
c2l(X,    [X]).

try(X) :- X.
try(_).

invert([H|T], [not H|T1]) :-
  invert(T,T1). 
invert([],[]). 

min([H|T],Min) :- min(T,H,Min).
min([],X,X).
min([H|T],In,Out) :- 
	(In < H -> Temp=In ; Temp=H),
	min(T,Temp,Out).

max([H|T],Max) :- max(T,H,Max).
max([],X,X).
max([H|T],In,Out) :- 
	(In > H -> Temp=In ; Temp=H),
	max(T,Temp,Out).
	
average(L,A) :-
	sum(L,S),
	length(L,N),
	A is S/N.
	
sum([H|T],N) :- sum(T,H,N).
sum([],Z,Z).
sum([H|T],X,Z) :-  Y is X + H,  sum(T,Y,Z). 
sums(L0,S) :- flatten(L0,L), sum(L,S).

multiply(L,Out):- multiply(L,1,Out).  
multiply([H|L],Temp,Out):- 
  T0 is Temp*H, multiply(L,T0,Out).  
multiply([],T,T).  


:- arithmetic_function(randomize/2).
:- arithmetic_function(randomize/1).

% randomize(normal(0,0.4), [[>=, 0], [=<, 0.2]], P).

randomize(A,B) :- callable(A), call(A,B). 

randomize(A,B,C) :- once(randomize1(A,B,C)).  
randomize1(ArithFun, CriteriaList, Out) :-
  callable(ArithFun), call(ArithFun, Out), 
  checklist(randomize2(Out), CriteriaList).  
randomize1(A,B,C) :- randomize(A,B,C). % recurse until the output passes the criteria
  
randomize2(Val, [Expr,Num]) :-
  Call =.. [Expr, Val, Num], call(Call).  

:- arithmetic_function(range/2).
range(Min,Max,Out) :-
  Out is (Max-Min)*ranf+Min. 


:- arithmetic_function(skewed_range/3).

skewed_range(Mean,Min, Max,Out) :-
  O is (Mean-Min)/(Max-Min), 
  beta_values(L), skewed_range1(O,L,Beta), 
  beta(Beta, 1, O1), Out is O1*(Max-Min)+Min.   
  
skewed_range1(_O, [Out], Out).
skewed_range1(O, [Out|_], Out) :- 
  OO is truncate(O*100), OOut is truncate(Out*100), OO=<OOut.
skewed_range1(O, [_|L], Out) :- skewed_range1(O,L,Out). 
/*

=(K,V,Old, [K=V|Less])  :- less1(Old,K=V0,Less),!, V0 = V. 
=(K,V,Old, [K=V|Old]). 
*/
:- arithmetic_function(normal/2).

normal(M,S,N) :-
        box_muller(M,S,N).

% classical fast method for computing
% normal functions using polar co-ords
% (no- i dont understand it either)
box_muller(M,S,N) :-
        w(W0,X),
        W is sqrt((-2.0 * log(W0))/W0),
        Y1 is X * W,
        N is M + Y1*S.

w(W,X) :-
        X1 is 2.0 * ranf - 1,
        X2 is 2.0 * ranf - 1,
        W0 is X1*X1 + X2*X2,
        % IF -> THEN ; ELSE
        % same as xx :- IF,!, THEN,
        %         xx :- ELSE
        % vars bound in IF not available to ELSE
        % no backtracking within the IF
        % -> ; precendence higher than ,
        (W0  >= 1.0 -> w(W,X) ; W0=W, X = X1).

:- arithmetic_function(ranf/0).

ranf(X) :-
        N =  65536,
        % X is random(N) returns a
        % random number from 0 .. N-1
        X is random(N)/N.
/*
repeats(N,X) :-
	between(1,N,I),
	memo(I),
	once(X),
	fail.
repeats(_,_).

memo(X) :- 0 is X mod 250, !, write(user,X), nl(user), flush_output(user).
memo(_).

printl([X|Y],Sep) :- 
	write(X), 
	forall(member(Z,Y),format('~w~w',[Sep,Z])).
*/


 :- arithmetic_function(beta/2). 

 beta(B,Param,X) :- beta1(B,Param,X).	
 
 beta1(B,Param,X) :- beta2(B,Param,X),!.
 beta1(B,Param,X) :- B1 is 1.0 - B, beta2(B1,Param,Y),X is 1 - Y.
 
 beta2(0.33,Param,X) :- X is (1-ranf^(0.5*Param)). 
 beta2(0.50,_,X) :- X is ranf. 
 beta2(0.60,Param,X) :- X is ranf^(0.67*Param).
 beta2(0.670,Param,X) :- X is ranf^(0.5*Param).
 beta2(0.750,Param,X) :- X is ranf^(0.33*Param).
 beta2(0.80,Param,X) :- X is ranf^(0.25*Param).
 beta2(0.90,Param,X)  :- X is ranf^((1/9)*Param).
 beta2(1,_,1).

gen_betas :-
  bagof(Num, A^B^Whatever^clause(beta2(Num, A,B),Whatever), Nums), 
  maplist(gen_betas1, Nums, N1), 
  append(Nums, N1, AllBs), sort(AllBs, Sorted), 
  assert(beta_values(Sorted)). 
gen_betas1(Num, Out) :- Out is 1-Num.  

:- gen_betas. 

oneof(X,Y,Z) :-
	bagof(X,Y, L),
	rone(L,Z,_).
	
bassert(X) :- assert(X).
bassert(X) :- retract(X),fail.

bretract(X) :- retract(X), bretract1(X).
bretract1(_).
bretract1(X) :- assert(X),fail.
 
brecorda(Key,Item) :- recorda(Key, Item).
brecorda(Key,Item) :- recorded(Key, Item, Ref), erase(Ref), fail. 

brecorda(Key,Item,Ref) :- recorda(Key,Item,Ref).
brecorda(Key,Item,_) :- recorded(Key, Item, Ref), erase(Ref), fail. 

l2r(L,Out, Rest) :- member(Out,L), select(Out, L, Rest). 
 
rone(L,One,Rest) :- length(L,N), rone(L,N,One,Rest,_).

rone([H],_,H,[],0) :- !.
rone([H|T],N0,X,Out,N) :-
        N is N0 - 1,
        Pos is random(N0) + 1,
        less1(Pos,One,[H|T],Rest),
        (X=One,
         Out=Rest
        ; Out=[One|Tail],
          N1 is N0 - 1,
          rone(Rest,N1,X,Tail,_)).


less1(1,H,[H|T],T) :- !.
less1(N0,X,[H|T],[H|L]) :-  N is N0 - 1, less1(N,X,T,L).

:- dynamic knownBuiltIn/1.

 makeBuiltin(X) :- knownBuiltIn(X),!.
 makeBuiltin(X) :- assert(knownBuiltIn(X)).

 :- forall(predicate_property(X,built_in), makeBuiltin(X)).
