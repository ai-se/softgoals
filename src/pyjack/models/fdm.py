from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from pyjack.template import *
from pyjack.utils import *
from pyjack.distribution import *
from pyjack.functions import evaluations
import operator as o

def percentile_95(x):
  return np.percentile(x, 95)

__author__ = "bigfatnoob"

sample_size = 10
m = Model("fda", sample_size)

o1 = m.objective(MAXIMIZE, evaluations["EV"](), "EV")
o2 = m.objective(MINIMIZE, percentile_95, "95P")


NbrLegitTransactionsPerAccountPerDay = m.input(Triangular(0, 3, 10), "NbrLegitTransactionsPerAccountPerDay")
NbrFraudPerCompromisedAccountPerDay1 = m.input(Triangular(0, 3, 10), "NbrFraudPerCompromisedAccountPerDay")
NbrLegitTransactions = m.variable("NbrLegitTransactions")
NbrFraud = m.variable("NbrFraud")
BatchClassifierTrueNegativeRate = m.decision({
  "low" : m.input(Triangular(0.95, 0.99, 0.995)),
  "medium" : m.input(Triangular(0.99, 0.995, 0.999)),
  "high" : m.input(Triangular(0.995, 0.999, 0.9999))
}, "alert threshold")
BatchTrueNegativeRate = m.decision({
  "classifier": BatchClassifierTrueNegativeRate,
  "rule-based": m.input(Constant(0.995))
}, "fraud-detection-method")
ContinuousAlertThreshold = m.decision({
  "low" : m.input(Triangular(0.75, 0.85, 0.95), "low-continuous-alert"),
	"medium" : m.input(Triangular(0.65, 0.75, 0.85), "medium-continuous-alert"),
	"high" : m.input(Triangular(0.55, 0.65, 0.75), "high-continuous-alert")
}, "alert threshold")
ContinuousTrueAlertRate = m.decision({
  "classifier" :  ContinuousAlertThreshold,
	"rule-based" :  m.input(Constant(0.75), "Continuous-Alert-rule-based")
}, "fraud detection method")
BatchAlertThreshold = m.decision({
	"low" : m.input(Triangular(0.75, 0.85, 0.95), "low-batch-alert"),
	"medium" : m.input(Triangular(0.65, 0.75, 0.85), "medium-batch-alert"),
	"high" : m.input(Triangular(0.55, 0.65, 0.75), "high-batch-alert")
}, "alert threshold")
BatchTrueAlertRate = m.decision({
	"classifier" :  BatchAlertThreshold,
	"rule-based" :  m.input(Constant(0.80), "Batch-Alert-rule-based")
}, "fraud detection method")
ContinuousClassierTrueNegativeRate = m.decision({
  "low" : m.input(Triangular(0.95, 0.99, 0.995)),
  "medium" : m.input(Triangular(0.99, 0.995, 0.999)),
  "high" : m.input(Triangular(0.995, 0.999, 0.9999))
}, "alert threshold")
ContinuousTrueNegativeRate = m.decision({
  "classifier" : ContinuousClassierTrueNegativeRate,
  "rule-based" : m.input(Constant(0.99), "Rule Based")
}, "fraud detection method")
TrueNegativeRate = m.decision({
  "continuous" : ContinuousTrueNegativeRate,
  "batch" : BatchTrueNegativeRate
}, "processing type")
TrueAlertRate = m.decision({
  "continuous" : ContinuousTrueAlertRate,
  "batch" : BatchTrueAlertRate
}, "processing type")
NegateTrueNegativeRate = m.variable("NegateTrueNegativeRate")
NbrFalseAlerts = m.variable("NbrFalseAlerts")
NbrTrueAlerts = m.variable("NbrTrueAlerts")
NbrAlerts = m.variable("NbrAlerts")
InvestigationDelay = m.input(Triangular(1/24, 1/3, 1))
NbrFraudDuringInvestigation = m.variable("NbrFraudDuringInvestigation")
NbrFraudPerCompromisedAccountPerDay = m.input(NormalCI(1, 20))
BATCHNbrFraudBeforeDetection = m.variable("BATCHNbrFraudBeforeDetection")
INVContinuousTrueAlertRate = m.variable("INVContinuousTrueAlertRate")
InvestigativeFirst = m.variable("InvestigativeFirst")
NbrFraudBeforeDetection = m.decision({
  "continuous" : INVContinuousTrueAlertRate,
  "batch" : BATCHNbrFraudBeforeDetection 
}, "Processing Type")
CompromisedAccountRatio = m.input(Triangular(0, 0.0001, 0.0003), "CompromisedAccountRatio")
NbrAccounts = m.input(NormalCI(0.9 * 10**6, 1.1 * 10**6), "NbrAccounts")
NbrFraudPerAccountBeforeBlocked = m.decision({
  "block first" : NbrFraudBeforeDetection,
  "investigate first": InvestigativeFirst
}, "Blocking Policy")
NbrCompromisedAccounts = m.variable("NbrCompromisedAccounts")
AverageFraudValue = m.input(NormalCI(100, 1000), "AverageFraudValue")
FinancialLoss = m.variable("FinancialLoss")
BaseLineFinancialLoss = m.input(Constant(500000), "BaseLineFinancialLoss")
Benefit = m.variable("Benefit")

