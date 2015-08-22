% extract node types from the definition
% mainly deals with extracting specific information 
% also contains graphing functions
% handles node types

% graph_type(softgoal, 'softgoal.dot'). 
% graph_type(contributions, 'contributions.dot').

:- ensure_loaded('graph.pl').  

graph_type(Type, FileName) :- 
  ignore(write_head(FileName)), 
  graph_type1(Type),  
  graph_nodes(FileName), 
  ignore(write_edges(FileName)), 
  ignore(write_bottom(FileName)), 
  clear_node_edge.  
  
graph_type1(Type) :- once(graph_type10(Type, N)), graph_type2(Type, N).  
graph_type10(Type, nodes) :- check( nodes, Type). 
graph_type10(Type, edges) :- check( edges, Type). 

graph_type10(X) :- complain( 'nodes and edges', X).  

graph_type2(Type, edges) :-
  forall(
    (edge_info(T,C,P,_,_), match_type(Type, T)), 
     assert_my_edge(T,C,P)).  
graph_type2(Type, nodes) :-
  forall(edge_info(_,C,P,_,_), 
    (  graph_type_nodes1(Type, C), 
       graph_type_nodes1(Type, P))).  
graph_type_nodes1(Type, Node) :-
  node_info(Type,Node,_), !, 
  ensure_assert(appearing(Node)), 
  forall(edge_info(T,Node,P,_,_), assert_my_edge(T,Node,P)).  
graph_type_nodes1(_,_).  
     
match_type(T,T):-!. 
match_type(Type,T1^T2) :- 
  match_type(Type,T2); 
  match_type(Type,T1).  
  