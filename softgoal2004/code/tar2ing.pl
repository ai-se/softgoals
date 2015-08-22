:- multifile test/1, preteston/2, preteston/3, tar2/1, tar2/2. 	

:- load_files([main], 
  [silent(true)]).  
  
tar2(arch_def):- 
  tar2_write_name_file('arch_def'), 
  time(make_results(goodness of system, 10000, 'arch_def')), 
  tar2_analyse_pl('arch_def'), 
  tar2_write_data_file('arch_def'). 

tar2(cara_analysis):- 
%  tar2_write_name_file('cara_analysis'), 
  time(make_results(riskMinimization of system, 10000, 'cara_analysis')), 
  tar2_analyse_pl('cara_analysis'), 
  tar2_write_data_file('cara_analysis'). 
  
tar2(credit_card_authorize):- 
%  tar2_write_name_file('credit_card_authorize'), 
  time(make_results(performance of authorize(card, money), 10000, 'credit_card_authorize')), 
  tar2_analyse_pl('credit_card_authorize'), 
  tar2_write_data_file('credit_card_authorize'). 
  
tar2(arch_patterns):- 
%  tar2_write_name_file('arch_patterns'), 
  time(make_results(goodness of system, 10000, 'arch_patterns')), 
  tar2_analyse_pl('arch_patterns'), 
  tar2_write_data_file('arch_patterns'). 
  
tar2(arch_def,CList):- 
  make_results(goodness of system, CList, 10000, 'arch_def'), 
  tar2_analyse_pl('arch_def'), 
  tar2_write_data_file('arch_def'). 

tar2(credit_card_authorize,CList):- 
  make_results(performance of authorize(card, money), CList, 10000, 'credit_card_authorize'), 
  tar2_analyse_pl('credit_card_authorize'), 
  tar2_write_data_file('credit_card_authorize'). 
   
tar2(arch_patterns,CList):- 
  make_results(goodness of system, CList, 10000, 'arch_patterns'), 
  tar2_analyse_pl('arch_patterns'), 
  tar2_write_data_file('arch_patterns'). 
  
% :- [defs/arch_def], [defs/arch_def_utils]. 
% :- [defs/cara_analysis], [defs/cara_analysis_utils]. 
 :- [defs/credit_card_authorize], [defs/credit_card_authorize_utils]. 
%:- [defs/arch_patterns], [defs/arch_patterns_utils]. 

% incremental simulation for rigorous qa:  to get better
incsim(1) :- tar2(arch_def, [sharedData of targetSystem]). 
incsim(2) :- tar2(arch_def, [implicitInvocation of targetSystem,sharedData of targetSystem]). 
incsim(3) :- tar2(arch_def, [abstractDataType of targetSystem, c3, implicitInvocation of targetSystem,sharedData of targetSystem]). 

% incremental simulation for loose qa:  to get worse
incsim(4) :- tar2(arch_def, [c4, not pipeAndFilter of targetSystem]). 
incsim(5) :- tar2(arch_def, [c3, c4, not pipeAndFilter of targetSystem]). 
incsim(6) :- tar2(arch_def, [c2, c3, c4, not pipeAndFilter of targetSystem]). 
incsim(7) :- tar2(arch_def, [not implicitInvocation of targetSystem, c2, c3, c4, not pipeAndFilter of targetSystem]). 

% incremental simulation for orororany:  to get better
incsim(8) :-  tar2(arch_def, [not abstractDataType of targetSystem]). 
incsim(9) :-  tar2(arch_def, [not abstractDataType of targetSystem, c2]). 
incsim(10) :-  tar2(arch_def, [not abstractDataType of targetSystem, c2, not implicitInvocation of targetSystem]). 
incsim(11) :-  tar2(arch_def, [not abstractDataType of targetSystem, c2, not implicitInvocation of targetSystem, not pipeAndFilter of targetSystem]). 

% incremental simulation for orororany:  to get worse
incsim(12) :- tar2(arch_def, [not pipeAndFilter of targetSystem]). 
incsim(13) :- tar2(arch_def, [not pipeAndFilter of targetSystem, c4]). 
incsim(14) :- tar2(arch_def, [not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem]). 
incsim(15) :- tar2(arch_def, [not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, not c5]). 
incsim(16) :- tar2(arch_def, [not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, not c5, c1]). 
incsim(17) :- tar2(arch_def, [not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, not c5, c1, c2]). 
incsim(18) :- tar2(arch_def, [not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, not c5, c1, c2, not abstractDataType of targetSystem]). 

% incremental simulation for anyanyanyor: to get better
incsim(19) :- tar2(arch_def, [implicitInvocation of targetSystem]). 
incsim(20) :- tar2(arch_def, [implicitInvocation of targetSystem, c3]). 
incsim(21) :- tar2(arch_def, [implicitInvocation of targetSystem, c3,abstractDataType of targetSystem]). 
incsim(22) :- tar2(arch_def, [implicitInvocation of targetSystem, c3,abstractDataType of targetSystem, sharedData of targetSystem]). 

% incremental simulation for anyanyanyor:  to get worse
incsim(23) :- tar2(arch_def, [not pipeAndFilter of targetSystem, c4]). 
incsim(24) :- tar2(arch_def, [not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, c3]). 
incsim(25) :- tar2(arch_def, [not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, c3, c2]). 
incsim(26) :- tar2(arch_def, [not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, c3, c2, sharedData of targetSystem]). 
incsim(27) :- tar2(arch_def, [not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, c3, c2, sharedData of targetSystem, not c5]). 

% incremental simulation for credit_card_authorize (all-and), to get better
incsim(100) :- tar2(credit_card_authorize, 
  [performFirst of retrieve(card*creditRemaining)at layer([3, operationComponents])
  ]). 
incsim(101) :- tar2(credit_card_authorize, 
  [performFirst of retrieve(card*creditRemaining)at layer([3, operationComponents]),
  earlyFixing of status at layer(2)
  ]). 
incsim(102) :- tar2(credit_card_authorize, 
  [performFirst of retrieve(card*creditRemaining)at layer([3, operationComponents]),
  earlyFixing of status at layer(2),
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents])
  ]). 
  
incsim(103) :- tar2(credit_card_authorize, 
  [performFirst of retrieve(card*creditRemaining)at layer([3, operationComponents]),
  earlyFixing of status at layer(2),
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  severalAttributesPerTuple at layer([4, prioritization])
  ]). 
  
