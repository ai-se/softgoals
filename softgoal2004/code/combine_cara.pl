% combination scoring definition

% score(CombinationType, MinOrMaxOrAverage, AddOrSubtractFromTotal). 
score(all_of, min, 1). 
score(any_of, average, 1).  
score(any_one_of, max, 1).  
score(one_of, max, 1).  
score(none_of, min, -1). 
score(claim2parent, multiply, 1).  

% score(helped, multiply, randomize(normal(0,0.4), [[>=, 0], [=<, 0.2]])).

score(helped, 	multiply, randomize(normal(1.4,0.2), [[>=, 0], [=<,2]])).
score(made, 	multiply, randomize(normal(1.8,0.2), [[>=, 0], [=<,2]])).
score(unhurt, 	multiply, randomize(normal(0.6,0.2), [[=<,2],[>=, 0]])).
score(unbroken, 	multiply, randomize(normal(0.2,0.2), [[>=, 0], [=<,2]])).

/*
score(helped, 	multiply, 1.4).
score(made, 	multiply, 1.8).
score(unhurt, 	multiply, 0.6).
score(unbroken, 	multiply, 0.2).
*/

score(catastrophically_rated, multiply, randomize(normal(1.9,0.1), [[>=, 0], [=<,2]])).
score(critically_rated, 	multiply, randomize(normal(1.4,0.1), [[>=, 0], [=<,2]])).
score(highly_rated, 	multiply, randomize(normal(1.1,0.1), [[=<,2],[>=, 0]])).
score(lowly_rated, 	multiply, randomize(normal(0.4,0.2), [[>=, 0], [=<,2]])).

score(c2p, multiply, 1).  % children to parent

% the following are non-randomizable
score(combine, add).  
score(stakeholder, 0).  
score(default, 1).  
score(not_done, 0).  
score(not_lurched, 0).
score(wout_claim_support, 0). 

% weight(Severity, SoftgoalName, Weight)

weight(extremelyCritical,_,randomize(normal(16,3.2), [[>=, 0], [=<,20]])).
weight(veryCritical,	_,randomize(normal(12,2.4), [[>=, 0], [=<,20]])).
weight(critical,	_,randomize(normal(8,1.6), [[>=, 0], [=<,20]])).
weight(normal,	_,randomize(normal(3,0.6), [[>=, 0], [=<,20]])).
weight(abduced,	_,1).
