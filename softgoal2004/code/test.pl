
:- load_files([
  readme, 	% notes
  ops, 		% operaters
  lib, 		% util functions
  setup, 		% app setup
  report, 		% report
  logic_setup, 	% logic inference config
  display, 		% graph display config
  check, 		% type checking
  expand, 	% term expansion
  graph, 		% graphing module
  extract,		% graphing sub-module
  choices, 	% clause-head calling syntax
  lurch, 		% meta-interpreter
  score		% heuristic
  ], 
  [silent(false)]).  
  
 
 run_test :-
   expand_file_name('tests/*.pl', Fs), 
   forall(member(F,Fs), [F]). 
 
run_test(X):-
  atom_concat('tests/', X, File), [File]. 
   
go_test(X) :-  reset, run(X), !, details(X).

details(S) :-
  findall(Z, Q^memo(Q,Z,0), Z0), sort(Z0, Zs), 
  format('assume ~t~w~n', [Zs]), 
  findall(X, A^B^(memo(A,X,B), X\= not(_)), X0), sort(X0, Xs), 
  findall(Y, C^D^memo(C,not Y,D), Y0), sort(Y0, Ys), 
  format('do ~t~w~n', [Xs]), 
  format('not do ~t~w~n', [Ys]), 
  scoreReport(S).
  
