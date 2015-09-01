% combination scoring definition

% score(CombinationType, MinOrMaxOrAverage, AddOrSubtractFromTotal). 
score(all_of, min, 1). 
score(any_of, add, 1).  
score(one_of, max, 1).  
score(any_one_of, max, 1).  
score(none_of, min, -1). 
score(claim2parent, multiply, 1).  

score(helped, 	multiply, randomize(normal(1.4,0.2), [[>=, 0], [=<,2]])).
score(made, 	multiply, randomize(normal(1.8,0.2), [[>=, 0], [=<,2]])).
score(unhurt, 	multiply, randomize(normal(0.6,0.2), [[=<,2],[>=, 0]])).
score(unbroken, 	multiply, randomize(normal(0.2,0.2), [[>=, 0], [=<,2]])).

score(c2p, multiply, 1).  % children to parent

% the following are non-randomizable
score(combine, add).  
score(stakeholder, 0).  
score(default, 1).  
score(not_done, 0).  
score(not_lurched, 0).
score(wout_claim_support, 0). 

% weight(Severity, SoftgoalName, Weight)
weight(critical,	_,randomize(normal(2,0.3), [[>=, 0], [=<,3]])).
weight(normal,	_,randomize(normal(1,0.3), [[>=, 0], [=<,3]])).
weight(abduced,	_,1).
