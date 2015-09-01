% setup.pl
% stuff for program setup
% changing the content of this file may have
% reduce your lifespan by half.  Beware.  


:- multifile 
	node_info/3, 
	edge_info/5, 
	severity/3, 
	cost/3,
	of/2, 
	(says)/2, 
	good_effect/1,
	bad_effect/1.
	
:- dynamic 
	memo/3, 
	choice/4,
	roulette/2, 
	price/3. 

:- dynamic 
	enable_jot_down/1, % record things like cost, weight etc for a node (useful when randomizing)
	jotted_down/3. 

go(X) :-  reset, reset(records), time(run(X)), !, report(X).
run(X) :- once(lurch(X)). 
reset  :- retractall(memo(_,_,_)), retractall(jotted_down(_,_,_)), retractall(price(_,_,_)). 
reset(tar2) :- retractall(curr_class(_,_,_,_)).

reset(records) :-  reset_records(roulette).
reset_records(A) :- once(reset_records1(A)).
reset_records1(PointerKey) :- 
  recorded(PointerKey,_), 
  bagof([Ref,OwnRef], recorded(PointerKey, Ref, OwnRef), AllRefs), 
  flatten(AllRefs, F), checklist(reset_records2, F).
reset_records1(_). 

reset_records2(Ref):- catch(erase(Ref), _, true).

fake_memo(Node) :-
   choices(Node, Index), bassert(memo(Index, Node, 0)). 

welcome :-
  format('~s~n~s~n~s~n~s~n~s~n~s~n~s~n', [
"---->'?- readme' --- for notes; ", 
"---->'?- demo(d)' and demo(a) (please halt and restart prolog for different demo) for examples; ", 
"---->'?- go(TopLevelGoalName)' for inference after loading definition file;", 
"---->......definition files are under folder /defs; ", 
"---->......refer to main.pl for descriptions of all pl files;", 
"---->......refer to todos for a list of (my) todos", 
"---->......graph will be opened by your windows' default viewer;"
]).  