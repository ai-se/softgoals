% catalogue
% specific on performance of authorize(card, money)

softgoal performance of authorize(card, money).  
softgoal timePerformance of authorize(card, money).  
softgoal spacePerformance of attributes(card).  
softgoal mainMemory of attributes(card).  
softgoal secondaryStorage of attributes(card).  

%i= intermediate node

% responseTime
softgoal responseTime of authorize(card, money) at layer(4).  
softgoal responseTime of commonCode(authorize) at layer([4, commonCode]).  
softgoal responseTime of nonCommonCode(authorize) at layer([4, commonCode]).  
softgoal responseTime_i of commonCode(authorize) at layer([4, commonCode]) is dominant.  
softgoal responseTime_i of nonCommonCode(authorize) at layer([4, commonCode]) is nonDominant.  
softgoal performFirst of commonCode(authorize) at layer([4, commonCode]).  
softgoal responseTime of commonCode(authorize) at layer([3, commonCode]).  
softgoal responseTime of retrieve(card*status) at layer([3, operationComponents]).  
softgoal responseTime of access(card*creditRemaining) at layer([3, operationComponents]).  
softgoal responseTime of otherOperation(authorize) at layer([3, operationComponents]).  
softgoal responseTime_i of retrieve(card*status) at layer([3, operationComponents]) is critical.  
softgoal responseTime of retrieve(card*creditRemaining) at layer([3, operationComponents]).  
softgoal responseTime of update(card*creditRemaining) at layer([3, operationComponents]).  
softgoal responseTime_i of otherOperation(authorize) at layer([3, operationComponents]) is nonCritical.  
softgoal performFirst of retrieve(card*status) at layer([3, operationComponents]).  
%softgoal performEarly of retrieve(card*status) at layer([3, operationComponents]).  
%softgoal performLater of retrieve(card*status) at layer([3, operationComponents]).  
softgoal responseTime of retrieve(card*status) at layer([2, operationComponents]).  
softgoal responseTime_i of retrieve(card*creditRemaining) at layer([3, operationComponents]) is critical.  
softgoal performFirst of update(card*creditRemaining) at layer([3, operationComponents]).  
%softgoal performEarly of update(card*creditRemaining) at layer([3, operationComponents]).  
%softgoal performLater of update(card*creditRemaining) at layer([3, operationComponents]).  
softgoal replicateDerivedAttribute of (card*creditRemaining) at layer([2, operationComponents]).  
softgoal performFirst of retrieve(card*creditRemaining) at layer([3, operationComponents]).  
%softgoal performEarly of retrieve(card*creditRemaining) at layer([3, operationComponents]).  
%softgoal performLater of retrieve(card*creditRemaining) at layer([3, operationComponents]).  
softgoal responseTime of retrieve(card*creditRemaining) at layer([2, operationComponents]).  

softgoal fewAttributePerTuple of (card*status) at layer([2, operationComponents]). 

% secondary storage
softgoal secondaryStorage of status at layer([4, individualAttributes]). 
softgoal secondaryStorage of otherAttrs at layer([4, individualAttributes]). 
softgoal secondaryStorage of creditRemaining at layer([4, individualAttributes]). 
softgoal secondaryStorage_i of status at layer([4, prioritization]) is nonDominant. 
softgoal secondaryStorage_i of otherAttrs at layer([4, prioritization]) is dominant. 
softgoal secondaryStorage_i of creditRemaining at layer([4, prioritization]) is nonDominant. 
softgoal secondaryStorage of status at layer(2). 
softgoal severalAttributesPerTuple at layer([4, prioritization]). 
softgoal secondaryStorage of otherAttrs at layer(2). 
softgoal earlyFixing of status at layer(2).  
softgoal lateFixing of otherAttrs at layer(2). 

% decomposing earlyFixing
%softgoal staticOffsetDetermination of earlyFixing(storage,status).  
%softgoal indexing of earlyFixing(storage,status).  
%softgoal uncompressedFormat of earlyFixing(storage,status).  