incsim(104) :- tar2(credit_card_authorize, 
  [performFirst of retrieve(card*creditRemaining)at layer([3, operationComponents]),
  earlyFixing of status at layer(2),
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  severalAttributesPerTuple at layer([4, prioritization]),
  performFirst of commonCode(authorize)at layer([4, commonCode])
  ]). 
  
incsim(105) :- tar2(credit_card_authorize, 
  [performFirst of retrieve(card*creditRemaining)at layer([3, operationComponents]),
  earlyFixing of status at layer(2),
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  severalAttributesPerTuple at layer([4, prioritization]),
  performFirst of commonCode(authorize)at layer([4, commonCode]),
  lateFixing of otherAttrs at layer(2)
  ]). 
incsim(106) :- tar2(credit_card_authorize, 
  [performFirst of retrieve(card*creditRemaining)at layer([3, operationComponents]),
  earlyFixing of status at layer(2),
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  severalAttributesPerTuple at layer([4, prioritization]),
  performFirst of commonCode(authorize)at layer([4, commonCode]),
  lateFixing of otherAttrs at layer(2),
  fewAttributePerTuple of (card*status)at layer([2, operationComponents])
  ]). 
  
% incremental simulation for credit_card_authorize (all-and), to get better
incsim(credit_card_authorize, all_and, better, 1) :- tar2(credit_card_authorize, [not earlyFixing of status at layer(2)]). 
incsim(credit_card_authorize, all_and, better, 2) :- tar2(credit_card_authorize, [not earlyFixing of status at layer(2),'status needed quickly to stop fraud' at layer(2)]). 
incsim(credit_card_authorize, all_and, better, 3) :- tar2(credit_card_authorize, [not earlyFixing of status at layer(2),'status needed quickly to stop fraud' at layer(2),'status not specialized' at layer([4, prioritization])]). 
incsim(credit_card_authorize, all_and, better, 4) :- tar2(credit_card_authorize, [not earlyFixing of status at layer(2),'status needed quickly to stop fraud' at layer(2),'status not specialized' at layer([4, prioritization]),not 'inherited code predominates authorization' at layer([4, commonCode])]). 
incsim(credit_card_authorize, all_and, better, 5) :- tar2(credit_card_authorize, [not earlyFixing of status at layer(2),'status needed quickly to stop fraud' at layer(2),'status not specialized' at layer([4, prioritization]),not 'inherited code predominates authorization' at layer([4, commonCode]),  not 'otherAttrs use most space' at layer([4, individualAttributes])]). 

incsim(1061) :- tar2(credit_card_authorize, 
    ['status needed quickly to stop fraud' at layer(2), 
  not earlyFixing of status at layer(2),
  not 'otherAttrs use most space' at layer([4, individualAttributes]),
  'status not specialized' at layer([4, prioritization])
  ]). 

incsim(107) :- tar2(credit_card_authorize, 
    ['status needed quickly to stop fraud' at layer(2), 
  not earlyFixing of status at layer(2),
  not 'otherAttrs use most space' at layer([4, individualAttributes]),
  'status not specialized' at layer([4, prioritization]), 
  not 'inherited code predominates authorization' at layer([4, commonCode])
  ]). 

% incremental simulation for credit_card_authorize (any_any_ands), to get better
incsim(1101) :- tar2(credit_card_authorize, 
  [
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents])
  ]). 
incsim(1102) :- tar2(credit_card_authorize, 
  [
  'disallow bad cards' at layer([3, operationComponents]), 
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  not lateFixing of otherAttrs at layer(2)
  ]). 
incsim(1103) :- tar2(credit_card_authorize, 
  [
  'disallow bad cards' at layer([3, operationComponents]), 
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  not lateFixing of otherAttrs at layer(2),
  earlyFixing of status at layer(2)
  ]). 
incsim(1104) :- tar2(credit_card_authorize, 
  [
  'disallow bad cards' at layer([3, operationComponents]), 
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  not lateFixing of otherAttrs at layer(2),
  earlyFixing of status at layer(2),
  performFirst of update(card*creditRemaining)at layer([3, operationComponents])
  ]). 
incsim(1105) :- tar2(credit_card_authorize, 
  [
  'disallow bad cards' at layer([3, operationComponents]), 
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  not lateFixing of otherAttrs at layer(2),
  earlyFixing of status at layer(2),
  performFirst of update(card*creditRemaining)at layer([3, operationComponents]),
  severalAttributesPerTuple at layer([4, prioritization])
  ]). 

% incremental simulation for credit_card_authorize (any_any_ands), to get worse
incsim(1106) :- tar2(credit_card_authorize, 
  [
  lateFixing of otherAttrs at layer(2)
  ]). 
incsim(1107) :- tar2(credit_card_authorize, 
  [
  lateFixing of otherAttrs at layer(2),
  'other Attrs not accessed during critical operations' at layer(2)
  ]). 
  
incsim(1108) :- tar2(credit_card_authorize, 
  [
  lateFixing of otherAttrs at layer(2),
  'other Attrs not accessed during critical operations' at layer(2),
  severalAttributesPerTuple at layer([4, prioritization])
  ]). 
incsim(1109) :- tar2(credit_card_authorize, 
  [
  lateFixing of otherAttrs at layer(2),
  'other Attrs not accessed during critical operations' at layer(2),
  severalAttributesPerTuple at layer([4, prioritization]),
  'otherAttrs use most space' at layer([4, individualAttributes])
  ]). 

% incremental simulation for credit_card_authorize (any_any_ors), to get better
incsim(1201) :- tar2(credit_card_authorize, 
  [
  not lateFixing of otherAttrs at layer(2)
  ]). 
incsim(1202) :- tar2(credit_card_authorize, 
  [
  not lateFixing of otherAttrs at layer(2),
  not 'other not important' at layer([3, operationComponents])
  ]). 
incsim(1203) :- tar2(credit_card_authorize, 
  [
  not lateFixing of otherAttrs at layer(2),
  'other not important' at layer([3, operationComponents]),
  not 'inherited code predominates authorization' at layer([4, commonCode])
  ]). 
incsim(1204) :- tar2(credit_card_authorize, 
  [
  not lateFixing of otherAttrs at layer(2),
  'other not important' at layer([3, operationComponents]),
  not 'inherited code predominates authorization' at layer([4, commonCode]),
  not earlyFixing of status at layer(2) 
  ]). 

