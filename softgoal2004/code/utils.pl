% utils.pl
% misc utilities including textual output
% for TAR2

% -------------------- all about intermediate files to be manipulated ---%

make_results(A,B,C):- make_results(A,[],B,C). 
make_results(Args, ConstraintList, NumOfTimes, File):-
  reset(tar2), 
  gen_tar2_filename(File, '.pl', F),
  tell(F), told, % initialize file... any better way to do this??
  forall(
    between(1,NumOfTimes, N), 
    (make_result(Args,ConstraintList, Out), append(F), 
    format('result(~w,~w).~n', [N, Out]),  told)
  ).

make_result(X,ConstraintList, [B,C|Out]) :- 
  reset, reset(records), 
  checklist(fake_memo, ConstraintList), 
  run(X), !, 
  costs(C), benefit(X,B), 
  make_result_list(Out). 
make_result_list(Out) :-
  attributes(L), maplist(done, L, Out).  

% -------------------- all about writing tar2 files -------------------------------%
 
tar2_analyse_pl(File) :-
  gen_tar2_filename(File, '.pl', F),[F],
  tar2_analyse_pl1( 0, benefit),
  tar2_analyse_pl1( 1, cost).
%  tar2_analyse_finishup.

tar2_analyse_pldata :-
  tar2_pencentile_chop(Function), 
  once(tar2_analyse_pldata1(Function)).  

tar2_analyse_pldata1('seperate'):-
  tar2_analyse_pl1( 0, benefit),
  tar2_analyse_pl1( 1, cost). 
  
tar2_analyse_pldata1(Function):-
  tar2_analyse_pldata1_findAllClassNames(AllClassNames), 
  tar2_analyse_pldata1_calculateResults(AllOuts),   
  msort(AllOuts, SortedAllOuts), last(L,SortedAllOuts), print(L), nl, 
  length(AllOuts, Len), length(AllClassNames, NumClasses), 
  Div is truncate(Len/NumClasses),  
  tar2_analyse_assertClass( Function, AllClassNames, SortedAllOuts, Div). 
    
tar2_analyse_pldata1_findAllClassNames(FormattedAll) :-
  bagof(ClassNames, 
  ClassType^(bagof(ClassName, (class(ClassType, V, ClassName), var(V)), ClassNames)), 
  Attrs), 
  tar2_analyse_find_variations(Attrs, AllClassNames), 
  maplist(tar2_analyse_format_classname, AllClassNames, FormattedAll).

tar2_analyse_pldata1_calculateResults(AllOuts):-
  classify_function(Function, ArithList), 
  function_param_location(Function, Locations), 
  bagof(
  OneOut, 
    Count^ParamsForOneResult^(maplist(tar2_analyse_pldata1_getone(Count), Locations, ParamsForOneResult), 
    tar2_analyse_calculate(ParamsForOneResult, ArithList, OneOut)),
  AllOuts).

tar2_analyse_pldata1_getone(Count, Name=Location, Name=Param) :-
  result(Count,L), nth0(Location, L, Param). 

tar2_analyse_pl1( Index, ClassType) :- 
  tar2_analyse_sortClass(Index, ClassType, ClassNames, MSortedData, Div), 
  tar2_analyse_assertClass( ClassType, ClassNames, MSortedData, Div). 

tar2_analyse_sortClass(Index, BorC, Classes, MSBs, Div):-
  bagof(Elem, Count^L^(result(Count,L), nth0(Index, L, Elem)), Elems), 
  msort(Elems, MSBs), % get sorted benefits
  findall(Class, V^(class(BorC,_,Class), var(V)), Classes), % get all benefit class types
  length(Elems, Len), length(Classes, NumClasses), 
  Div is truncate(Len/NumClasses).
  
tar2_analyse_assertClass( Name, A,B,C):-
  tar2_analyse_assertClass( Name, A,B,C,0,C).
tar2_analyse_assertClass( Name, [One],MSBs,_,MinP,_) :-
  last(Max,MSBs), nth0(MinP,MSBs,Min), 
  bassert(curr_class(Name, Min, Max, One)). 
tar2_analyse_assertClass( Name, [BC|BCs], MSBs, Div, MinP, MaxP):-
  nth0(MinP,MSBs,Min), nth0(MaxP,MSBs,Max),    
  bassert(curr_class(Name, Min, Max, BC)), 
  NMinP is MaxP+1, NMaxP is MaxP+Div, 
  tar2_analyse_assertClass( Name, BCs, MSBs, Div, NMinP, NMaxP). 
tar2_analyse_assertClass(_,[],_,_,_,_). 

tar2_analyse_finishup :- tar2_pencentile_chop(A), once(tar2_analyse_finishup1(A)).

tar2_analyse_finishup1('seperate').