% decomposing lateFixing
%softgoal dynamicOffsetDetermination of lateFixing(storage, otherAttrs).  
%softgoal compressedFormat of lateFixing(storage, otherAttrs).  
%softgoal reduceRunTimeReorganization of lateFixing(storage, otherAttrs).  

% responseTime
claim 'inherited code predominates authorization' at layer([4, commonCode]).
claim 'disallow bad cards' at layer([3, operationComponents]). 
claim 'other not important' at layer([3, operationComponents]). 
claim 'do not exceed credit limit' at layer([3, operationComponents]). 

% secondary storage
claim 'status not specialized' at layer([4, prioritization]). 
claim 'otherAttrs use most space' at layer([4, individualAttributes]). 
claim 'status needed quickly to stop fraud' at layer(2).  
claim 'other Attrs not accessed during critical operations' at layer(2).

% catalogue
stakeholder cat01.
stakeholder cat02.
stakeholder cat03.

% responseTime
stakeholder rule01. 
stakeholder rule02. 
stakeholder rule03. 
stakeholder rule04. 
stakeholder rule05. 
stakeholder rule06. 
stakeholder rule07. 
stakeholder rule08. 
stakeholder rule09. 
stakeholder rule10. 
stakeholder rule11. 
stakeholder rule12. 
stakeholder rule13. 
stakeholder rule14. 

% secondary storage
stakeholder rule15. 
stakeholder rule16. 
stakeholder rule17. 
stakeholder rule18. 
stakeholder rule19. 
stakeholder rule20. 
stakeholder rule21. 
stakeholder rule22. 

% eliza's modification, based on L Chung's book page 234, page 271
stakeholder eliza01. 
stakeholder eliza02. 
stakeholder eliza03. 
%stakeholder eliza04. 

% catalogue
cat01 says performance of authorize(card, money) if
  timePerformance of authorize(card, money)
  any_of spacePerformance of attributes(card)
  ref "Figure 8.2 in L Chung's book" keywords [performance, authorize, card, money, cat].
  
cat02 says timePerformance of authorize(card, money) if
  responseTime of authorize(card, money) at layer(4)
  ref "Figure 8.2 in L Chung's book" keywords [timePerformance, authorize, card, money, cat].

cat03 says spacePerformance of attributes(card) if
  mainMemory of attributes(card)
  any_of secondaryStorage of attributes(card)
  ref "Figure 8.2 in L Chung's book" keywords [spacePerformance, attributes, card, cat].

% responseTime
rule01 says responseTime of authorize(card, money) at layer(4) if
  responseTime of commonCode(authorize) at layer([4, commonCode])
  all_of responseTime of nonCommonCode(authorize) at layer([4, commonCode])
  ref "Figure 11.15 in L Chung's book" keywords [authorize, card, money, 4].

rule02 says responseTime of commonCode(authorize) at layer([4, commonCode]) if
  made by responseTime_i of commonCode(authorize) at layer([4, commonCode])
    with made by 'inherited code predominates authorization' at layer([4, commonCode])
  ref "Figure 11.15 in L Chung's book" keywords [commonCode, authorize, 4].

rule03 says responseTime of nonCommonCode(authorize) at layer([4, commonCode]) if
  made by responseTime_i of nonCommonCode(authorize) at layer([4, commonCode])
    with unbroken by 'inherited code predominates authorization' at layer([4, commonCode])
  ref "Figure 11.15 in L Chung's book" keywords [nonCommonCode, authorize, 4].
  
rule04 says responseTime_i of commonCode(authorize) at layer([4, commonCode]) if
  helped by performFirst of commonCode(authorize) at layer([4, commonCode])
  all_of made by responseTime of commonCode(authorize) at layer([3, commonCode])
  ref "Figure 11.15 in L Chung's book" keywords [nonCommonCode, authorize, 4].

