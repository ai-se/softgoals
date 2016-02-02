### Results
- continuous domination
- uniform cost of 1 for each decision
- 4 objectivs(softgoals, goals, path_cost and decision_cost)
- Cost of a node is weighted proportional to the number of leaves the node has under it
  - Weight = (1 + 0.1 * number of incoming edges)

Models are sorted below w.r.t to their sizes in descending order

| Rank | Model | PDF |Report |
|------|-------|-----|-------|
| 1|CSServices| [pdf](../../../GMRepo/pdfs/CSServices.pdf)|[report](CSServices.md)|
| 2|CSFDandMarketing| [pdf](../../../GMRepo/pdfs/CSFDandMarketing.pdf)|[report](CSFDandMarketing.md)|
| 3|CSCounselling| [pdf](../../../GMRepo/pdfs/CSCounselling.pdf)|[report](CSCounselling.md)|
| 4|CSCounsellingManagement| [pdf](../../../GMRepo/pdfs/CSCounsellingManagement.pdf)|[report](CSCounsellingManagement.md)|
| 5|CSITDepartment| [pdf](../../../GMRepo/pdfs/CSITDepartment.pdf)|[report](CSITDepartment.md)|
| 6|CSSAProgram| [pdf](../../../GMRepo/pdfs/CSSAProgram.pdf)|[report](CSSAProgram.md)|
| 7|CSSimplifiedSD| [pdf](../../../GMRepo/pdfs/CSSimplifiedSD.pdf)|[report](CSSimplified.md)|
| 8|KidsAndYouth| [pdf](../../../GMRepo/pdfs/KidsAndYouth.pdf)|[report](KidsAndYouth.md)|
| 9|DelayModeratedBulletinBoard| [pdf](../../../GMRepo/pdfs/DelayModeratedBulletinBoard.pdf)| [report](DelayModeratedBulletinBoard.md)|
| 10|OOOChatRooms| [pdf](../../../GMRepo/pdfs/OOOChatRooms.pdf)|[report](OOOChatRooms.md)|
| 11|CSCounsellingManagementSD| [pdf](../../../GMRepo/pdfs/CSCounsellingManagementSD.pdf)| [report](CSCounsellingManagementSD.md)|
| 12|CSFDandMarketingSD| [pdf](../../../GMRepo/pdfs/CSFDandMarketingSD.pdf)|[report](CSFDandMarketingSD.md)|


Few Take Aways:
- Continous domination gives much better improvement compared to Binary Domination. Check the improvement rates in first 5 reports.
- Path cost including debate weights provide better results compared to not using a debate factor.
