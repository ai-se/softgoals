
%enable_jot_down(Type)
%enable_jot_down(price).  

basic_cost(high, randomize(range(1,2))).
cost_variance(_AllPriceType,0.04).  % for x(mean)=1

scaling_factor(high, notHigh, 0.7).
scaling_factor(high, veryHigh, randomize(skewed_range(1.2, 1.1,1.7))).% F=(1.1, 1.7)L, mean(F)=1.2L
scaling_factor(high, extremelyHigh, randomize(skewed_range(1.6,1.2,1.7))).	% F=(1.2, 1.7)L, mean(F)=1.6L

assert_prices:- 
  basic_cost(Type, _), 
  bagof(OtherType, A^B^scaling_factor(A, OtherType, B), OtherTypes), 
  checklist(assert_price, [Type|OtherTypes]).

assert_prices:- basic_cost(Type,_), assert_price(Type).  

assert_price(A) :- once(assert_price1(A)). 
assert_price1(CType):-
  basic_cost(CType, BasicCost),
  bagof(Node/CType, A^cost(Node,A,CType), Structs), 
  forall(
    member(N/C, Structs), 
    (once(call_one(BasicCost,Price)), bassert(price(C,N,Price)))
    ).
    
assert_price1(CType):-
  scaling_factor(CompareType, CType, ScalingRange), 
  bagof(Price, N^price(CompareType,N,Price), Prices), sum(Prices, Total), 
  findall(Node/CType, A^cost(Node,A,CType), Structs), Structs\=[], 
  length(Structs, NumCTypeNode), 
  get_prices(NumCTypeNode, Total, CType, ScalingRange, List), 
  assert_price2(Structs, List). 
assert_price1(_). 

assert_price2([],[]):-!. 
assert_price2([N/C|Structs], [L|List]):-  bassert(price(C,N,L)), assert_price2(Structs, List). 

get_prices(NumCTypeNode, Total, CType, ScalingRange, List):-
  cost_variance(CType, Variance), Std is sqrt(Variance), 
  get_prices1(NumCTypeNode, randomize(normal(1, Std)), L), 
  sum(L,TL), maplist(get_prices2(TL), L, LO), 
  call_one(ScalingRange, NumericalRange), 
  Range is 1/(Total*NumericalRange), 
  maplist(get_prices2(Range), LO, List). 

get_prices1(Num,Fun,Out) :- get_prices1(Num,0,Fun,[],Out). 
get_prices1(Total, Total, _Fun, O, O):-!. 
get_prices1(Total, Curr, Fun, O, [One|Out]) :- 
  once(call_one(Fun, One)), NewCurr is Curr+1, get_prices1(Total, NewCurr, Fun, O, Out).
get_prices2(Divident, One, Out) :- Out is One/Divident.  
  
call_one(Callable,Out):- callable(Callable), call(Callable, Out). 
call_one(C,C).  

costs(X) :- 
  todos(All),
  assert_prices, 
  maplist(getCost, All, Costs), 
  sum(Costs,X).  
  
costs(0).

todos(All) :- bagof(X,todo(X),All),!.
todo(X) :- 
  memo(_,X,0), % limited only to the leaf node
  \+ clause(node_info(claim, X, _), true), % node is not a claim
  \+ clause(node_info(stakeholder, X, _), true), % node is not a stakeholder
  \+ X=not(_). % we _do_ the node

% mean * 20%

getCost(A,B) :- once(getCost1(A,B)).  
getCost1(Node, Cost) :- cost(Node, _, CType), pricing(CType, Node, Cost).  
%getCost1(Node, Cost) :- pricing(notHigh,Node, Cost).  

%			benefit
%		vvl	vl	l	h	vh	vvh	
%     vvl	|	27	18	11	6	3	1
%c    vl	|	29	20	13	8	4	2
%o    l	|	31	22	15	9	7	5
%s    h	|	33	24	16	14	12	10
%t    vh	|	35	25	23	21	19	17
%     vvh	|	36	34	32	30	28	26