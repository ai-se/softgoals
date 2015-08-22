
% C stands for capability (actor)

softgoal riskMinimization of system.  

softgoal minimizeFaultCriticality of system. 
softgoal minimizeFaultPotentiality of system.

softgoal performanceAndOperation 	of faultCriticality. 
softgoal safety 			of faultCriticality. 
softgoal devCostAndSched 		of faultCriticality. 

softgoal complexity 		of faultPotentiality. 
softgoal maturityOfTechnology 	of faultPotentiality. 
softgoal reqmtsDefnAndStability 	of faultPotentiality. 
softgoal testability 			of faultPotentiality. 

softgoal guidance		of dart. 
softgoal navigation		of dart. 
softgoal vehicleManagement	of dart. 
softgoal stateFilter		of dart. 
softgoal targetStateFilter	of dart. 
softgoal telemetry		of dart.  
softgoal control		of dart.   
softgoal cam		of dart. 

softgoal diagnosticMode 	of avgs.  
softgoal overallRequirement 	of avgs.
softgoal trackingMode	of avgs.  
softgoal acquisitionMode 	of avgs.
softgoal spotMode 		of avgs.
softgoal standbyMode	of avgs.

stakeholder ruleA. 
stakeholder ruleB. 
stakeholder ruleC. 
stakeholder ruleD. 
stakeholder ruleE. 
stakeholder ruleF. 
stakeholder ruleG. 
stakeholder ruleH. 
stakeholder ruleI. 
stakeholder ruleJ. 

ruleA says riskMinimization of system if
  minimizeFaultCriticality of system
  any_of minimizeFaultPotentiality of system
  ref "cchr doc" keywords [nfr, riskMinimization].      

ruleB says minimizeFaultCriticality of system if
  performanceAndOperation 	of faultCriticality
  any_of safety of faultCriticality
  any_of devCostAndSched of faultCriticality
  ref "cchr doc" keywords [nfr, minimizeFaultCriticality].      

ruleC says minimizeFaultPotentiality of system if
  complexity of faultPotentiality
  any_of maturityOfTechnology of faultPotentiality
  any_of reqmtsDefnAndStability of faultPotentiality
  any_of testability of faultPotentiality
  ref "cchr doc" keywords [nfr, minimizeFaultPotentiality].      

ruleD says performanceAndOperation 	of faultCriticality if
  catastrophically_rated by guidance of dart
  any_of catastrophically_rated by navigation of dart
  any_of catastrophically_rated by vehicleManagement of dart
  any_of catastrophically_rated by stateFilter of dart 
  any_of catastrophically_rated by targetStateFilter of dart 
  any_of catastrophically_rated by telemetry of dart  
  any_of catastrophically_rated by control of dart
  any_of moderately_rated by cam of dart
  any_of critically_rated by diagnosticMode of avgs
  any_of critically_rated by overallRequirement of avgs
  any_of critically_rated by trackingMode of avgs  
  any_of critically_rated by acquisitionMode of avgs
  any_of critically_rated by spotMode of avgs
  any_of lowly_rated by standbyMode of avgs
  ref "cchr doc" keywords [nfr_function, performanceAndOperation].      

ruleE says safety of faultCriticality if
  catastrophically_rated by guidance of dart
  any_of catastrophically_rated by navigation of dart
  any_of catastrophically_rated by vehicleManagement of dart
  any_of catastrophically_rated by stateFilter of dart 
  any_of lowly_rated by targetStateFilter of dart 
  any_of lowly_rated by telemetry of dart  
  any_of catastrophically_rated by control of dart
  any_of lowly_rated by cam of dart
  any_of lowly_rated by diagnosticMode of avgs
  any_of critically_rated by overallRequirement of avgs
  any_of lowly_rated by trackingMode of avgs  
  any_of lowly_rated by acquisitionMode of avgs
  any_of lowly_rated by spotMode of avgs
  any_of critically_rated by standbyMode of avgs
  ref "cchr doc" keywords [nfr_function, safety].      
  
 ruleF says devCostAndSched of faultCriticality if
  moderately_rated by guidance of dart
  any_of moderately_rated by navigation of dart
  any_of moderately_rated by vehicleManagement of dart
  any_of moderately_rated by stateFilter of dart 
  any_of moderately_rated by targetStateFilter of dart 
  any_of critically_rated by telemetry of dart  
  any_of lowly_rated by control of dart
  any_of lowly_rated by cam of dart
  any_of moderately_rated by diagnosticMode of avgs
  any_of critically_rated by overallRequirement of avgs
  any_of critically_rated by trackingMode of avgs  
  any_of critically_rated by acquisitionMode of avgs
  any_of critically_rated by spotMode of avgs
  any_of lowly_rated by standbyMode of avgs
  ref "cchr doc" keywords [nfr_function, devCostAndSched].      
  