% incremental simulation for credit_card_authorize (any_any_ors), to get worse
incsim(1211) :- tar2(credit_card_authorize, 
  [
  fewAttributePerTuple of (card*status)at layer([2, operationComponents])
  ]). 
incsim(1212) :- tar2(credit_card_authorize, 
  [
  fewAttributePerTuple of (card*status)at layer([2, operationComponents]),
  'disallow bad cards' at layer([3, operationComponents])
  ]). 
incsim(1213) :- tar2(credit_card_authorize, 
  [
  fewAttributePerTuple of (card*status)at layer([2, operationComponents]),
  'disallow bad cards' at layer([3, operationComponents]),
  performFirst of retrieve(card*status)at layer([3, operationComponents])
  ]). 
incsim(1214) :- tar2(credit_card_authorize, 
  [
  fewAttributePerTuple of (card*status)at layer([2, operationComponents]),
  'disallow bad cards' at layer([3, operationComponents]),
  performFirst of retrieve(card*status)at layer([3, operationComponents]),
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents])
  ]). 

incsim(1215) :- tar2(credit_card_authorize, 
  [
  fewAttributePerTuple of (card*status)at layer([2, operationComponents]),
  'disallow bad cards' at layer([3, operationComponents]),
  performFirst of retrieve(card*status)at layer([3, operationComponents]),
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  'do not exceed credit limit' at layer([3, operationComponents])
  ]). 
incsim(1216) :- tar2(credit_card_authorize, 
  [
  fewAttributePerTuple of (card*status)at layer([2, operationComponents]),
  'disallow bad cards' at layer([3, operationComponents]),
  performFirst of retrieve(card*status)at layer([3, operationComponents]),
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  'do not exceed credit limit' at layer([3, operationComponents]),
  'inherited code predominates authorization' at layer([4, commonCode])
  ]). 

incsim(1217) :- tar2(credit_card_authorize, 
  [
  fewAttributePerTuple of (card*status)at layer([2, operationComponents]),
  'disallow bad cards' at layer([3, operationComponents]),
  performFirst of retrieve(card*status)at layer([3, operationComponents]),
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  'do not exceed credit limit' at layer([3, operationComponents]),
  'inherited code predominates authorization' at layer([4, commonCode]),
  'status not specialized' at layer([4, prioritization])
  ]). 
incsim(1218) :- tar2(credit_card_authorize, 
  [
  fewAttributePerTuple of (card*status)at layer([2, operationComponents]),
  'disallow bad cards' at layer([3, operationComponents]),
  performFirst of retrieve(card*status)at layer([3, operationComponents]),
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  'do not exceed credit limit' at layer([3, operationComponents]),
  'inherited code predominates authorization' at layer([4, commonCode]),
  'status not specialized' at layer([4, prioritization]),
  not 'otherAttrs use most space' at layer([4, individualAttributes])
  ]). 
incsim(1219) :- tar2(credit_card_authorize, 
  [
  fewAttributePerTuple of (card*status)at layer([2, operationComponents]),
  'disallow bad cards' at layer([3, operationComponents]),
  performFirst of retrieve(card*status)at layer([3, operationComponents]),
  replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  'do not exceed credit limit' at layer([3, operationComponents]),
  'inherited code predominates authorization' at layer([4, commonCode]),
  'status not specialized' at layer([4, prioritization]),
  not 'otherAttrs use most space' at layer([4, individualAttributes]),
  earlyFixing of status at layer(2)
  ]). 
% incremental simulation for credit_card_authorize (any_any_anys), to get better
incsim(1301) :- tar2(credit_card_authorize, 
  [
  not 'inherited code predominates authorization' at layer([4, commonCode])
  ]). 
incsim(1302) :- tar2(credit_card_authorize, 
  [
  not 'inherited code predominates authorization' at layer([4, commonCode]),
  not earlyFixing of status at layer(2)
  ]). 
incsim(1303) :- tar2(credit_card_authorize, 
  [
  not 'inherited code predominates authorization' at layer([4, commonCode]),
  not earlyFixing of status at layer(2),
  'status needed quickly to stop fraud' at layer(2)

  ]). 
incsim(1304) :- tar2(credit_card_authorize, 
  [
  not 'inherited code predominates authorization' at layer([4, commonCode]),
  not earlyFixing of status at layer(2),
  'status needed quickly to stop fraud' at layer(2),
  'status not specialized' at layer([4, prioritization])
  ]). 
incsim(1305) :- tar2(credit_card_authorize, 
  [
  not 'inherited code predominates authorization' at layer([4, commonCode]),
  not earlyFixing of status at layer(2),
  'status needed quickly to stop fraud' at layer(2),
  'status not specialized' at layer([4, prioritization]),
  not 'otherAttrs use most space' at layer([4, individualAttributes])
  ]). 
% incremental simulation for credit_card_authorize (any_any_anys), to get worse
incsim(1311) :- tar2(credit_card_authorize, 
  [
  not replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents])
  ]). 
incsim(1312) :- tar2(credit_card_authorize, 
  [
  not replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents]),
  not lateFixing of otherAttrs at layer(2)
  ]). 

% incremental simulation for arch_patterns_any2_ands to get better
%incsim(arch_patterns,better,1) :- tar2(arch_patterns, [not co_optation of archPattern]). 

% incremental simulation for arch_patterns_any_ors to get worse
incsim(arch_patterns_any_ors,worse,1) :- tar2(arch_patterns, ['external agents can aquire trusted information']). 
incsim(arch_patterns_any_ors,worse,2) :- tar2(arch_patterns, ['external agents can aquire trusted information',co_optation of archPattern]). 
% incremental simulation for arch_patterns_any_ors to get better
incsim(arch_patterns_any_ors,better,1) :- tar2(arch_patterns, [jointVenture of archPattern]). 
incsim(arch_patterns_any_ors,better,2) :- tar2(arch_patterns, [co_optation of archPattern]). 
incsim(arch_patterns_any_ors,better,3) :- tar2(arch_patterns, [pyramid of archPattern]). 

% incremental simulation for arch_patterns_anys to get better
incsim(arch_patterns_anys,better,1) :- tar2(arch_patterns, [co_optation of archPattern]). 
% incremental simulation for arch_patterns_anys to get worse
incsim(arch_patterns_anys,worse,1) :- tar2(arch_patterns, [not 'external agents can aquire trusted information']). 
incsim(arch_patterns_anys,worse,2) :- tar2(arch_patterns, [not 'external agents can aquire trusted information',not co_optation of archPattern]). 

