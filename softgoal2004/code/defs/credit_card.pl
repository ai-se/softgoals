%i= intermediate node

softgoal responseTime of cancel(card) at layer=3.  
softgoal responseTime of components(cancel(card)) at layer=3.

softgoal responseTime of access(attributes(card)) at layer=[3, operationalComponents].
softgoal responseTime of otherOperations(cancel) at layer=[3, operationalComponents].
softgoal responseTime_i of access(attributes(card)) at layer=[3, operationalComponents] is critical.
softgoal responseTime_i of otherOperations(cancel) at layer=[3, operationalComponents] is noncritical.

softgoal responseTime of access(card*status) at layer=[3,individualAttributes].
softgoal responseTime of access(card*otherAttrs) at layer=[3,individualAttributes].
softgoal responseTime_i of access(card*status) at layer=[3,individualAttributes] is critical.
softgoal responseTime_i of access(card*otherAttrs) at layer=[3,individualAttributes] is noncritical.

softgoal responseTime of update(card*status) at layer=[3,entityManagement].
softgoal responseTime of retrieve(card*status) at layer=[3,entityManagement].
softgoal responseTime_i of update(card*status) at layer=[3,entityManagement] is critical.
softgoal responseTime_i of retrieve(card*status) at layer=[3,entityManagement] is noncritical.

softgoal performFirst of update(card*status) at layer=[3,entityManagement].
softgoal performLater of retrieve(card*status) at layer=[3,entityManagement].

softgoal responseTime of update(card*status) at layer=[2,flow_through].
softgoal responseTime of implementationComponents(update(card*status)) at layer=[2,implementationComponents].
softgoal responseTime of findOffset(card*status) at layer=[2,implementationComponents].
softgoal responseTime of sendToStorage(card*status) at layer=[2,implementationComponents].
softgoal staticOffsetDetermination of card*status at layer=[2,implementationComponents].
softgoal fewAttributesPerTuple of card*status at layer=[2,implementationComponents].

claim 'access important for cancellation' at layer=[3, operationalComponents].
claim 'other ops not important for cancellation' at layer=[3, operationalComponents]. 
claim 'status important for cancellation' at layer=[3,individualAttributes].
claim 'other attrs not important for cancellation' at layer=[3,individualAttributes].
claim 'updating status is important for cancellation' at layer=[3,entityManagement].
claim 'retrieving status is not important for cancellation' at layer=[3,entityManagement].

stakeholder rule0. 
stakeholder rule1. 
stakeholder rule2. 
stakeholder rule3. 
stakeholder rule4. 
stakeholder rule5. 
stakeholder rule6. 
stakeholder rule7. 
stakeholder rule8. 
stakeholder rule9. 
stakeholder rule10. 
stakeholder rule11. 
stakeholder rule12. 
stakeholder rule13. 
stakeholder rule14. 
stakeholder rule15. 

rule0 says responseTime of cancel(card) at layer=3 if
  responseTime of components(cancel(card)) at layer=3
  ref "Figure 11.11 in L Chung's book" keywords [cancel, card, 3].
  
rule1 says responseTime of components(cancel(card)) at layer=3 if
  responseTime of access(attributes(card)) at layer=[3, operationalComponents]
  all_of responseTime of otherOperations(cancel) at layer=[3, operationalComponents]
  ref "Figure 11.11 in L Chung's book" keywords [components, cancel, card, 3].

rule2 says responseTime of access(attributes(card)) at layer=[3, operationalComponents] if
  made by responseTime_i of access(attributes(card)) at layer=[3, operationalComponents]
    with made by claim 'access important for cancellation' at layer=[3, operationalComponents]
  ref "Figure 11.11 in L Chung's book" keywords [access, attributes, card, operationalComponents, 3].

rule3 says responseTime of otherOperations(cancel) at layer=[3, operationalComponents] if
  made by responseTime_i of otherOperations(cancel) at layer=[3, operationalComponents]
    with unbroken by claim 'other ops not important for cancellation' at layer=[3, operationalComponents]
  ref "Figure 11.11 in L Chung's book" keywords [otherOperations, cancel, operationalComponents, 3].
  