ruleG says complexity of faultPotentiality if
  critically_rated by guidance of dart
  any_of critically_rated by navigation of dart
  any_of critically_rated by vehicleManagement of dart
  any_of critically_rated by stateFilter of dart 
  any_of critically_rated by targetStateFilter of dart 
  any_of critically_rated by telemetry of dart  
  any_of moderately_rated by control of dart
  any_of critically_rated by cam of dart
  any_of critically_rated by diagnosticMode of avgs
  any_of lowly_rated by overallRequirement of avgs
  any_of critically_rated by trackingMode of avgs  
  any_of critically_rated by acquisitionMode of avgs
  any_of critically_rated by spotMode of avgs
  any_of lowly_rated by standbyMode of avgs
  ref "cchr doc" keywords [nfr_function, complexity].      

ruleH says maturityOfTechnology of faultPotentiality if
  moderately_rated by guidance of dart
  any_of moderately_rated by navigation of dart
  any_of moderately_rated by vehicleManagement of dart
  any_of lowly_rated by stateFilter of dart 
  any_of moderately_rated by targetStateFilter of dart 
  any_of lowly_rated by telemetry of dart  
  any_of lowly_rated by control of dart
  any_of critically_rated by cam of dart
  any_of moderately_rated by diagnosticMode of avgs
  any_of moderately_rated by overallRequirement of avgs
  any_of moderately_rated by trackingMode of avgs  
  any_of moderately_rated by acquisitionMode of avgs
  any_of moderately_rated by spotMode of avgs
  any_of lowly_rated by standbyMode of avgs
  ref "cchr doc" keywords [nfr_function, maturityOfTechnology].      

ruleI says reqmtsDefnAndStability of faultPotentiality if
  moderately_rated by guidance of dart
  any_of moderately_rated by navigation of dart
  any_of critically_rated by vehicleManagement of dart
  any_of moderately_rated by stateFilter of dart 
  any_of moderately_rated by targetStateFilter of dart 
  any_of critically_rated by telemetry of dart  
  any_of moderately_rated by control of dart
  any_of moderately_rated by cam of dart
  any_of moderately_rated by diagnosticMode of avgs
  any_of moderately_rated by overallRequirement of avgs
  any_of moderately_rated by trackingMode of avgs  
  any_of moderately_rated by acquisitionMode of avgs
  any_of moderately_rated by spotMode of avgs
  any_of moderately_rated by standbyMode of avgs
  ref "cchr doc" keywords [nfr_function,reqmtsDefnAndStability].      
  
ruleJ says testability of faultPotentiality if
  critically_rated by guidance of dart
  any_of critically_rated by navigation of dart
  any_of critically_rated by vehicleManagement of dart
  any_of critically_rated by stateFilter of dart 
  any_of critically_rated by targetStateFilter of dart 
  any_of moderately_rated by telemetry of dart  
  any_of lowly_rated by control of dart
  any_of critically_rated by cam of dart
  any_of critically_rated by diagnosticMode of avgs
  any_of critically_rated by overallRequirement of avgs
  any_of critically_rated by trackingMode of avgs  
  any_of critically_rated by acquisitionMode of avgs
  any_of critically_rated by spotMode of avgs
  any_of moderately_rated by standbyMode of avgs
  ref "cchr doc" keywords [nfr_function, testability].      
% ----------------------------------------------------------------------------------------------%

softgoal rav01	of ral costed notHigh. 
softgoal rav02	of ral costed notHigh. 
softgoal rav03	of ral costed notHigh. 
softgoal rav04	of ral costed notHigh. 
softgoal rav05	of ral costed notHigh. 
softgoal rav06	of ral costed notHigh. 
softgoal rav07	of ral costed notHigh. 
softgoal rav08	of ral costed notHigh. 
softgoal rav09	of ral costed notHigh. 
softgoal rav10	of ral costed veryHigh. 
softgoal rav11	of ral costed veryHigh. 
softgoal rav12	of ral costed veryHigh. 
softgoal rav13	of ral costed veryHigh. 