tar2_analyse_finishup1(ClassifyType):-
  setof(ClassType, A^B^C^curr_class(ClassType,A,B,C), ClassTypes), 
  bagof(Attr, 
    (member(OneClassType, ClassTypes), 
    setof( 
      OneClassType/Min/Max/ClassName,  
      OneClassType^curr_class(OneClassType, Min, Max, ClassName),
      Attr)
    ), 
    Attrs), 
  tar2_analyse_finishup2(ClassifyType, Attrs).  
  
tar2_analyse_finishup2(ClassifyType, Attrs):-
  tar2_analyse_find_variations(Attrs, Variations), 
  classify_function(ClassifyType, List), 
  forall(member(V, Variations), tar2_analyse_finishup3(ClassifyType, List, V)).  
  
tar2_analyse_find_variations(Attrs, Variations):-
  bagof(V, tar2_analyse_find_variation(Attrs,V), Variations).  
    
tar2_analyse_find_variation(Attrs, V):-
    tar2_analyse_find_variation(Attrs, [], V).  
 tar2_analyse_find_variation([],O,O).
 tar2_analyse_find_variation([Attr|Attrs], Vs, [One|Out]) :-
   member(One, Attr), tar2_analyse_find_variation(Attrs, Vs, Out).
   
tar2_analyse_finishup3(ClassifyType, List, ParamSets) :-
  bagof(
    ClassType=Min, 
    Max^ClassName^member(ClassType/Min/Max/ClassName, ParamSets), 
    ParamMin), 
  bagof(
    ClassType=Max, 
    Min^ClassName^member(ClassType/Min/Max/ClassName, ParamSets), 
    ParamMax), 
  setof(ClassName, A^B^C^member(A/B/C/ClassName, ParamSets), ClassNames), 
  msort(ClassNames, CNS), tar2_analyse_format_classname(CNS, FormattedCNS), 
  tar2_analyse_calculate(ParamMin,List,Min), 
  tar2_analyse_calculate(ParamMax,List,Max), 
  msort([Min,Max], [NMin,NMax]), 
  bassert(curr_class(ClassifyType, NMin, NMax,FormattedCNS)). 

tar2_analyse_format_classname(ClassName, Formatted) :-
  tar2_analyse_format_classname(ClassName, '', Formatted). 
  
tar2_analyse_format_classname([OneC], Curr, Out) :-
  atom_concat(OneC, Curr, Out). 
tar2_analyse_format_classname([OneC|Cs], Curr, Out) :-
  tar2_analyse_format_classname(Cs, Curr, O1), 
  atom_concat('=',O1,O2), atom_concat(OneC,O2,Out).

tar2_analyse_calculate(A,B,C):- 
  once(tar2_analyse_calculate1(A,B,C)).
tar2_analyse_calculate1(_, List, List):- \+ is_list(List).  
tar2_analyse_calculate1(Params, List, Out) :- % Params=[cost=1, benefit=2.34]
  checklist(atomic, List), 
  tar2_analyse_calculate3(Params, List, Out).  
  
tar2_analyse_calculate1(Params, List, Out):-
  maplist(tar2_analyse_calculate1(Params), List, NewList), 
  tar2_analyse_calculate3(Params, NewList, Out).  
  
tar2_analyse_calculate3(Params, List, Result):-
  maplist(tar2_analyse_calculate4(Params), List, Callable), 
  Unif =.. Callable, call(Unif,Result).  
  
tar2_analyse_calculate4(Params, ClassType, Number):-
  member(ClassType=Number, Params). 
  
tar2_analyse_calculate4(_, Others, Others). 
  
tar2_write_name_file(File) :-
  gen_tar2_filename(File, '.names', FileName),
  tar2_pencentile_chop(FunctionName), 
  bagof(C, X0^X1^(classify(FunctionName,X0,X1,C)), [HC|Cs]), 
  attributes(L), 
  bagof(One=AType, (member(One, L), attribute_type(One,AType)), LL), 
  tell(FileName), ignore(( % absolute laziness...
    format('~w', [HC]), forall(member(OneC,Cs), format(',~w',[OneC])),
    format('~n'), forall(member(O=A, LL), format('~w: ~t~10|~w~n',[O,A]))
  )), told. 

tar2_write_data_file(File) :-
  gen_tar2_filename(File, '.data', FileName),
  tell(FileName), told, 
  tar2_pencentile_chop(FunctionName), 
  forall(
    result(_,[B,C|R]), 
    (  classify(FunctionName,C,B,CB), 
      append(FileName), 
      checklist(tar2_write_data_file1, R),
      format('~w.~n', [CB]), 
      told
    )
  ).
    
tar2_write_data_file1(B) :- format('~w, ~t', [B]). 

gen_tar2_filename(File, Extention, FileName):-
  tar2_directory(D), (\+ exists_directory(D)->make_directory(D);true), 
  atom_concat(D, '/', DD), 
  atom_concat(DD,File,DF), atom_concat(DF, Extention, FileName). 