rule4 says responseTime_i of access(attributes(card)) at layer=[3, operationalComponents] if
  responseTime of access(card*status) at layer=[3,individualAttributes]
  all_of responseTime of access(card*otherAttrs) at layer=[3,individualAttributes]
  ref "Figure 11.11 in L Chung's book" keywords [otherOperations, cancel, operationalComponents, 3].

rule5 says responseTime of access(card*status) at layer=[3,individualAttributes] if
  made by responseTime_i of access(card*status) at layer=[3,individualAttributes]
    with made by claim 'status important for cancellation' at layer=[3, individualAttributes]
  ref "Figure 11.11 in L Chung's book" keywords [access, card, status, individualAttributes, 3].
  
rule6 says responseTime of access(card*otherAttrs) at layer=[3,individualAttributes] if
  made by responseTime_i of access(card*otherAttrs) at layer=[3,individualAttributes]
    with unbroken by claim 'other attrs not important for cancellation' at layer=[3, individualAttributes]
  ref "Figure 11.11 in L Chung's book" keywords [access, card, otherAttrs, individualAttributes, 3].
  
rule7 says responseTime_i of access(card*status) at layer=[3,individualAttributes] if
  responseTime of update(card*status) at layer=[3,entityManagement]
  all_of responseTime of retrieve(card*status) at layer=[3,entityManagement]
  ref "Figure 11.11 in L Chung's book" keywords [access, card, status, individualAttributes, 3].

rule8 says responseTime of update(card*status) at layer=[3,entityManagement] if
  made by responseTime_i of update(card*status) at layer=[3,entityManagement]
    with made by claim 'updating status is important for cancellation' at layer=[3, entityManagement]
  ref "Figure 11.11 in L Chung's book" keywords [update, card, status, entityManagement, 3].
  
rule9 says responseTime of retrieve(card*status) at layer=[3,entityManagement] if
  made by responseTime_i of retrieve(card*status) at layer=[3,entityManagement]
    with unbroken by claim 'retrieving status is not important for cancellation' at layer=[3, individualAttributes]
  ref "Figure 11.11 in L Chung's book" keywords [retrieve, card, status, entityManagement, 3].
  
rule10 says responseTime_i of update(card*status) at layer=[3,entityManagement] if
  helped by performFirst of update(card*status) at layer=[3,entityManagement]
  ref "Figure 11.11 in L Chung's book" keywords [update, card, status, entityManagement, 3].
  
rule11 says responseTime_i of update(card*status) at layer=[3,entityManagement] if
  unbroken by performLater of retrieve(card*status) at layer=[3,entityManagement]
  ref "Figure 11.11 in L Chung's book" keywords [update, card, status, entityManagement, 3].

rule12 says responseTime of update(card*status) at layer=[2,flow_through] if
  helped by responseTime of implementationComponents(update(card*status)) at layer=[2,implementationComponents]
  ref "Figure 11.11 in L Chung's book" keywords [update, card, status, flow_through, 2].

rule13 says responseTime of implementationComponents(update(card*status)) at layer=[2,implementationComponents] if
  responseTime of findOffset(card*status) at layer=[2,implementationComponents]
  all_of responseTime of sendToStorage(card*status) at layer=[2,implementationComponents]
  ref "Figure 11.11 in L Chung's book" keywords [implementationComponents, card, status, implementationComponents, 2].

rule14 says responseTime of findOffset(card*status) at layer=[2,implementationComponents] if
  helped by staticOffsetDetermination of card*status at layer=[2,implementationComponents]
  ref "Figure 11.11 in L Chung's book" keywords [findOffset, card, status, implementationComponents, 2].

rule15 says sendToStorage(card*status) at layer=[2,implementationComponents] if
  helped by fewAttributesPerTuple of card*status at layer=[2,implementationComponents]
  ref "Figure 11.11 in L Chung's book" keywords [rsendToStorage, card, status, implementationComponents, 2].