% trials are for odd .names file   
% trials for rigorous qa:  to get better
trial(0) :- tar2(arch_def). 
trial(1) :- tar2(arch_def, [not pipeAndFilter of targetSystem]). 
trial(2) :- tar2(arch_def, [not c5, not abstractDataType of targetSystem, not pipeAndFilter of targetSystem]). 
trial(3) :- tar2(arch_def, [not implicitInvocation of targetSystem, not c5, not abstractDataType of targetSystem, not pipeAndFilter of targetSystem]). 
     
% trials for rigorous qa:  to get worse
trial(4) :- tar2(arch_def, [c3,abstractDataType of targetSystem]). 
trial(5) :- tar2(arch_def, [pipeAndFilter of targetSystem,c3,abstractDataType of targetSystem]). 
trial(6) :- tar2(arch_def, [sharedData of targetSystem,pipeAndFilter of targetSystem,c3,abstractDataType of targetSystem]). 

% trials for loose qa:  to get better
trial(7) :- tar2(arch_def, [c2,not c5, not sharedData of targetSystem]). 

% trials for loose qa:  to get worse
trial(8) :- tar2(arch_def, [c3]).
trial(9) :- tar2(arch_def, [c3,abstractDataType of targetSystem]).
trial(10) :- tar2(arch_def, [sharedData of targetSystem,c3,abstractDataType of targetSystem]).
trial(11) :- tar2(arch_def, [c4, not pipeAndFilter of targetSystem,sharedData of targetSystem,c3,abstractDataType of targetSystem]).


present(PageTitle, Titles, BenefitL, XU,XL,YU,YL,WildCard, OutFile) :-
  CostL=[  cost=0,cost=1,cost=2,cost=3,cost=4,cost=5],
  present(PageTitle, Titles, BenefitL, CostL, XU,XL,YU,YL,WildCard, OutFile). 
  
present(PageTitle, Titles, BenefitL, CostL, XU,XL,YU,YL,WildCard, OutFile) :-
  expand_file_name(WildCard, L), 
  html_tables(L,Titles,
  BenefitL,
  CostL,
  XU,XL,YU,YL, 
  %350, 0, 5, 0, 
  0, 1, String), 
  tell(OutFile), 
  format('<html><body><p>~w ~n ~s</body></html>', [PageTitle, String]), 
  told.

pretest(FileName) :-   
   [FileName], 
   assert(data(max, -1)), 
   assert(data(min, 100000)),
   findMinMax1(0), 
   listing(data).

test(0):-present('rigorous qa for weird:  to get better', 
  [  'no treatment',
     'not pipeAndFilter of targetSystem',
     'not c5, not abstractDataType of targetSystem, not pipeAndFilter of targetSystem',
     'not implicitInvocation of targetSystem, not c5, not abstractDataType of targetSystem, not pipeAndFilter of targetSystem'], 
  [   b=<2.3333,
      b=<4.6667,
      b=<7,
      b=<9.3333,
      b=<11.6667,
      b=<14,
      b=<16.3333,
      b=<18.6667,
      b=<21,
      b=<23.3333,
      b=<25.6667,
      b=<27], 27, 0, 5, 0, 
     'tar2/test/rigorous_weird/better/data*/*.pl', 'rigourous_better.html').
     
preteston(1,1) :- pretest('tar2/test/rigorous_weird/worse/data01/arch_def'). 
preteston(1,2) :- pretest('tar2/test/rigorous_weird/worse/data02/arch_def'). 
preteston(1,3) :- pretest('tar2/test/rigorous_weird/worse/data03/arch_def'). 
preteston(1,4) :- pretest('tar2/test/rigorous_weird/worse/data04/arch_def'). 

test(1):-present('rigorous qa weird:  to get worse', 
  [  'no treatment',
     'c3,abstractDataType of targetSystem',
     'c4,c3,abstractDataType of targetSystem',
     'sharedData of targetSystem,pipeAndFilter of targetSystem,c3,abstractDataType of targetSystem'], 
  [   b=<2.41667,
      b=<4.8333,
      b=<7.25,
      b=<9.6667,
      b=<12.0833,
      b=<14.5,
      b=<16.9167,
      b=<19.3333,
      b=<21.75,
      b=<24.1667,
      b=<26.5833,
      b=<28], 28, 0, 5, 0, 
     'tar2/test/rigorous_weird/worse/data*/*.pl', 'rigourous_worse.html').
     
preteston(2,1) :- pretest('tar2/test/loose_weird/worse/data01/arch_def'). 
preteston(2,2) :- pretest('tar2/test/loose_weird/worse/data02/arch_def'). 
preteston(2,3) :- pretest('tar2/test/loose_weird/worse/data03/arch_def'). 
preteston(2,4) :- pretest('tar2/test/loose_weird/worse/data04/arch_def'). 
preteston(2,5) :- pretest('tar2/test/loose_weird/worse/data05/arch_def'). 

test(2):-present('loose qa, weird .names:  to get worse', 
  [  'no treatment',
     'c3',
     'c3,abstractDataType of targetSystem',
     'sharedData of targetSystem,c3,abstractDataType of targetSystem',
     'c4, not pipeAndFilter of targetSystem,sharedData of targetSystem,c3,abstractDataType of targetSystem'], 
  [   b=<7.66667,
      b=<15.3333,
      b=<23,
      b=<30.6667,
      b=<38.3333,
      b=<46,
      b=<53.6667,
      b=<61.3333,
      b=<69,
      b=<76.6667,
      b=<84.3333,
      b=<91], 91, 0, 5, 0, 
     'tar2/test/loose_weird/worse/data*/*.pl', 'loose_worse_weirdname.html').

% for rigorous qa: to get better
preteston(3,1) :- pretest('tar2/test/rigorous/better/data01/arch_def'). 
preteston(3,2) :- pretest('tar2/test/rigorous/better/data02/arch_def'). 
preteston(3,3) :- pretest('tar2/test/rigorous/better/data03/arch_def'). 
preteston(3,4) :- pretest('tar2/test/rigorous/better/data04/arch_def'). 