rule05 says responseTime of commonCode(authorize) at layer([3, commonCode]) if 
  responseTime of retrieve(card*status) at layer([3, operationComponents])
  all_of responseTime of access(card*creditRemaining) at layer([3, operationComponents])
  all_of responseTime of otherOperation(authorize) at layer([3, operationComponents])
  ref "Figure 11.15 in L Chung's book" keywords [commonCode, authorize, authorize, 3].

rule06 says responseTime of retrieve(card*status) at layer([3, operationComponents]) if
  made by responseTime_i of retrieve(card*status) at layer([3, operationComponents])
    with helped by 'disallow bad cards' at layer([3, operationComponents])
  ref "Figure 11.15 in L Chung's book" keywords [card, status, operationalComponents, 3].

rule07 says responseTime of access(card*creditRemaining) at layer([3, operationComponents]) if
  responseTime of retrieve(card*creditRemaining) at layer([3, operationComponents])
  all_of responseTime of update(card*creditRemaining) at layer([3, operationComponents])
  ref "Figure 11.15 in L Chung's book" keywords [access, card, creditRemaining, operationalComponents, 3].

rule08 says responseTime of otherOperation(authorize) at layer([3, operationComponents]) if
  made by responseTime_i of otherOperation(authorize) at layer([3, operationComponents])
    with unbroken by 'other not important' at layer([3, operationComponents])
  ref "Figure 11.15 in L Chung's book" keywords [access, card, creditRemaining, operationalComponents, 3].
  
rule09 says responseTime_i of retrieve(card*status) at layer([3, operationComponents]) if
  made by performFirst of retrieve(card*status) at layer([3, operationComponents])
  all_of made by responseTime of retrieve(card*status) at layer([2, operationComponents])
  ref "Figure 11.15 in L Chung's book" keywords [retrieve, card, status, operationalComponents, 3].
  
rule10 says responseTime of retrieve(card*creditRemaining) at layer([3, operationComponents]) if
  made by responseTime_i of retrieve(card*creditRemaining) at layer([3, operationComponents])
    with helped by 'do not exceed credit limit' at layer([3, operationComponents])
  ref "Figure 11.15 in L Chung's book" keywords [retrieve, card, creditRemaining, operationalComponents, 3].

rule11 says responseTime_i of retrieve(card*creditRemaining) at layer([3, operationComponents]) if 
  made by responseTime of retrieve(card*creditRemaining) at layer([2, operationComponents])
  all_of made by performFirst of retrieve(card*creditRemaining) at layer([3, operationComponents])
  ref "Figure 11.15 in L Chung's book" keywords [retrieve, card, creditRemaining, operationalComponents, 3].

rule12 says responseTime of update(card*creditRemaining) at layer([3, operationComponents]) if
  made by performFirst of update(card*creditRemaining) at layer([3, operationComponents]) 
  all_of unbroken by replicateDerivedAttribute of (card*creditRemaining) at layer([2, operationComponents])
  ref "Figure 11.15 in L Chung's book" keywords [update, card, creditRemaining, operationalComponents, 3].

rule13 says responseTime of retrieve(card*status) at layer([2, operationComponents]) if 
  helped by fewAttributePerTuple of (card*status) at layer([2, operationComponents])
  all_of helped by earlyFixing of status at layer(2)
  ref "Figure 11.15 in L Chung's book" keywords [retrieve, card, status, operationalComponents, 2].
  
rule14 says responseTime of retrieve(card*creditRemaining) at layer([2, operationComponents]) if
  helped by replicateDerivedAttribute of (card*creditRemaining) at layer([2, operationComponents])
  ref "Figure 11.15 in L Chung's book" keywords [retrieve, card, creditRemaining, operationalComponents, 2].

rule15 says secondaryStorage of attributes(card) if
  secondaryStorage of status at layer([4, individualAttributes])
  all_of secondaryStorage of otherAttrs at layer([4, individualAttributes])
  all_of secondaryStorage of creditRemaining at layer([4, individualAttributes])
  ref "Figure 11.18 in L Chung's book" keywords [secondaryStorage, attributes, card, 4].

