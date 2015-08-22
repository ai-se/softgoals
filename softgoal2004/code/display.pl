% display.pl
% configuration file for all visible stuff

displaying(depends_on=[arrowhead='normal']). 
displaying(means=[arrowhead='open']). 
displaying(consists_of=[arrowhead='tee']). 
displaying(contributions=[arrowhead='inv']). 
displaying(and=[label='and']).  
displaying(or=[label='or']).  
displaying(all_of=[label='all_of']).  
displaying(none_of=[label='none_of']).  
displaying(any_of=[label='any_of']).  
displaying(any_one_of=[label='any_one_of']).  
displaying(one_of=[label='one_of']).  
displaying(made=[label='++']).  
displaying(helped=[label='+']).  
displaying(unhurt=[label='-']).  
displaying(unbroken=[label='--']). 
displaying((with)=[label='claim to effect']). 
displaying((intermediate)=[arrowhead='inv']). 

% ------------------------------added for cara------------------------------%
displaying(catastrophically_rated=[label='4']).  
displaying(critically_rated=[label='3']).  
displaying(highly_rated=[label='3']). 
displaying(moderately_rated=[label='2']).  
displaying(lowly_rated=[label='1']). 
displaying(positively_influenced=[label='?']).  
% ------------------------------added for cara------------------------------%

displaying((softgoal)=[shape=doubleoctagon]). 
displaying((goal)=[shape=octagon]). 
displaying((task)=[shape=hexagon]).  
displaying((resource)=[shape=box]). 
displaying((actor)=[shape=circle]). 
displaying((claim)=[shape=triangle]). 
displaying((stakeholder)=[shape=triangle]). 
displaying((intermediate_node)=[label='i']). 

display_gen(R, Out):- 
  display_gen1(R, Temp), 
  display_gen2(Temp, Out).  
display_gen1(A^B, [O1,O2]):- !, 
  display_gen1(A, O1), display_gen1(B, O2). 
display_gen1(A, Out) :- displaying(A=Out).  
display_gen2(L, Out) :-
  flatten(L, NewL), setof(T, Junk^(member(T=Junk,NewL)), Ts), 
  maplist(display_gen3(NewL), Ts, Out).  
  
display_gen3(All, T, PrettyJunks) :-
  setof(Junk, member(T=Junk, All), Junks), 
  display_gen4(T, Junks, PrettyJunks).  

display_gen4(label, Raw, label=S) :- 
  sformat(S, '~w', [Raw]).
display_gen4(Tag, [Raw], Tag=Raw).  
display_gen4(_,_,'label="undefined"').  
  