test(3):-present('rigorous qa:  to get better', 
  [  'no treatment',
     'sharedData of targetSystem',
     'implicitInvocation of targetSystem,sharedData of targetSystem',
     'abstractDataType of targetSystem, c3, implicitInvocation of targetSystem,sharedData of targetSystem'], 
  [   b=<2.75,
      b=<5.5,
      b=<8.25,
      b=<11,
      b=<13.75,
      b=<16.5,
      b=<19.25,
      b=<22,
      b=<24.75,
      b=<27.5,
      b=<30.25,
      b=<32], 32, 0, 5, 0, 
     'tar2/test/rigorous/better/data*/*.pl', 'rigourous_better.html').
     
% for loose qa: to get worse
preteston(4,1) :- pretest('tar2/test/loose/worse/data01/arch_def'). 
preteston(4,2) :- pretest('tar2/test/loose/worse/data02/arch_def'). 
preteston(4,3) :- pretest('tar2/test/loose/worse/data03/arch_def'). 
preteston(4,4) :- pretest('tar2/test/loose/worse/data04/arch_def'). 
preteston(4,5) :- pretest('tar2/test/loose/worse/data05/arch_def'). 

test(4):-present('loose qa:  to get worse', 
  [  'no treatment',
     'c4, not pipeAndFilter of targetSystem', 
     'c4,c3,abstractDataType of targetSystem',
     'c2,c4,c3,abstractDataType of targetSystem',
     'not implicitInvocation of targetSystem,c2,c4,c3,abstractDataType of targetSystem'], 
  [   b=<7.33,
      b=<14.67,
      b=<22,
      b=<29.33,
      b=<36.67,
      b=<44,
      b=<51.33,
      b=<58.67,
      b=<66,
      b=<73.33,
      b=<80.67,
      b=<87], 87, 0, 5, 0, 
     'tar2/test/loose/worse/data*/*.pl', 'loose_worse.html').
     
% for orororany:  better
preteston(5,1) :- pretest('tar2/arch_def/or3any/better/0/arch_def'). 
preteston(5,2) :- pretest('tar2/arch_def/or3any/better/1/arch_def'). 
preteston(5,3) :- pretest('tar2/arch_def/or3any/better/2/arch_def'). 
preteston(5,4) :- pretest('tar2/arch_def/or3any/better/3/arch_def'). 
preteston(5,5) :- pretest('tar2/arch_def/or3any/better/4/arch_def'). 


test(5):-present('orororany:  to get better', 
  [  'no treatment',
     'not abstractDataType of targetSystem', 
     'not abstractDataType of targetSystem, c2',
     'not abstractDataType of targetSystem, c2, not implicitInvocation of targetSystem',
     'not abstractDataType of targetSystem, c2, not implicitInvocation of targetSystem, not pipeAndFilter of targetSystem'], 
  [   b=<3.25,
      b=<6.5,
      b=<9.75,
      b=<13,
      b=<16.25,
      b=<19.5,
      b=<22.75,
      b=<26,
      b=<29.25,
      b=<32.5,
      b=<35.75,
      b=<38], 38, 0, 5, 0, 
     'tar2/arch_def/or3any/better/*/arch_def.pl', 'tar2/arch_def/or3any/better/orororany_better.html').
     
% for orororany:  worse
preteston(6,1) :- pretest('tar2/arch_def/or3any/worse/0/arch_def'). 
preteston(6,2) :- pretest('tar2/arch_def/or3any/worse/1/arch_def'). 
preteston(6,3) :- pretest('tar2/arch_def/or3any/worse/2/arch_def'). 
preteston(6,4) :- pretest('tar2/arch_def/or3any/worse/3/arch_def'). 
preteston(6,5) :- pretest('tar2/arch_def/or3any/worse/4/arch_def'). 
preteston(6,6) :- pretest('tar2/arch_def/or3any/worse/5/arch_def'). 
preteston(6,7) :- pretest('tar2/arch_def/or3any/worse/6/arch_def'). 

test(6):-present('orororany:  to get worse', 
  [  'no treatment',
     'not pipeAndFilter of targetSystem', 
     'not pipeAndFilter of targetSystem, c4',
     'not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem', 
     'not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, not c5',
     'not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, not c5, c1', 
     'not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, not c5, c1, c2', 
     'not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, not c5, c1, c2, not abstractDataType of targetSystem'
     ], 
  [   b=<2.67,
      b=<5.33,
      b=<8,
      b=<10.67,
      b=<13.33,
      b=<16,
      b=<18.67,
      b=<21.33,
      b=<24,
      b=<26.67,
      b=<29.33,
      b=<31], 31, 0, 5, 0, 
     'tar2/arch_def/or3any/worse/*/arch_def.pl', 'tar2/arch_def/or3any/worse/orororany_worse.html').
     
% for anyanyanyor:  better
preteston(7,1) :- pretest('tar2/arch_def/any3or/better/0/arch_def'). 
preteston(7,2) :- pretest('tar2/arch_def/any3or/better/1/arch_def'). 
preteston(7,3) :- pretest('tar2/arch_def/any3or/better/2/arch_def'). 
preteston(7,4) :- pretest('tar2/arch_def/any3or/better/3/arch_def'). 
preteston(7,5) :- pretest('tar2/arch_def/any3or/better/4/arch_def'). 

test(7):-present('anyanyanyor:  to get better', 
  [  'no treatment',
     'implicitInvocation of targetSystem', 
     'implicitInvocation of targetSystem, c3',
     'implicitInvocation of targetSystem, c3,abstractDataType of targetSystem', 
     'implicitInvocation of targetSystem, c3,abstractDataType of targetSystem, sharedData of targetSystem'
     ], 
  [   b=<8.42,
      b=<16.83,
      b=<25.25,
      b=<33.67,
      b=<42.08,
      b=<50.5,
      b=<58.92,
      b=<67.33,
      b=<75.75,
      b=<84.17,
      b=<92.58,
      b=<100], 100, 0, 5, 0, 
     'tar2/arch_def/any3or/better/*/arch_def.pl', 'tar2/arch_def/any3or/better/anyanyanyor_better.html').
    
% for anyanyanyor:  worse
preteston(8,1) :- pretest('tar2/arch_def/any3or/worse/0/arch_def'). 
preteston(8,2) :- pretest('tar2/arch_def/any3or/worse/1/arch_def'). 
preteston(8,3) :- pretest('tar2/arch_def/any3or/worse/2/arch_def'). 
preteston(8,4) :- pretest('tar2/arch_def/any3or/worse/3/arch_def'). 
preteston(8,5) :- pretest('tar2/arch_def/any3or/worse/4/arch_def'). 
preteston(8,6) :- pretest('tar2/arch_def/any3or/worse/5/arch_def'). 

