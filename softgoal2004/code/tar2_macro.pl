% tar2_macro
% all about running macro-cycle and generating corresponding report 

:- load_files([main], 
  [silent(true)]).  
  
 macro_print_type(text).
 macro_output_filename('macro_result.out'). 
% input:  
% 1. list of tar2 recommanded actions in this format: [[a1, a2], [b1,b2]|Rest]
% 2. # lurches for each recommanded action(s)
% 3.  attribute type (e.g. activities) to be presented
% output:  
% 1. present frequency counts for each bottom leaves of the graph

 :- [defs/cara_analysis], [defs/cara_analysis_utils]. 
 
macro_lurches(X, Constraints, Runs, Bs,Cs,Outputs) :-
  macro_lurches(X, Constraints, 0, Runs, [], Bs,[], Cs,[], Outputs). 
macro_lurches(_,_, R,R, Bs,Bs,Cs,Cs,Outputs,Outputs):-!. 
macro_lurches(X, Constraints, Curr, Runs, CurrBs, NewBs,CurrCs, NewCs, CurrOutputs, NewOutputs):- 
  macro_lurch(X,B,C,Out),
  once(macro_lurch_case(Constraints, Curr, NewCurr, B, Bs, NewBs, C, Cs, NewCs, Out, Outputs, NewOutputs)), 
  macro_lurches(X, Constraints, NewCurr, Runs, CurrBs, Bs,CurrCs, Cs, CurrOutputs, Outputs).

macro_lurch_case(Constraints, Curr, NewCurr, B, Bs, [B|Bs], C, Cs, [C|Cs], Out, Outputs, [Out|Outputs]):-
  forall(member(O,Constraints), memo(_,O,0)), !, NewCurr is Curr +1.
macro_lurch_case(_,Curr,Curr, _, Bs, Bs, _, Cs, Cs,_,Outputs,Outputs).	
  
macro_lurch(X,B,C,Out) :- 
  reset, reset(records), 
  run(X), !, 
  costs(C), benefit(X,B),
  bagof(One, A^memo(A,One,0), Out). 
 
macro_getAttrFreqCount(AllOuts,AttrFreqCount):-
  flatten(AllOuts, Flattened), 
  sort(Flattened, SortedEmperical), 
  maplist(macro_getfcount(Flattened), SortedEmperical, AttrFreqCount).
 
macro_getfcount(List, Attr, fcount(Count,Attr)) :-
  bagof(I, nth0(I, List,Attr), Total), length(Total, Count). 
  
macro_printOne(Bs, Cs, Outs) :-
  average(Bs, AvegB), average(Cs, AvegC), 
  macro_getAttrFreqCount(Outs, AttrFreqCountO), 
  msort(AttrFreqCountO, AttrFreqCount), 
  % sieve out rules and stuff
  Wanted=fcount(C,Attr), 
  findall(Wanted, 
  A^B^(member(Wanted, AttrFreqCount), (Attr=of(A,B);Attr=not(of(A,B)))),
  WantedAttrFreqCounts), 
  macro_output_filename(FileName), 
  append(FileName), 
  ignore((
    macro_print('Average Benefits for all runs', AvegB), 
    macro_print('Average Costs for all runs', AvegC), 
    checklist(macro_print_fcount, WantedAttrFreqCounts)
  )), 
  told.
  
macro_print(Text) :-
   macro_print_type(text), 
   format('~t~w: ~t~40|~n', [Text]). 
macro_print(Text, Thing) :-
   macro_print_type(text), 
   format('~t~w: ~t~40|~w~n', [Text, Thing]). 
  
macro_print_fcount(fcount(Count, Attr)):-  
  macro_print('Frequency Count for:', Attr=Count).
  
tests:-
  macro_lurches_all(riskMinimization of system,
  [
  [dav04 of dal] ,
  [dav05 of dal] ,
  [dav06 of dal] ,
  [dav07 of dal] ,
  [dav08 of dal] ,
  [dav09 of dal] ,
  [cav06 of cal] ,
  [cav01 of cal] ,
  [cav02 of cal] ,
  [cav03 of cal] ,
  [cav04 of cal] ,
  [cav05 of cal] ,
  [dav01 of dal] ,
  [dav02 of dal] ,
  [tav08 of tal] ,
  [tav09 of tal] ,
  [dav03 of dal] 
     ],
    100).
  
macro_lurches_all(X, ConstraintsLists, RunsForEachConstraints):-
  macro_output_filename(FileName) ,
  tell(FileName),
  macro_print('Report: lurching',X), 
  macro_print('============================================'),
  told, 
  forall(member(Constraints, ConstraintsLists), 
  (
    append(FileName), 
    macro_print('lurching: ',Constraints), told, 
    macro_lurches(X,Constraints,RunsForEachConstraints,B,C,O),
    macro_printOne(B,C,O),
    append(FileName), 
    macro_print('------------------------------------------------------'), told
  )
  ).