softgoal coherence of system. 
softgoal comprehensibility of system.
softgoal simplicity of system.
softgoal deletability of function is critical.
softgoal extensibility of function is critical. 
softgoal modifiability of process is critical.
softgoal modifiability of system is critical. 
softgoal modifiability of function is critical. 
softgoal performance of system is critical. 
softgoal reusability of system is critical. 
softgoal spacePerformance of system is critical. 
softgoal timePerformance of system is critical. 
softgoal updatability of function is critical.
softgoal modifiability of dataRep is veryCritical. 
softgoal abstractDataType of targetSystem. 
softgoal implicitInvocation of targetSystem. 
softgoal pipeAndFilter of targetSystem. 
softgoal sharedData of targetSystem. 
           
claim c1.
claim c2. 
claim c3. 
claim c4.
claim c5.

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

rule0 says goodness of system if
	modifiability of system
	any_of comprehensibility of system
	any_of performance of system
	any_of reusability of system
	ref "L Chung's book" keywords [chung].      

rule1 says modifiability of system if
	helped by c1
	any_of modifiability of process
	any_of modifiability of dataRep
	any_of modifiability of function
	ref "L Chung's book" keywords [chung].      

rule2 says comprehensibility of system if
	coherence of system
	any_of simplicity of system
	ref "L Chung's book" keywords [chung].      

rule3 says performance of system if
	helped by c1
	any_of spacePerformance of system
	any_of  timePerformance of system
	ref "L Chung's book" keywords [chung].      

rule4 says modifiability of function if
	extensibility of function
	any_of deletability of function
	any_of updatability of function
	ref "L Chung's book" keywords [chung].      

rule5 says coherence of system if
	helped by sharedData of targetSystem
	ref "L Chung's book" keywords [chung].      

rule6 says extensibility of function if
	made by implicitInvocation of targetSystem
	any_of helped by sharedData of targetSystem
	any_of unhurt by abstractDataType of targetSystem
		with unhurt by c5
	ref "L Chung's book" keywords [chung].      

rule7 says simplicity of system if
	made by pipeAndFilter of targetSystem
	ref "L Chung's book" keywords [chung].      

rule8 says modifiability of process if
	unhurt by abstractDataType of targetSystem
	any_of unbroken by sharedData of targetSystem
		with helped by c2
	ref "L Chung's book" keywords [chung].      

rule9 says modifiability of dataRep if
	unhurt by implicitInvocation of targetSystem
	any_of helped by abstractDataType of targetSystem
	any_of unbroken by pipeAndFilter of targetSystem
	any_of unhurt by sharedData of targetSystem
		with helped by c2
	ref "L Chung's book" keywords [chung].      

rule10 says reusability of system if
	helped by pipeAndFilter of targetSystem
	any_of helped by implicitInvocation of targetSystem
	any_of unhurt by sharedData of targetSystem
	any_of helped by abstractDataType of targetSystem
		with helped by c3
	ref "L Chung's book" keywords [chung].      

rule11 says spacePerformance of system if
	unhurt by implicitInvocation of targetSystem
	any_of made by sharedData of targetSystem
	any_of unbroken by pipeAndFilter of targetSystem
		with made by c4
	ref "L Chung's book" keywords [chung].      

rule12 says timePerformance of system if
	unbroken by implicitInvocation of targetSystem
	any_of unhurt by abstractDataType of targetSystem
	ref "L Chung's book" keywords [chung].      

rule13 says updatability of function if
	helped by pipeAndFilter of targetSystem
	any_of helped by abstractDataType of targetSystem
	ref "L Chung's book" keywords [chung].      