test(8):-present('anyanyanyor:  to get worse', 
  [  'no treatment',
     'not pipeAndFilter of targetSystem', 
     'not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, c3',
     'not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, c3, c2', 
     'not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, c3, c2, sharedData of targetSystem',
     'not pipeAndFilter of targetSystem, c4, not implicitInvocation of targetSystem, c3, c2, sharedData of targetSystem, not c5'
     ], 
  [   b=<8.42,
      b=<16.83,
      b=<25.25,
      b=<33.67,
      b=<42.08,
      b=<50.5,
      b=<58.92,
      b=<67.33,
      b=<75.75,
      b=<84.17,
      b=<92.58,
      b=<100], 100, 0, 5, 0, 
     'tar2/arch_def/any3or/worse/*/arch_def.pl', 'tar2/arch_def/any3or/worse/anyanyanyor_worse.html').

preteston(10,0) :- pretest('tar2/credit_card_authorize/all_and/worse/0/credit_card_authorize'). 
preteston(10,1) :- pretest('tar2/credit_card_authorize/all_and/worse/1/credit_card_authorize'). 
preteston(10,2) :- pretest('tar2/credit_card_authorize/all_and/worse/2/credit_card_authorize'). 
preteston(10,3) :- pretest('tar2/credit_card_authorize/all_and/worse/3/credit_card_authorize'). 
preteston(10,4) :- pretest('tar2/credit_card_authorize/all_and/worse/4/credit_card_authorize'). 
preteston(10,5) :- pretest('tar2/credit_card_authorize/all_and/worse/5/credit_card_authorize'). 
preteston(10,6) :- pretest('tar2/credit_card_authorize/all_and/worse/6/credit_card_authorize'). 
preteston(10,7) :- pretest('tar2/credit_card_authorize/all_and/worse/7/credit_card_authorize'). 

test(10):-present('credit card authorize:  all_and, to get worse', 
  [  'no treatment',
     'round1: performFirst of retrieve(card*creditRemaining)at layer([3, operationComponents])',
     'round2: round1 +  earlyFixing of status at layer(2)',
     'round3: round2 + replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents])',
     'round4: round3 + severalAttributesPerTuple at layer([4, prioritization])',
     'round5: round4 + performFirst of commonCode(authorize)at layer([4, commonCode])',
     'round6: round5 +  lateFixing of otherAttrs at layer(2)',
     'round7: round6 +  fewAttributePerTuple of (card*status)at layer([2, operationComponents])'
     ], 
  [   b=<0.38,
      b=<0.77,
      b=<1.5,
      b=<1.53,
      b=<1.92,
      b=<2.3,
      b=<2.68,
      b=<3.07,
      b=<3.45,
      b=<3.83,
      b=<4.22,
      b=<4.60], 
  [  cost=0,
     cost=1,
     cost=2,
     cost=3,
     cost=4,
     cost=5,
     cost=6,
     cost=7],
      3.60, 0, 7, 0, 
     'tar2/credit_card_authorize/all_and/worse/*/credit_card_authorize.pl', 'tar2/credit_card_authorize/all_and/worse/all_and_worse.html').

preteston(101,0) :- pretest('tar2/credit_card_authorize/all_and/better/0/credit_card_authorize'). 
preteston(101,1) :- pretest('tar2/credit_card_authorize/all_and/better/1/credit_card_authorize'). 
preteston(101,2) :- pretest('tar2/credit_card_authorize/all_and/better/2/credit_card_authorize'). 
preteston(101,3) :- pretest('tar2/credit_card_authorize/all_and/better/3/credit_card_authorize'). 
preteston(101,4) :- pretest('tar2/credit_card_authorize/all_and/better/4/credit_card_authorize'). 
preteston(101,5) :- pretest('tar2/credit_card_authorize/all_and/better/5/credit_card_authorize'). 


test(101):-present('credit card authorize:  all_and, to get better', 
  [  'no treatment',
     'round1: not earlyFixing of status at layer(2)',
     'round2: round1 +  status needed quickly to stop fraud at layer(2)',
     'round3: round2 + status not specialized at layer([4, prioritization])',
     'round4: round3 + not inherited code predominates authorization at layer([4, commonCode])',
     'round5: round4 + not otherAttrs use most space at layer([4, individualAttributes])'
     ], 
  [   b=<0.38,
      b=<0.77,
      b=<1.5,
      b=<1.53,
      b=<1.92,
      b=<2.3,
      b=<2.68,
      b=<3.07,
      b=<4.22,
      b=<4.60], 
  [  cost=vvlow,
     cost=vlow,
     cost=low,
     cost=high,
     cost=vhigh,
     cost=vvhigh],
      3.60, 0, 10, 0, 
     'tar2/credit_card_authorize/all_and/better/*/credit_card_authorize.pl', 'tar2/credit_card_authorize/all_and/better/all_and_better.html').

preteston(11,0) :- pretest('tar2/credit_card_authorize/any_any_ands/better/0/credit_card_authorize'). 
preteston(11,1) :- pretest('tar2/credit_card_authorize/any_any_ands/better/1/credit_card_authorize'). 
preteston(11,2) :- pretest('tar2/credit_card_authorize/any_any_ands/better/2/credit_card_authorize'). 
preteston(11,3) :- pretest('tar2/credit_card_authorize/any_any_ands/better/3/credit_card_authorize'). 
preteston(11,4) :- pretest('tar2/credit_card_authorize/any_any_ands/better/4/credit_card_authorize'). 
preteston(11,5) :- pretest('tar2/credit_card_authorize/any_any_ands/better/5/credit_card_authorize'). 
preteston(11,6) :- pretest('tar2/credit_card_authorize/any_any_ands/better/6/credit_card_authorize'). 

