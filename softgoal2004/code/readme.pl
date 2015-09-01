readme :-
  show_me_types, 
  show_me_all_notes. 
  
show_me_all_notes :- forall( note(Type,String), show_me('general notes', Type, String)). 
  
show_me_types:-forall( type(Type, List), show_me('type', Type, List)). 
show_me(Head, Type, List) :- 
  is_list(List), format('~w: ~t~w has ~w ~n', [Head, Type, List]). 
show_me(Head, Type, String) :- 
  format('~w --- ~t[~w] :~t ~w ~n', [Head, Type, String]). 
  
note(edge_def, 
  'edges with different logical relations should be defined in individual sentences. i.e. a consists_of b and c.  a consists_of d or e. ').
  
note(tar2, 
  'functions for easy tar2-ing can be found in utils.pl').  
  
note(lurch, 
  ' if SG :- rule1, A by C1 any_of B by C2. and SG :- rule2, X by C3 one_of Y by C4. either rule1 or rule2 will be true in one inference').  
  
note(lurch, 
  ' the trick is to set the top-level goal is composed of any_of children'). 
  
note(softgoal, 
  ' assumption:  goals after with are claims to an edge').  
  
note(cara, 
  ' cara graphs are located under folder /graphs').  
  
note(test, 
  ' test cases are under folder tests').  
note(test, 
  ' load file test.pl for running test cases').  