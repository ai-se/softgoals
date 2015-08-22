
:- welcome.  

my_dir('C:/eliza/code/playground/'). 
my_graph_folder('present/').  
my_graphviz('C:/ATT/Graphviz/bin/dot.exe').  

demo(d) :- [main], 
  my_dir(D), my_graph_folder(F), 
  atom_concat(D,F,DF), 
  (\+ exists_directory(DF)
  ->  make_directory(DF)
  ;true), 
  demo(d,_), pause, fail. 

demo(a) :- [main],  
  my_dir(D), my_graph_folder(F), 
  atom_concat(D,F,DF), 
  (\+ exists_directory(DF)
  ->  make_directory(DF)
  ;true), 
  demo(a,1), pause, demo(a,2), pause, demo(a,3), pause.  
demo(_).  

gimme(FileName, FullPath) :- 
  my_dir(D), my_graph_folder(F), 
  atom_concat(D,F,DF), 
  atom_concat(DF, FileName, FullPath).  

demo(d,1) :- [defs/def], 
  gimme('all', P), 
  format('Graph all defined nodes and edges ~n'),
  demo1(graph, [], P).  
demo(d,2) :-
  gimme('fig1', P), 
  format('Graph nodes with keyword fig1: ~n'), 
  demo1(graph, [keywords=[fig1]], P).  
demo(d,3) :-
  gimme('fig3', P), 
  format('Another example --- Graph nodes with keyword fig3: ~n'), 
  demo1(graph, [keywords=[fig3]], P).  
demo(d,4) :-
  gimme('fig4', P), 
  format('One more example --- Graph nodes with keyword fig4: ~n'), 
  demo1(graph, [keywords=[fig4]], P).  
demo(d,5) :-
  gimme('softgoal', P), 
  format('Graph nodes with node labelled softgoal: ~n'), 
  demo1(graph_type,softgoal, P).  
demo(d,6) :-
  gimme('contributions', P), 
  format('Another example -- Graph nodes with edge labelled contributions: ~n'), 
  demo1(graph_type,contributions, P).  
  
demo(a,1) :- [defs/arch_def], 
  gimme('arch', P), 
  format('An example Softgoal graph from Chung et al ~n'), 
  demo1(graph, [], P).  
  
demo(a,2) :-
  format('Inference number 1: ~n score goodness of system ~n'), 
  go(goodness of system).  
  
demo(a,3) :-
  format('Inference number 2: ~n'), 
  go(goodness of system).  
  
demo1(graph, Params, FileName) :-
  atom_concat(FileName, '.dot', Dot), 
  atom_concat(FileName, '.gif', Gif), 
  graph(Params, Dot),
  demo2(Dot, Gif). 
  
demo1(graph_type, Type, FileName) :-
  atom_concat(FileName, '.dot', Dot), 
  atom_concat(FileName, '.gif', Gif), 
  graph_type(Type, Dot), 
  demo2(Dot, Gif). 
  
demo2(Dot, Gif) :-
  my_graphviz(G), 
  sformat(S, '~w -Tgif ~w -o ~w', [G,Dot, Gif]), 
  string_to_atom(S, A), 
  shell(A), win_shell(open, Gif).  
  
pause :- format('press any key to continue ~n'), get_single_char(_).