rule16 says secondaryStorage of status at layer([4, individualAttributes]) if
  made by secondaryStorage_i of status at layer([4, prioritization])
    with unbroken by 'otherAttrs use most space' at layer([4, individualAttributes])
  ref "Figure 11.18 in L Chung's book" keywords [secondaryStorage, status, individualAttributes, 4].

rule17 says secondaryStorage of otherAttrs at layer([4, individualAttributes]) if
  made by secondaryStorage_i of otherAttrs at layer([4, prioritization])
    with made by 'otherAttrs use most space' at layer([4, individualAttributes])
  ref "Figure 11.18 in L Chung's book" keywords [secondaryStorage, otherAttrs, individualAttributes, 4].
  
rule18 says secondaryStorage of creditRemaining at layer([4, individualAttributes]) if
  made by secondaryStorage_i of creditRemaining at layer([4, prioritization])
    with unbroken by 'otherAttrs use most space' at layer([4, individualAttributes])
  ref "Figure 11.18 in L Chung's book" keywords [secondaryStorage, creditRemaining, individualAttributes, 4].
  
rule19 says secondaryStorage_i of status at layer([4, prioritization]) if
  made by secondaryStorage of status at layer(2)
    with helped by 'status not specialized' at layer([4, prioritization])
  ref "Figure 11.18 in L Chung's book" keywords [secondaryStorage, status, prioritization, 4].
  
rule20 says secondaryStorage_i of otherAttrs at layer([4, prioritization]) if
  made by secondaryStorage of otherAttrs at layer(2)
  all_of helped by severalAttributesPerTuple at layer([4, prioritization])
  ref "Figure 11.18 in L Chung's book" keywords [secondaryStorage, otherAttrs, prioritization, 4].
  
rule21 says secondaryStorage of status at layer(2) if
  unbroken by earlyFixing of status at layer(2)
    with made by 'status needed quickly to stop fraud' at layer(2)
  ref "Figure 11.18 in L Chung's book" keywords [secondaryStorage, status, 2].

rule22 says secondaryStorage of otherAttrs at layer(2) if
  helped by lateFixing of otherAttrs at layer(2)
    with made by 'other Attrs not accessed during critical operations' at layer(2)
  ref "Figure 11.18 in L Chung's book" keywords [secondaryStorage, otherAttrs, 2].

eliza01 says responseTime_i of otherOperation(authorize) at layer([3, operationComponents]) if 
  unhurt by lateFixing of otherAttrs at layer(2) 
  ref "page 234 in L Chung's book" keywords [otherOperation, authorize, eliza, operationalComponents, 2].

pick_one_in([
  performFirst of retrieve(card*status) at layer([3, operationComponents]), 
  performFirst of update(card*creditRemaining) at layer([3, operationComponents]), 
  performFirst of retrieve(card*creditRemaining) at layer([3, operationComponents])
  ]). 

pick_one_in([a,b,v,d]).

/*eliza02 says performFirst of retrieve(card*status) at layer([3, operationComponents]) if
  unbroken by performFirst of update(card*creditRemaining) at layer([3, operationComponents])
  all_of unbroken by performFirst of retrieve(card*creditRemaining) at layer([3, operationComponents])
  ref "exclusive or" keywords [excluxive, eliza, 3].
 
eliza03 says performFirst of retrieve(card*creditRemaining) at layer([3, operationComponents]) if
  unbroken by performFirst of update(card*creditRemaining) at layer([3, operationComponents])
%  all_of  unbroken by performFirst of retrieve(card*status) at layer([3, operationComponents])
  ref "exclusive or" keywords [excluxive, eliza, 3].
  
%eliza04 says performFirst of update(card*creditRemaining) at layer([3, operationComponents]) if
%  unbroken by performFirst of retrieve(card*status) at layer([3, operationComponents])
%  all_of unbroken by performFirst of retrieve(card*creditRemaining) at layer([3, operationComponents])
%  ref "exclusive or" keywords [excluxive, eliza, 3].
*/