softgoal dav01	of dal costed high. 
softgoal dav02	of dal costed high. 
softgoal dav03	of dal costed high. 
softgoal dav04	of dal costed high. 
softgoal dav05	of dal costed high. 
softgoal dav06	of dal costed high. 
softgoal dav07	of dal costed high. 
softgoal dav08	of dal costed high. 
softgoal dav09	of dal costed high. 
softgoal dav10	of dal costed veryHigh. 
softgoal dav11	of dal costed veryHigh. 
softgoal dav12	of dal costed veryHigh. 
softgoal dav13	of dal costed veryHigh. 

softgoal cav01	of cal costed high. 
softgoal cav02	of cal costed high. 
softgoal cav03	of cal costed high. 
softgoal cav04	of cal costed high. 
softgoal cav05	of cal costed high. 
softgoal cav06	of cal costed high. 
softgoal cav07	of cal costed veryHigh. 
softgoal cav08	of cal costed veryHigh. 
softgoal cav09	of cal costed veryHigh. 
softgoal cav10	of cal costed veryHigh. 
softgoal cav11	of cal costed veryHigh. 

softgoal tav01	of tal costed notHigh. 
softgoal tav02	of tal costed notHigh. 
softgoal tav03	of tal costed notHigh. 
softgoal tav04	of tal costed notHigh. 
softgoal tav05	of tal costed notHigh. 
softgoal tav06	of tal costed notHigh. 
softgoal tav07	of tal costed notHigh. 
softgoal tav08	of tal costed high. 
softgoal tav09	of tal costed high. 
softgoal tav10	of tal costed veryHigh. 
softgoal tav11	of tal costed veryHigh. 

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

rule1 says guidance of dart if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  any_of positively_influenced by rav10 of ral
  any_of positively_influenced by rav11 of ral
  any_of positively_influenced by rav12 of ral
  any_of positively_influenced by rav13 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  any_of positively_influenced by dav10 of dal
  any_of positively_influenced by dav11 of dal
  any_of positively_influenced by dav12 of dal
  any_of positively_influenced by dav13 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  any_of positively_influenced by cav07 of cal
  any_of positively_influenced by cav08 of cal
  any_of positively_influenced by cav09 of cal
  any_of positively_influenced by cav10 of cal
  any_of positively_influenced by cav11 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  any_of positively_influenced by tav10 of tal
  any_of positively_influenced by tav11 of tal
  ref "cchr doc" keywords [function_analysis].      
  
rule2 says navigation of dart if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  any_of positively_influenced by rav10 of ral
  any_of positively_influenced by rav11 of ral
  any_of positively_influenced by rav12 of ral
  any_of positively_influenced by rav13 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  any_of positively_influenced by dav10 of dal
  any_of positively_influenced by dav11 of dal
  any_of positively_influenced by dav12 of dal
  any_of positively_influenced by dav13 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  any_of positively_influenced by cav07 of cal
  any_of positively_influenced by cav08 of cal
  any_of positively_influenced by cav09 of cal
  any_of positively_influenced by cav10 of cal
  any_of positively_influenced by cav11 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  any_of positively_influenced by tav10 of tal
  any_of positively_influenced by tav11 of tal
  ref "cchr doc" keywords [function_analysis].      
  
rule3 says vehicleManagement of dart if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  any_of positively_influenced by rav10 of ral
  any_of positively_influenced by rav11 of ral
  any_of positively_influenced by rav12 of ral
  any_of positively_influenced by rav13 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  any_of positively_influenced by dav10 of dal
  any_of positively_influenced by dav11 of dal
  any_of positively_influenced by dav12 of dal
  any_of positively_influenced by dav13 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  any_of positively_influenced by cav07 of cal
  any_of positively_influenced by cav08 of cal
  any_of positively_influenced by cav09 of cal
  any_of positively_influenced by cav10 of cal
  any_of positively_influenced by cav11 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  any_of positively_influenced by tav10 of tal
  any_of positively_influenced by tav11 of tal
  ref "cchr doc" keywords [function_analysis].      
  
 
