report(X) :-  quickReport, write('\n===> '), scoreReport(X).

scoreReport(X) :-
	costs(C), 
	benefit(X,B),
	format('cost=~w benefit=~w\n',[C,B]). 

quickReport :- forall(memo(_,Y,0),format('assumption=~w\n',[Y])).

% find max/min for one data at a time to avoid outta stack

findMinMax([],_).
findMinMax([H|T],PosAtL) :-
  [H],
  findMinMax1(PosAtL),
  findMinMax(T,PosAtL).

findMinMax1(PosAtL) :-
  result(_, L), nth0(PosAtL, L, Elem), 
  findM(>=, max, Elem), findM(=<, min, Elem), fail.  
findMinMax1(_).

findM(Arith, M, Elem) :- data(M,CurrM), 
  Call =.. [Arith, Elem, CurrM], Call, !, 
  retract(data(M,CurrM)), assert(data(M,Elem)). 
findM(_,_,_). 

% make sure the directories have only one pl file 
get_boundries_for_all_files(Wildcard, PosAtList):-
   expand_file_name(Wildcard, ListOfFileNames), retractall(data(_,_)), 
   assert(data(max, -1)), assert(data(min, 100000)),
   findMinMax(ListOfFileNames,PosAtList).   
   
   
html_tables([FileName|ListOfFiles], [OneT|ListOfTitles], 
  XLabels, YLabels, XUBound, XLBound, YUBound, YLBound, IndexX, IndexY, String) :-
  retractall(data_classify(_,_,_,_)),
  classify_cell_elem(x,XLabels, XUBound, XLBound), 
  classify_cell_elem(y,YLabels,YUBound,YLBound), 
  html_tables1([FileName|ListOfFiles], [OneT|ListOfTitles], 
  XLabels, YLabels, IndexX, IndexY, "", String).
   
html_tables1([],[],_,_,_,_,S,S).    
html_tables1([FileName|ListOfFiles], [OneT|ListOfTitles], 
  XLabels, YLabels, IndexX, IndexY, CS, String) :-
  html_tablize(FileName, XLabels, YLabels, IndexX, IndexY, S), 
  sformat(TS, '~s<p>Title: ~w ~n ~s', [CS,OneT,S]), 
  html_tables1(ListOfFiles, ListOfTitles, 
  XLabels, YLabels, IndexX, IndexY, TS, String).
   
html_tablize(FileName, XLabels, YLabels, IndexX, IndexY, String) :-
  data_classifying(FileName, IndexX, IndexY), 
  html_tablize_cells([''|XLabels], na, "", XSs), 
  sformat(NS, '<table border=0><tr>~s</tr>~n', [XSs]),
  html_tablize_rows(XLabels,YLabels,NS,S),
  sformat(String, '~s</table>~n',[S]) .  
  
%html_tablize_rows(_,[],S,S).
html_tablize_rows(_,[],S,NewS) :-
  setof(C, Num^reportSlot(C, Num), Cs), max(Cs, Max), 
  bagof(SumBagNum, 
  BagNum^Num^Count^(between(1, Max, Count), 
    (bagof(Num, reportSlot(Count, Num), BagNum), sum(BagNum, SumBagNum) )
  ) , WouldItWork), 
  sformat(S0, '~s<td width=30 bgcolor=#ffffff>&nbsp</td>~n',[S]),
  html_tablize_cells(WouldItWork, na, S0, NewS), 
  retractall(reportSlot(_,_)).  
  
html_tablize_rows(X,[Y|Ys],CS,S) :-
  html_tablize_row(X,Y,Ss), 
  sformat(NS, '~s<tr>~s</tr>~n', [CS,Ss]),
  html_tablize_rows(X,Ys,NS,S).
  
html_tablize_row(XLabels, Y, String) :-
  bagof(Count, 
    X^(member(X,XLabels), (class_count(X,Y,Count)->true;Count=0)), 
    Bag), 
  sum(Bag, SumBag), append(Bag, [SumBag], NBag), 
  html_tablize_cells([Y|NBag], 0, "", String).
  
html_tablize_cells([Elem|List], Count, CS, Ss) :- 
  cell_color(Elem, Color), 
  (\+ Count=na 
   ->(assert(reportSlot(Count, Elem)),NewCount is Count+1)
  ;true), 
  sformat(S, '~s<td width=30 bgcolor=~w>~w</td>~n', [CS,Color,Elem]), 
  html_tablize_cells(List, NewCount, S,Ss).
html_tablize_cells([],_,S,S).

classify_cell_elem(Axis,Labels,U,L) :-
  length(Labels,Len), Div is (U-L+1)/Len, 
  classify_cell_elem1(Axis,Labels,L,Div,U).  
  
classify_cell_elem1(Axis,A,B,C,D):-once(classify_cell_elem2(Axis,A,B,C,D)).
classify_cell_elem2(Axis, [H],L,_,U):- assert(data_classify(Axis,H,L,U)).  
classify_cell_elem2(Axis, [H|T],L,Div,U):-
  LL is L+Div, assert(data_classify(Axis, H,L,LL)), 
  classify_cell_elem1(Axis, T,LL,Div,U).
  
data_classifying(FileName, IndexX, IndexY) :-  
  retractall(class_count(_X,_Y,_Count)),
  [FileName], result(_,L), 
  data_classifying1(L, IndexX, IndexY), fail.
data_classifying(_,_,_).
  
data_classifying1(L, IndexX, IndexY):-  
  nth0(IndexX,L,ElemX), 
  fit_class(x,ElemX,ClassX), 
  nth0(IndexY,L,ElemY), 
  fit_class(y,ElemY,ClassY), 
  set_count(ClassX,ClassY).
  
fit_class(A,B,C) :- once(fit_class1(A,B,C)).
  
fit_class1(Axis, Elem,Label) :- data_classify(Axis, Label, L, U), Elem>=L, Elem<U.
fit_class1(Axis, Elem,Label) :- data_classify(Axis, Label, L, L), Elem=L.
fit_class1(_, Elem, blah) :- print(Elem), nl.

set_count(ClassX,ClassY) :-
  clause(class_count(ClassX,ClassY,_), true), !, 
  class_count(ClassX,ClassY,Num),
  N is Num+1, retractall(class_count(ClassX,ClassY,Num)), 
  assert(class_count(ClassX,ClassY,N)).
set_count(ClassX,ClassY) :-
  assert(class_count(ClassX,ClassY,1)).
  
cell_color(A,B) :- once(cell_color1(A,B)).    
cell_color1(Elem, '#6699cc') :- \+ number(Elem). 
cell_color1(Elem, '#663300') :- Elem>=1000. 
cell_color1(Elem, '#996633') :- Elem>=800, Elem<1000. 
cell_color1(Elem, '#cc9966') :- Elem>=600, Elem<800. 
cell_color1(Elem, '#ff9966') :- Elem>=400, Elem<600. 
cell_color1(Elem, '#ffcc99') :- Elem>=200, Elem<400.  
cell_color1(Elem, '#ffffcc') :- Elem>=50, Elem<200.  
cell_color1(Elem, '#fffffc') :- Elem>=1, Elem<50. 
cell_color1(_Elem, '#ffffff').