test(11):-present('credit card authorize:  any_any_ands, to get better', 
  [  'no treatment',
  'round1: disallow bad cards at layer([3, operationComponents])', 
  'round2: round1 + replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents])',
  'round3: round2 + not lateFixing of otherAttrs at layer(2)',
  'round4: round3 + earlyFixing of status at layer(2)',
  'round5: round4 + performFirst of update(card*creditRemaining)at layer([3, operationComponents])',
  'round6: round5 + severalAttributesPerTuple at layer([4, prioritization])'
     ], 
  [   b=<4.67,
      b=<9.33,
      b=<14.0,
      b=<18.7,
      b=<23.3,
      b=<28.0,
      b=<32.7,
      b=<37.3,
      b=<42.0,
      b=<46.7,
      b=<51.3,
      b=<55.0], 
  [  cost=0,
     cost=1,
     cost=2,
     cost=3,
     cost=4,
     cost=5,
     cost=6,
     cost=7],
     55.0, 0,7, 0, 
     'tar2/credit_card_authorize/any_any_ands/better/*/credit_card_authorize.pl', 'tar2/credit_card_authorize/any_any_ands/better/any_any_ands.html').

preteston(12,0) :- pretest('tar2/credit_card_authorize/any_any_ands/worse/0/credit_card_authorize'). 
preteston(12,1) :- pretest('tar2/credit_card_authorize/any_any_ands/worse/1/credit_card_authorize'). 
preteston(12,2) :- pretest('tar2/credit_card_authorize/any_any_ands/worse/2/credit_card_authorize'). 
preteston(12,3) :- pretest('tar2/credit_card_authorize/any_any_ands/worse/3/credit_card_authorize'). 
preteston(12,4) :- pretest('tar2/credit_card_authorize/any_any_ands/worse/4/credit_card_authorize'). 

test(12):-present('credit card authorize:  any_any_ands, to get worse', 
  [  'no treatment',
     'round1: lateFixing of otherAttrs at layer(2)',
     'round2: round1 + other Attrs not accessed during critical operations at layer(2)',
     'round3: round2 + severalAttributesPerTuple at layer([4, prioritization])',
     'round4: round3 + otherAttrs use most space at layer([4, individualAttributes])'
     ], 
  [   b=<4.67,
      b=<9.33,
      b=<14.0,
      b=<18.7,
      b=<23.3,
      b=<28.0,
      b=<32.7,
      b=<37.3,
      b=<42.0,
      b=<46.7,
      b=<51.3,
      b=<55.0], 
  [  cost=0,
     cost=1,
     cost=2,
     cost=3,
     cost=4,
     cost=5,
     cost=6,
     cost=7],
     75.0, 0,7, 0, 
     'tar2/credit_card_authorize/any_any_ands/worse/*/credit_card_authorize.pl', 'tar2/credit_card_authorize/any_any_ands/worse/any_any_ands.html').
     
preteston(14,0) :- pretest('tar2/credit_card_authorize/any_any_ors/worse/0/credit_card_authorize'). 
preteston(14,1) :- pretest('tar2/credit_card_authorize/any_any_ors/worse/1/credit_card_authorize'). 
preteston(14,2) :- pretest('tar2/credit_card_authorize/any_any_ors/worse/2/credit_card_authorize'). 
preteston(14,3) :- pretest('tar2/credit_card_authorize/any_any_ors/worse/3/credit_card_authorize'). 
preteston(14,4) :- pretest('tar2/credit_card_authorize/any_any_ors/worse/4/credit_card_authorize'). 
preteston(14,5) :- pretest('tar2/credit_card_authorize/any_any_ors/worse/5/credit_card_authorize'). 
preteston(14,6) :- pretest('tar2/credit_card_authorize/any_any_ors/worse/6/credit_card_authorize'). 
preteston(14,7) :- pretest('tar2/credit_card_authorize/any_any_ors/worse/7/credit_card_authorize'). 
preteston(14,8) :- pretest('tar2/credit_card_authorize/any_any_ors/worse/8/credit_card_authorize'). 
preteston(14,9) :- pretest('tar2/credit_card_authorize/any_any_ors/worse/9/credit_card_authorize'). 

test(14):-present('credit card authorize:  any_any_ords, to get better', 
  [  'no treatment',
  'round1: fewAttributePerTuple of (card*status)at layer([2, operationComponents])',
  'round2: round1 + disallow bad cards at layer([3, operationComponents])',
  'round3: round2 + performFirst of retrieve(card*status)at layer([3, operationComponents])',
  'round4: round3 + replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents])',
  'round5: round4 + do not exceed credit limit at layer([3, operationComponents])',
  'round6: round5 + inherited code predominates authorization at layer([4, commonCode])',
  'round7: round6 + status not specialized at layer([4, prioritization])',
  'round8: round7 + not otherAttrs use most space at layer([4, individualAttributes])',
  'round9: round8 + earlyFixing of status at layer(2)'
     ], 
  [   b=<88.5,
      b=<177,
      b=<266,
      b=<354,
      b=<443,
      b=<531,
      b=<620,
      b=<708,
      b=<797,
      b=<885,
      b=<974,
      b=<1061], 
  [  cost=0,
     cost=1,
     cost=2,
     cost=3,
     cost=4,
     cost=5,
     cost=6,
     cost=7],
     1238.0, 0,7, 0, 
     'tar2/credit_card_authorize/any_any_ors/worse/*/credit_card_authorize.pl', 'tar2/credit_card_authorize/any_any_ors/worse/any_any_ors_worse.html').
     
     
preteston(15,0) :- pretest('tar2/credit_card_authorize/any_any_anys/better/0/credit_card_authorize'). 
preteston(15,1) :- pretest('tar2/credit_card_authorize/any_any_anys/better/1/credit_card_authorize'). 
preteston(15,2) :- pretest('tar2/credit_card_authorize/any_any_anys/better/2/credit_card_authorize'). 
preteston(15,3) :- pretest('tar2/credit_card_authorize/any_any_anys/better/3/credit_card_authorize'). 
preteston(15,4) :- pretest('tar2/credit_card_authorize/any_any_anys/better/4/credit_card_authorize'). 
preteston(15,5) :- pretest('tar2/credit_card_authorize/any_any_anys/better/5/credit_card_authorize'). 

