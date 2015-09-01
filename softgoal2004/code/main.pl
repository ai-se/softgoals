
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
  extract, 		% graphing sub-module
  choices, 	% clause-head calling syntax
  lurch, 		% meta-interpreter
%  lurch_new, 		% meta-interpreter with pick_one_in
  utils, 		% utils for tar2	
  benefits,	% heuristic
  score
  ], 
  [silent(true)]).  
%    [silent(false)]).  
  
:- format('~s', [
  "----------------------Please modify score.pl for the type of scoring.--------------------------- "
  ]).  
  