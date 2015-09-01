% extracted from ``towards Requirements-Driven Information Systems Engineering:  The Tropos Project; Jaelson Castro, Manuel Kopl, John Mylopoulos [Jaelson02]''
softgoal goodness of system.  

softgoal availability of system.  
softgoal security of system is critical.  
softgoal adaptability of system.  
softgoal integrity of system is critical.  
softgoal authorization of system.  
softgoal dynamicity of system.  
softgoal evolvability of system.  

softgoal accuracy of system.  
softgoal completness of system.  
softgoal usability of system.  
softgoal responseTime of system.  
softgoal identification of system.  
softgoal authentication of system.  
softgoal validation of system.  
softgoal confidentiality of system.  
softgoal externalConsistency of system.  
softgoal run_timeMaintainability of system.  
softgoal run_timeModifiability of system.  
softgoal extensibility of system.  
softgoal updatability of system.  

softgoal pyramid of archPattern costed high.  
softgoal jointVenture of archPattern costed high.  
softgoal co_optation of archPattern costed high.  

claim 'external agents can aquire trusted information'. 
claim 'possible conflicts between responseTime and security'.  
claim 'possible conflicts between security and adaptability'.  

stakeholder rule1. 
stakeholder rule2. 
stakeholder rule3. 
stakeholder rule4. 
stakeholder rule5. 
stakeholder rule6. 
stakeholder rule7. 
stakeholder rule8.
stakeholder rule_a.  
stakeholder rule_b.  
stakeholder rule_c.  
stakeholder rule_d.  
stakeholder rule_e.  
stakeholder rule_f.  
stakeholder rule_g.  
stakeholder rule_h.  
stakeholder rule_i.  
stakeholder rule_j.  
stakeholder rule_k.  
stakeholder rule_l.  
stakeholder rule_m.  

rule1 says goodness of system if
  availability of system
  any_of security of system
  any_of adaptability of system
  ref "Figure 8 in  [Jaelson02]" keywords [level_0].

rule2 says availability of system if
  integrity of system
  any_of usability of system
  any_of responseTime of system
  ref "Figure 8 in  [Jaelson02]" keywords [level_1, level_2].
  
rule3 says integrity of system if
  accuracy of system
  any_of completness of system
  ref "Figure 8 in  [Jaelson02]" keywords [level_2].

rule4 says security of system if
  authorization of system
  any_of confidentiality of system
  any_of externalConsistency of system
  any_of made by availability of system
  any_of helped by 'possible conflicts between responseTime and security'
  any_of helped by 'possible conflicts between security and adaptability'
  ref "Figure 8 in  [Jaelson02]" keywords [level_1, level_2].

rule5 says authorization of system if
  identification of system
  any_of authentication of system
  any_of validation of system
  ref "Figure 8 in  [Jaelson02]" keywords [level_2].

rule6 says adaptability of system if
  dynamicity of system
  any_of updatability of system
  any_of helped by 'possible conflicts between security and adaptability'
  ref "Figure 8 in  [Jaelson02]" keywords [level_1, level_2].
  
rule7 says dynamicity of system if
  run_timeMaintainability of system
  any_of evolvability of system
  ref "Figure 8 in  [Jaelson02]" keywords [level_1, level_2].

rule8 says evolvability of system if
  run_timeModifiability of system
  any_of extensibility of system
  ref "Figure 8 in  [Jaelson02]" keywords [level_2].
  
rule_a says accuracy of system if
  made by pyramid of archPattern
  any_of helped by jointVenture of archPattern
  any_of helped by authorization of system
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].
  
rule_b says completness of system if
  made by jointVenture of archPattern
  any_of unbroken by co_optation of archPattern
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].
  
rule_c says usability of system if
  helped by pyramid of archPattern
  any_of made by jointVenture of archPattern
  any_of unhurt by co_optation of archPattern
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].
  
rule_d says responseTime of system if
  helped by 'possible conflicts between responseTime and security'
  any_of helped by jointVenture of archPattern
  any_of helped by co_optation of archPattern
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].

rule_e says identification of system if
  helped by pyramid of archPattern
  any_of helped by jointVenture of archPattern
    with made by 'external agents can aquire trusted information'
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].

rule_f says authentication of system if
  helped by jointVenture of archPattern
  any_of unbroken by co_optation of archPattern
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].

rule_g says validation of system if
  helped by jointVenture of archPattern
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].

rule_h says confidentiality of system if
  made by pyramid of archPattern
    with made by 'external agents can aquire trusted information'
  any_of helped by jointVenture of archPattern
  any_of unbroken by co_optation of archPattern
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].
  
rule_i says externalConsistency of system if
  unhurt by co_optation of archPattern
    with unhurt by 'external agents can aquire trusted information'
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].

rule_j says run_timeMaintainability of system if
  helped by jointVenture of archPattern
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].

rule_k says run_timeModifiability of system if
  helped by pyramid of archPattern
  any_of helped by co_optation of archPattern
  ref "Figure 8 in  [Jaelson02]; note:  stripped out arc between run_timeModifiability and usability because it seemed to be an error" keywords [level_3].

rule_l says extensibility of system if
  made by pyramid of archPattern
  any_of made by co_optation of archPattern
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].

rule_m says updatability of system if
  made by jointVenture of archPattern
  ref "Figure 8 in  [Jaelson02]" keywords [level_3].