rule4 says stateFilter of dart if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  any_of positively_influenced by rav10 of ral
  any_of positively_influenced by rav11 of ral
  any_of positively_influenced by rav12 of ral
  any_of positively_influenced by rav13 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  any_of positively_influenced by dav10 of dal
  any_of positively_influenced by dav11 of dal
  any_of positively_influenced by dav12 of dal
  any_of positively_influenced by dav13 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  any_of positively_influenced by cav07 of cal
  any_of positively_influenced by cav08 of cal
  any_of positively_influenced by cav09 of cal
  any_of positively_influenced by cav10 of cal
  any_of positively_influenced by cav11 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  any_of positively_influenced by tav10 of tal
  any_of positively_influenced by tav11 of tal
  ref "cchr doc" keywords [function_analysis].      
  
rule5 says targetStateFilter of dart if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  ref "cchr doc" keywords [function_analysis].      
  
rule6 says telemetry of dart if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  any_of positively_influenced by rav10 of ral
  any_of positively_influenced by rav11 of ral
  any_of positively_influenced by rav12 of ral
  any_of positively_influenced by rav13 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  any_of positively_influenced by dav10 of dal
  any_of positively_influenced by dav11 of dal
  any_of positively_influenced by dav12 of dal
  any_of positively_influenced by dav13 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  any_of positively_influenced by cav07 of cal
  any_of positively_influenced by cav08 of cal
  any_of positively_influenced by cav09 of cal
  any_of positively_influenced by cav10 of cal
  any_of positively_influenced by cav11 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  any_of positively_influenced by tav10 of tal
  any_of positively_influenced by tav11 of tal
  ref "cchr doc" keywords [function_analysis].      

rule7 says control of dart if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  ref "cchr doc" keywords [function_analysis].      

rule8 says cam of dart if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  ref "cchr doc" keywords [function_analysis].      


rule9 says diagnosticMode of avgs if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  ref "cchr doc" keywords [function_analysis].      
  
rule10 says overallRequirement of avgs if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  any_of positively_influenced by rav10 of ral
  any_of positively_influenced by rav11 of ral
  any_of positively_influenced by rav12 of ral
  any_of positively_influenced by rav13 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  any_of positively_influenced by dav10 of dal
  any_of positively_influenced by dav11 of dal
  any_of positively_influenced by dav12 of dal
  any_of positively_influenced by dav13 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  any_of positively_influenced by cav07 of cal
  any_of positively_influenced by cav08 of cal
  any_of positively_influenced by cav09 of cal
  any_of positively_influenced by cav10 of cal
  any_of positively_influenced by cav11 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  any_of positively_influenced by tav10 of tal
  any_of positively_influenced by tav11 of tal
  ref "cchr doc" keywords [function_analysis].      
  
rule11 says trackingMode of avgs if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  ref "cchr doc" keywords [function_analysis].      

rule12 says acquisitionMode of avgs if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  ref "cchr doc" keywords [function_analysis].      

rule13 says spotMode of avgs if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
 any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  ref "cchr doc" keywords [function_analysis].      

rule14 says standbyMode of avgs if
  positively_influenced by rav01 of ral
  any_of positively_influenced by rav02 of ral
  any_of positively_influenced by rav03 of ral
  any_of positively_influenced by rav04 of ral
  any_of positively_influenced by rav05 of ral
  any_of positively_influenced by rav06 of ral
  any_of positively_influenced by rav07 of ral
  any_of positively_influenced by rav08 of ral
    any_of positively_influenced by rav09 of ral
  
  any_of positively_influenced by dav01 of dal
  any_of positively_influenced by dav02 of dal
  any_of positively_influenced by dav03 of dal
  any_of positively_influenced by dav04 of dal
  any_of positively_influenced by dav05 of dal
  any_of positively_influenced by dav06 of dal
  any_of positively_influenced by dav07 of dal
  any_of positively_influenced by dav08 of dal
  any_of positively_influenced by dav09 of dal
  
  any_of positively_influenced by cav01 of cal
  any_of positively_influenced by cav02 of cal
  any_of positively_influenced by cav03 of cal
  any_of positively_influenced by cav04 of cal
  any_of positively_influenced by cav05 of cal
  any_of positively_influenced by cav06 of cal
  
  any_of positively_influenced by tav01 of tal
  any_of positively_influenced by tav02 of tal
  any_of positively_influenced by tav03 of tal
  any_of positively_influenced by tav04 of tal
  any_of positively_influenced by tav05 of tal
  any_of positively_influenced by tav06 of tal
  any_of positively_influenced by tav07 of tal
  any_of positively_influenced by tav08 of tal
  any_of positively_influenced by tav09 of tal
  ref "cchr doc" keywords [function_analysis].      
