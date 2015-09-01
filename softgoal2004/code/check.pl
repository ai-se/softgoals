% check.pl
% check the sanity of the code writer (yup that's me)

type( nodes, [actor, goal, softgoal, task, resource, claim, stakeholder, god]). 
type( edges, [depends_on, means, consists_of, contributions]). 
type( logics, [all_of, none_of, any_of, any_one_of, one_of]). 

type( effects, [
  made, helped, unhurt, unbroken, positively_influenced, 
  catastrophically_rated, 
  critically_rated,
%  moderately_rated, 
  lowly_rated, 
  highly_rated]).  

type( roulette, [ moderately_rated, positively_influenced]).  

type( internal_logics, [
	and, 	
	rand, 	
	or, 	
	ror, 	
	any, 	
	rany, 	
	xor, 	
	rxor, 	
	nand, 	
	rnand, 	
	nor, 	
	rnor, 	
	nany, 	
	nrany,	
	dxor, 	
	rdxor
	]).  

type( severity, [critical, veryCritical, extremelyCritical, normal, nonCritical, mandatory, dominant, nonDominant]).  
type( costs, [ extremelyHigh , veryHigh, high, notHigh]).  

check(A,B) :- once(check1(A,B)).  
check1( Type, Thing) :- type(Type, List), memberchk(Thing, List).  

%cheat here
check1(effect, AnotherTypeThing) :- check(roulette, AnotherTypeThing). 

complain(wrongSyntax, Type, L) :-
  format('Wrong syntax in defining ~w in ~w ~n', [Type, L]). 
  
complain(Type, X) :-
  format('bad ~w for ~w ~n', [Type, X]). 