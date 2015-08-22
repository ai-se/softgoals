% params:  
% simplify=[mediaShop, mediA]
% hide everything within actors mediaShop and mediA
% keywords=[early, fig1, fig2]
% show only edge_info with keywords early, fig1, or fig 2
% format:  graph('file.dot')  graph everything
% graph([keywords=[early, fig1]] graph edges with these keywords
% graph([simplify=[mediaShop, mediA]] graph with simplified
% graph([keywords=[...], simplify=[...]]

graph(FileName) :-
  graph([], FileName).   

graph(Params, FileName) :-
  ignore(write_head(FileName)), 
  graph_edges(Params),
  graph_nodes(FileName), 
  ignore(write_edges(FileName)), 
  ignore(write_bottom(FileName)), 
  clear_node_edge.  
  
graph_nodes(FileName) :-
  setof(BN, A^B^node_info(A,B,BN), BNs), 
  forall(member(OneBN, BNs), graph_node(OneBN)), 
  write_clusters(BNs, FileName).  
  
graph_node(OneBN) :-
  forall(node_info(NType, Name, OneBN), 
  assert_my_node(NType, Name, OneBN)).   
  
graph_edges(Params) :-   
  get_p(simplify, Params, Simplify), 
  get_p(keywords, Params, Keywords), 
  bagof( T|C|P|K, W^edge_info(T,C,P,W,K),Es),
  forall(    % check that the edge is to be shown
      (member(E, Es), 
      E=(_|_|_|keywords=Keyword), 
      check_keywords(Keyword,Keywords)),
    graph_big(E, Simplify)). 
    
graph_big(EdgeT|Child|Parent|_, Simplify):-
   simplify(Child, Simplify, NChild), 
   simplify(Parent, Simplify, NParent),
   assert_my_edge(EdgeT, NChild, NParent).  

check_keywords(A,B):-once(check_keywords0(A,B)).  
check_keywords0(_, []). 
check_keywords0([all], _). 
check_keywords0(Ks, Keywords):-
  member(One,Keywords), memberchk(One, Ks).  

simplify(A,B,C):-once(simplify0(A,B,C)). 
simplify0(One,SList, Big):-
  node_info(_,One,Big), memberchk(Big,SList).  
simplify0(One,_, One).
  
%%%%%%%%%%%%%%%%%%%%%%%%
% get params
get_p(T, P, L):- memberchk(T=L, P), !. 
get_p(_, _, []).

%%%%%%%%%%%%%%%%%%%%%%%%
% assertion and cleaning here
assert_my_edge(EdgeT, NChild, NParent) :- 
  display_gen(EdgeT,Display), 
  sformat(S, '"~w" -> "~w" ~p; ~n', [NChild, NParent, Display]), 
  ensure_assert(edge(S)),
  ensure_assert(appearing(NChild)), 
  ensure_assert(appearing(NParent)). 
assert_my_node(NType, Name, Big) :-
  display_gen(NType,Display), 
  sformat(S, '"~w" ~p; ~n', [Name, Display]), 
  ensure_assert(node(Big, Name, S)).   
  
ensure_assert(Stuff) :-  clause(Stuff, true). 
ensure_assert(Stuff) :- assert(Stuff).  
  
clear_node_edge :- retractall(edge(_)), retractall(node(_,_,_)), retractall(appearing(_)).  
%%%%%%%%%%%%%%%%%%%%%%%%
% write_Whatever
% write stuff on file
write_head(FileName) :-
  tell(FileName), format('digraph G { ~n ranksep=2.0; ~n'), told.  
write_clusters(BNs, FileName) :- 
  forall( 
    member(BN, BNs), 
    ignore(write_cluster(BN, FileName))
  ).  
write_cluster(BN, FileName) :-
  bagof(S, Name^(node(BN, Name, S), appearing(Name)), Ss), 
  append(FileName), 
  format('subgraph ~w { ~n', [BN]),
  format('style=filled; ~n label="~w";', [BN]), 
  forall(member(OneS, Ss), format('~s', OneS)), 
  format('~n} ~n'), 
  told. 
write_edges(FileName):-
  append(FileName), 
  forall( edge(S), format('~s', [S])), told.  
write_bottom(FileName):-
  append(FileName), format('} ~n'), told.  
%%%%%%%%%%%%%%%%%%%%%%%%