test(15):-present('credit card authorize:  any_any_anys, to get better', 
  [  'no treatment',
  'round1: not inherited code predominates authorization at layer([4, commonCode])', 
  'round2: round1 + not earlyFixing of status at layer(2)',
  'round3: round2 + status needed quickly to stop fraud at layer(2)',
  'round4: round3 + status not specialized at layer([4, prioritization])',
  'round5: round4 + not otherAttrs use most space at layer([4, individualAttributes])'
     ], 
  [   b=<286,
      b=<573,
      b=<859,
      b=<1146,
      b=<1432,
      b=<1719,
      b=<2005,
      b=<2291,
      b=<2578,
      b=<2864,
      b=<3151,
      b=<3436], 
  [  cost=0,
     cost=1,
     cost=2,
     cost=3,
     cost=4,
     cost=5,
     cost=6,
     cost=7],
     3436.0, 0,7, 0, 
     'tar2/credit_card_authorize/any_any_anys/better/*/credit_card_authorize.pl', 'tar2/credit_card_authorize/any_any_anys/better/any_any_anys.html').
     
preteston(16,0) :- pretest('tar2/credit_card_authorize/any_any_anys/worse/0/credit_card_authorize'). 
preteston(16,1) :- pretest('tar2/credit_card_authorize/any_any_anys/worse/1/credit_card_authorize'). 
preteston(16,2) :- pretest('tar2/credit_card_authorize/any_any_anys/worse/2/credit_card_authorize'). 

test(16):-present('credit card authorize:  any_any_anys, to get worse', 
  [  'no treatment',
  'round1: not replicateDerivedAttribute of (card*creditRemaining)at layer([2, operationComponents])', 
  'round2: round1 +   not lateFixing of otherAttrs at layer(2)'
     ], 
  [   b=<287,
      b=<574,
      b=<862,
      b=<1150,
      b=<1437,
      b=<1725,
      b=<2012,
      b=<2299,
      b=<2587,
      b=<2874,
      b=<3161,
      b=<3448], 
  [  cost=0,
     cost=1,
     cost=2,
     cost=3,
     cost=4,
     cost=5,
     cost=6,
     cost=7],
     3448.0, 0,7, 0, 
     'tar2/credit_card_authorize/any_any_anys/worse/*/credit_card_authorize.pl', 'tar2/credit_card_authorize/any_any_anys/worse/any_any_anys_worse.html').
     
preteston(arch_patterns,worse,0) :- pretest('tar2/arch_patterns/any_ors/worse/0/arch_patterns'). 
preteston(arch_patterns,worse,1) :- pretest('tar2/arch_patterns/any_ors/worse/1/arch_patterns'). 
preteston(arch_patterns,worse,2) :- pretest('tar2/arch_patterns/any_ors/worse/2/arch_patterns'). 
test(arch_patterns,worse):-present('architecture patterns:  any_ors, to get worse', 
  [  'no treatment',
  'round1: external agents can aquire trusted information', 
  'round2: round1 + co_optation of archPattern'
     ], 
  [   b=<15.5,
      b=<31,
      b=<46.5,
      b=<62,
      b=<77.5,
      b=<93,
      b=<108.5,
      b=<124,
      b=<139.5,
      b=<154], 
  [  cost<1.4,
     cost<2.8,
     cost<4.2,
     cost<5.6,
     cost<6],
     154, 0,6, 0, 
     'tar2/arch_patterns/any_ors/worse/*/arch_patterns.pl', 'tar2/arch_patterns/any_ors/worse/any_ors_worse.html').

preteston(arch_patterns,better,0) :- pretest('tar2/arch_patterns/any_ors/better/0/arch_patterns'). 
preteston(arch_patterns,better,1) :- pretest('tar2/arch_patterns/any_ors/better/1/arch_patterns'). 
preteston(arch_patterns,better,2) :- pretest('tar2/arch_patterns/any_ors/better/2/arch_patterns'). 
preteston(arch_patterns,better,3) :- pretest('tar2/arch_patterns/any_ors/better/3/arch_patterns'). 
test(arch_patterns,better):-present('architecture patterns:  any_ors, to get better, compare recommendation and other options', 
  [  'no treatment',
  'round1: jointVenture', 
  'round2: co_optation',  
  'round3: pyramid'
     ], 
  [   b=<17.6,
      b=<35.2,
      b=<52.8,
      b=<70.4,
      b=<88,
      b=<105.6,
      b=<123.2,
      b=<140.8,
      b=<158.4,
      b=<175], 
  [  cost<1.4,
     cost<2.8,
     cost<4.2,
     cost<5.6,
     cost<6],
     175, 0,6, 0, 
     'tar2/arch_patterns/any_ors/better/*/arch_patterns.pl', 'tar2/arch_patterns/any_ors/better/any_ors_better.html').

preteston(arch_patterns_anys,better,0) :- pretest('tar2/arch_patterns/anys/better/0/arch_patterns'). 
preteston(arch_patterns_anys,better,1) :- pretest('tar2/arch_patterns/anys/better/1/arch_patterns'). 
test(arch_patterns_anys,better):-present('architecture patterns:  anys, to get better', 
  [  'no treatment',
  'round1: co_optation'
     ], 
  [   b=<95.1,
      b=<190.2,
      b=<285.3,
      b=<380.4,
      b=<475.5,
      b=<570.6,
      b=<665.7,
      b=<760.8,
      b=<855.9,
      b=<950], 
  [  cost<1.4,
     cost<2.8,
     cost<4.2,
     cost<5.6,
     cost<6],
     950, 0,6, 0, 
     'tar2/arch_patterns/anys/better/*/arch_patterns.pl', 'tar2/arch_patterns/anys/better/anys_better.html').
     
preteston(arch_patterns_anys,worse,0) :- pretest('tar2/arch_patterns/anys/worse/0/arch_patterns'). 
preteston(arch_patterns_anys,worse,1) :- pretest('tar2/arch_patterns/anys/worse/1/arch_patterns'). 
preteston(arch_patterns_anys,worse,2) :- pretest('tar2/arch_patterns/anys/worse/2/arch_patterns'). 
test(arch_patterns_anys,worse):-present('architecture patterns:  anys, to get worse', 
  [  'no treatment',
  'round1: not external agents can aquire trusted information',
  'round2: round1 + not co_optation'
     ], 
  [   b=<95.1,
      b=<190.2,
      b=<285.3,
      b=<380.4,
      b=<475.5,
      b=<570.6,
      b=<665.7,
      b=<760.8,
      b=<855.9,
      b=<950], 
  [  cost<1.4,
     cost<2.8,
     cost<4.2,
     cost<5.6,
     cost<6],
     950, 0,6, 0, 
     'tar2/arch_patterns/anys/worse/*/arch_patterns.pl', 'tar2/arch_patterns/anys/worse/anys_worse.html').
     