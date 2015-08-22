% logic_setup.pl
% contains the definition of logical ops
% all_of, one_of, none_of, any_of

% this should be moved to some other files...

rightness(stakeholder). 
rightness(god). 

roulette(positively_influenced,helped). 
roulette(positively_influenced,made). 

roulette(moderately_rated,critically_rated). % good effect anytime
roulette(moderately_rated,lowly_rated). % sometimes good sometimes bad

good_effect(helped).
good_effect(made).  
bad_effect(unhurt).  
bad_effect(unbroken).  

good_effect(catastrophically_rated).
good_effect(critically_rated).
good_effect(highly_rated).
bad_effect(lowly_rated). 

infer(all_of, rand). 
infer(one_of, rxor). 
infer(none_of, rnand). 
infer(any_of, rany). 
infer(any_one_of, ror).

%good_effect(positively_influenced).
%bad_effect(moderately_rated).

rouletting(effect(Roulette=G), effect(Out=G)) :- rouletting1(Roulette,Out).  
rouletting1(Roulette, Out) :- !, bagof(R, roulette(Roulette,R), Rs), once(rone(Rs, Out, _)).  
/*------------- logics and de morgan rules ----------------- %

TS = threshold of success (situation that leads to immediate success of lurch(Goal))
TF = threshold of failure (situation that leads to immediate success of lurch(not Goal))
Attempts (number of times to try lurching the rest of the Nodes after success)

internal_logics	|TS		|TF		|Attempts(TS/TF)
	and	|(A,0)		|(_,1)		|A/1
	or	|(1,_)		|(0,A)		|1/A
	any	|(1,_)		|(0,A)		|A/A
	xor	|(1, (A-1))	|(0,_);(2,_)	|A/A;2
	nand	|(0,A)		|(1,_)		|A/1
	nor	|(_,1)		|(A,0)		|1/A
	nany	|(_,1)		|(A,0)		|A/A
	
note:  TF is equivalent to de-morganed situation
_ means whatever
so it boils down to	
Logic	numNode,numNotNode,Attempts
and: 	A,0,A
or:	1,_,1
any:	1,_,A
xor:	1,(A-1),A
nand:	0,A,A
nor:	_,1,1
nany:	_,1,A

dand: 	_,1,1 	->nor
dor:	0,A,A	->nand
dany:	0,A,A	->nand
dxor:	(0,A,A) or (2,_,2)
dnand:	1,_,1	->or
dnor:	A,0,A	->and
dnany:	A,0,A	->and

dc= don't care

% ------------- logics and de morgan rules -----------------*/

lurch_logic(and, 	[seq=l2r,		y=all,	n=dc,	ytries=all,	ntries=0]).
lurch_logic(rand, 	[seq=rone,	y=all,	n=dc,	ytries=all,	ntries=0]).
lurch_logic(or, 	[seq=l2r,		y=1,	n=dc,	ytries=1,	ntries=0]).
lurch_logic(ror, 	[seq=rone,	y=1,	n=dc,	ytries=1,	ntries=0]).
lurch_logic(any, 	[seq=l2r,		y=1,	n=dc,	ytries=all,	ntries=0]).
lurch_logic(rany, 	[seq=rone,	y=1,	n=dc,	ytries=all,	ntries=0]).
lurch_logic(xor, 	[seq=l2r,		y=1,	n=xc(1),	ytries=1,	ntries=xc(1)]).
lurch_logic(rxor, 	[seq=rone,	y=1,	n=xc(1),	ytries=1,	ntries=xc(1)]).
lurch_logic(nand, 	[seq=l2r,		y=dc,	n=all,	ytries=0,	ntries=all]).
lurch_logic(rnand, 	[seq=rone,	y=dc,	n=all,	ytries=0,	ntries=all]).
lurch_logic(nor, 	[seq=l2r,		y=dc,	n=1,	ytries=0,	ntries=1]).
lurch_logic(rnor, 	[seq=rone,	y=dc,	n=1,	ytries=0,	ntries=1]).
lurch_logic(nany, 	[seq=l2r,		y=dc,	n=1,	ytries=0,	ntries=all]).
lurch_logic(nrany,	[seq=rone,	y=dc,	n=1,	ytries=0,	ntries=all]).
lurch_logic(dxor1, 	[seq=l2r,		y=2,	n=dc,	ytries=2,	ntries=0]).
lurch_logic(rdxor1, 	[seq=rone,	y=2,	n=dc,	ytries=2,	ntries=0]).

lurch_logic(dxor, L) :- lurch_logic(dxor1, L); lurch_logic(nand, L). 
lurch_logic(rdxor, L) :- lurch_logic(rdxor1, L); lurch_logic(rnand, L). 

de_morgan(and, nor). 
de_morgan(rand, rnor). 
de_morgan(or, nand). 
de_morgan(ror, rnand). 
de_morgan(any, nand).   
de_morgan(rany, rnand).  
de_morgan(nand, or).
de_morgan(rnand, ror).
de_morgan(nor, and).
de_morgan(rnor, rand).
de_morgan(nany, and). 
de_morgan(xor, dxor).  
de_morgan(rxor, rdxor). 

% invert_effect
% can't figure out a better way to handle negation of claim2parent
invert_effect(A,B) :- check( effects, A), invert_effect1(A,B).  

invert_effect1(A,A) :- check(roulette, A).  

invert_effect1(helped, unhurt).
invert_effect1(made, unbroken).

invert_effect1(catastrophically_rated, lowly_rated). 
invert_effect1(critically_rated, lowly_rated). 
invert_effect1(highly_rated, lowly_rated). 

invert_effect1(A,B) :- invert_effect1(B,A).  