m.add_edge(Benefit, o1)
m.add_edge(BaseLineFinancialLoss, Benefit, o.sub)
m.add_edge(FinancialLoss, Benefit, o.sub)
m.add_edge(AverageFraudValue, FinancialLoss, o.mul)
m.add_edge(NbrCompromisedAccounts, FinancialLoss, o.mul)
m.add_edge(NbrFraudPerAccountBeforeBlocked, FinancialLoss, o.mul)
m.add_edge(NbrAccounts, NbrCompromisedAccounts, o.mul)
m.add_edge(CompromisedAccountRatio, NbrCompromisedAccounts, o.mul)
m.add_edge(NbrFraudBeforeDetection, InvestigativeFirst, o.add)
m.add_edge(NbrFraudDuringInvestigation, InvestigativeFirst, o.add)
m.add_edge(m.input(Constant(1)), INVContinuousTrueAlertRate, o.div)
m.add_edge(ContinuousTrueAlertRate, INVContinuousTrueAlertRate, o.div)
m.add_edge(NbrFraudPerCompromisedAccountPerDay, BATCHNbrFraudBeforeDetection, o.div)
m.add_edge(BatchTrueAlertRate, BATCHNbrFraudBeforeDetection, o.div)
m.add_edge(NbrFraudPerCompromisedAccountPerDay, NbrFraudDuringInvestigation, o.mul)
m.add_edge(InvestigationDelay, NbrFraudDuringInvestigation, o.mul)


m.add_edge(NbrAlerts, o2)
m.add_edge(NbrTrueAlerts, NbrAlerts, o.add)
m.add_edge(NbrFalseAlerts, NbrAlerts, o.add)
m.add_edge(NbrFraud, NbrTrueAlerts, o.mul)
m.add_edge(TrueAlertRate, NbrTrueAlerts, o.mul)
m.add_edge(NbrLegitTransactions, NbrFalseAlerts, o.mul)
m.add_edge(NegateTrueNegativeRate, NbrFalseAlerts, o.mul)
m.add_edge(m.input(Constant(1)), NegateTrueNegativeRate, o.sub)
m.add_edge(TrueNegativeRate, NegateTrueNegativeRate, o.sub)
m.add_edge(NbrAccounts, NbrFraud, o.mul)
m.add_edge(CompromisedAccountRatio, NbrFraud, o.mul)
m.add_edge(NbrFraudPerCompromisedAccountPerDay1, NbrFraud, o.mul)
m.add_edge(NbrAccounts, NbrLegitTransactions, o.mul)
m.add_edge(NbrLegitTransactionsPerAccountPerDay, NbrLegitTransactions, o.mul)


# Test
# o1.dfs()
# o1.bfs()

m.test()