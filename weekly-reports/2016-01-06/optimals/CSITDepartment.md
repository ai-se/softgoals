## CSITDepartment
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,    78.95  ,  10.53 (      ----  *  | ------       ),71.05, 76.32, 78.95, 84.21, 92.11
   2 ,     gen20_f1 ,    89.47  ,    7.9 (          -----|---  * ----   ),76.32, 86.84, 89.47, 92.11, 97.37
   3 ,     gen40_f1 ,    92.11  ,   5.27 (              -|-----  * --   ),81.58, 89.47, 92.11, 94.74, 97.37
   3 ,     gen60_f1 ,    92.11  ,   5.27 (               |   --  * --   ),86.84, 89.47, 92.11, 94.74, 97.37
   3 ,     gen80_f1 ,    92.11  ,   2.63 (               |   ----* --   ),86.84, 92.11, 92.11, 94.74, 97.37
   3 ,    gen100_f1 ,    92.11  ,   2.63 (               |   ----  *-   ),86.84, 92.11, 94.74, 94.74, 97.37

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,     91.3  ,   8.69 (            ---|-*            ),86.96, 91.30, 91.30, 95.65, 95.65
   2 ,     gen20_f2 ,    95.65  ,   4.35 (            ---|-      *----- ),86.96, 91.30, 95.65, 95.65, 100.00
   2 ,     gen40_f2 ,    95.65  ,    0.0 (               | ------*----- ),91.30, 95.65, 95.65, 95.65, 100.00
   2 ,     gen60_f2 ,    95.65  ,   4.35 (               | ------*      ),91.30, 95.65, 95.65, 100.00, 100.00
   2 ,     gen80_f2 ,    95.65  ,   4.35 (               | ------*      ),91.30, 95.65, 95.65, 100.00, 100.00
   2 ,    gen100_f2 ,    95.65  ,   4.35 (               | ------*      ),91.30, 95.65, 95.65, 100.00, 100.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,     gen80_f3 ,      8.0  ,    3.0 (     ---     * |-----         ), 6.00,  7.00,  9.00, 10.00, 12.00
   1 ,    gen100_f3 ,      8.0  ,    2.0 (     ---     *-|---           ), 6.00,  7.00,  9.00,  9.00, 11.00
   2 ,     gen20_f3 ,      9.0  ,    3.0 (     -----   * |   --         ), 6.00,  8.00,  9.00, 11.00, 12.00
   2 ,     gen40_f3 ,      9.0  ,    3.0 (     -----   * |-----         ), 6.00,  8.00,  9.00, 10.00, 12.00
   2 ,     gen60_f3 ,      9.0  ,    3.0 (     ---     * |-----         ), 6.00,  7.00,  9.00, 10.00, 12.00
   3 ,      gen0_f3 ,      9.0  ,    4.0 (        -----  |*    ------   ), 7.00,  9.00, 10.00, 12.00, 14.00
```

### Time Taken : 28.5812339783
![1](../../../src/img/optimals/CSITDepartment.png)
```
+------+-------------------------------------------------+----------+-------+------+
| rank |                       name                      |   type   | value | cost |
+------+-------------------------------------------------+----------+-------+------+
|  1   |                      Use T1                     |   task   |   1   |  1   |
|  2   |         Provide Online Donor Technology1        |   task   |   -1  |  1   |
|  3   |                   Network PCs                   |   task   |   -1  |  1   |
|  4   |                  Free Hardware                  | resource |   1   |  1   |
|  5   |      Use Informal Buddy System for Training     |   task   |   1   |  1   |
|  6   |                 Free Web Server                 | resource |   1   |  1   |
|  7   |                  Free Upgrades                  | resource |   -1  |  1   |
|  8   |         *Implement Email for Counsellors        |   task   |   -1  |  1   |
|  9   |            !Implement Phone Feedback1           |   task   |   -1  |  1   |
|  10  |                   Web Server1                   | resource |   -1  |  1   |
|  11  |                     Hardware                    | resource |   -1  |  1   |
|  12  |            Put Content Onto Website1            |   task   |   -1  |  1   |
|  13  |                  Free Software                  | resource |   1   |  1   |
|  14  | Provide Technology to Create and Send Documents |   task   |   1   |  1   |
|  15  |                Use Current Method               |   task   |   -1  |  1   |
|  16  |                     Upgrades                    | resource |   1   |  1   |
|  17  |                     Software                    | resource |   1   |  1   |
|  18  |                     Use VPN                     |   task   |   -1  |  1   |
|  19  |  Perform Donor/Accounting Data Base Maintenance |   task   |   -1  |  1   |
|  20  |                   IT Resources                  | resource |   -1  |  1   |
|  21  |                      Oracle                     | resource |   -1  |  1   |
+------+-------------------------------------------------+----------+-------+------+
```

### Top 14 Decisions from above table.
```
+------------------------------------------------------------------------+----------+-------+
|                                  name                                  |   type   | value |
+------------------------------------------------------------------------+----------+-------+
|               Easily Accessable Technology Instructions1               | softgoal |   1   |
|     Properly and Suitably Equipped in IT [to Accomplish CS Needs]1     | softgoal |  0.5  |
|                             Free Upgrades                              | resource |   -1  |
|            Increase Access Speed [  Regional Offices to DL]            | softgoal |   1   |
|                       Put Content Onto Website1                        |   task   |   -1  |
|                  Improve Quality Assurance Technology                  | softgoal |  0.5  |
|                     Hardware Be Acquired for Free                      |   task   |   1   |
|                                Use VPN                                 |   task   |   1   |
|    Sensitive to the Environment IT Equipment will Be Introduced to     | softgoal |  0.5  |
|                  !Calls Be Recorded into a Data Base1                  |   goal   |   1   |
|               IT Training/Support Be Given to Employees                |   goal   |   1   |
|                              IT Resources                              | resource |   1   |
|   Properly and Suitably Equipped in IT [to Accomplish Service Goals]   | softgoal |  0.5  |
|                                 Oracle                                 | resource |   -1  |
|                    Decrease Clumsiness [Technology]                    | softgoal |   1   |
|                        Use Oracle for Data Base                        |   task   |   -1  |
|                    Provide Document Library System1                    |   task   |   1   |
|                       Cost Effective Technology                        | softgoal |  0.5  |
|                           *Pay for Upgrades                            |   task   |   1   |
|         Call Center Server and Scheduling System Be Integrated         |   goal   |   1   |
|                  Improve [Call Recording Equipment]1                   | softgoal |   1   |
|          Fit Between System Capabilities and CS Requirements           | softgoal |  0.5  |
|     Properly and Suitably Equipped in IT [to Accomplish CS Needs]      | softgoal |  0.5  |
|                         !Integrate IT Systems                          |   goal   |   1   |
|       !Performance Review Information Be Collected in Data Base        |   goal   |   1   |
|                          CS Be Not for Profit                          |   goal   |   1   |
|                *Increase [IT Training for Counsellors]1                | softgoal |  0.5  |
|                       !An IT Trainer Be Present1                       |   goal   |   1   |
|                        *Cost Effective Training                        | softgoal |  -0.5 |
|       *IT Providers have Knowledge of Fundraising and Marketing        |   goal   |   1   |
|                            Free Web Server                             | resource |   1   |
|               Easily Accessable Technology Instructions                | softgoal |   1   |
|                         *Hardware Be Acquired                          |   goal   |   1   |
|                     *Implement Categorization Tool                     |   task   |   1   |
|                       !An IT Trainer Be Present                        |   goal   |   1   |
|                      Feedback Form Be Implemented                      |   task   |   1   |
|                       !Implement Phone Feedback1                       |   task   |   -1  |
|                  Support Analysis [Counsellors Time]1                  | softgoal |  0.5  |
|            Provide Technology to Create and Send Documents             |   task   |   1   |
|                              Network PCs                               |   task   |   -1  |
|                             Free Software                              | resource |   1   |
|                          Simple [Technology]1                          | softgoal |  0.5  |
|                Increase IT Methods to Acquire Feedback                 | softgoal |  0.5  |
|                           *Pay for Software                            |   task   |   -1  |
|          Implement Director Enterprise through Blue Pumpkin            |   task   |   1   |
|                 Telephony Be Implemented and Managed1                  |   goal   |   1   |
|                      *Implement Activity Manager                       |   task   |   1   |
|                Adequately Customizable [CS Technology]                 | softgoal |   1   |
|                             Implement IVR                              |   task   |   1   |
|                          Simple [Technology]                           | softgoal |  0.5  |
|                           Use Current Method                           |   task   |   1   |
| Properly and Suitably Equipped in IT [to Accomplish Fundraising Needs] | softgoal |  0.5  |
|                 Improve Quality Assurance Technology1                  | softgoal |  0.5  |
|      Increased Emphasis on IT in Hiring Process [of Counsellors]       | softgoal |   1   |
|           Increase Access Speed [  Regional Offices to DL]1            | softgoal |   1   |
|                    *Implement Email for Counsellors                    |   task   |   -1  |
|                      Keep Up With New Technology                       | softgoal |  0.5  |
|                          Acquire IT Resources                          |   task   |   1   |
|                                 Use T1                                 |   task   |   1   |
|                         *Effective IT Training                         | softgoal |  0.5  |
|                        Install Desktop Software                        |   task   |   1   |
|                   Decrease Clumsiness [Technology]1                    | softgoal |   1   |
|                 Use Informal Buddy System for Training                 |   task   |   1   |
|                       *Acquire Software for Free                       |   task   |   1   |
|                    !A Training Computer Be Present1                    |   goal   |   1   |
|                       Adjust to Software Changes                       | softgoal |  -0.5 |
|                             Free Hardware                              | resource |   1   |
|                Consideration of Feedback [IT Providers]                | softgoal |   1   |
|                         Increase IT Resources1                         | softgoal |   1   |
|                  Telephony Be Implemented and Managed                  |   task   |   1   |
|                                Software                                | resource |   -1  |
|                            Pay for Hardware                            |   task   |   -1  |
|                   Manage Donor/ Accounting Data Base                   |   task   |   1   |
|                              Web Server1                               | resource |   -1  |
|              *IT Providers have Knowledge of Counselling               |   goal   |   1   |
|       !Performance Review Information Be Collected in Data Base1       |   goal   |   1   |
|                       !IT Systems Be Integrated                        |   goal   |   1   |
|                          Expand IT Department                          | softgoal |  -0.5 |
|                            Acquire Software                            |   goal   |   1   |
|                        *Web Server Be Acquired                         |   goal   |   1   |
|                         CS Be Not for Profit1                          |   goal   |   1   |
|      Increased Emphasis on IT in Hiring Process [of Counsellors]1      | softgoal |   1   |
|                         Increase IT Resources                          | softgoal |  -0.5 |
|                      *Acquire Web Server for Free                      |   task   |   1   |
|                   Improve [Call Recording Equipment]                   | softgoal |   1   |
|                                Hardware                                | resource |   -1  |
|                                Upgrades                                | resource |   1   |
|                  !Calls Be Recorded into a Data Base                   |   goal   |   1   |
|                       *Implement Bulletin Board                        |   task   |   1   |
|                             IT Be Upgraded                             |   goal   |   1   |
|             Perform Donor/Accounting Data Base Maintenance             |   task   |   1   |
|              Consideration of Feedback [from Counsellors]              | softgoal |   1   |
|                *Increase [IT Training for Counsellors]                 | softgoal |  0.5  |
|                          *Pay for Web Server                           |   task   |   -1  |
|                  Support Analysis [Counsellors Time]                   | softgoal |  0.5  |
|                    Provide Online Donor Technology1                    |   task   |   -1  |
|               IT Dept Provides Orientation and Training                |   task   |   1   |
|                       *Web Software Be Acquired                        |   goal   |   1   |
|                    !A Training Computer Be Present                     |   goal   |   1   |
|                     Increase IT Training Resources                     | softgoal |  0.5  |
|              Provide Peer-to-Peer Access Regional Offices              |   goal   |   1   |
|                Increase IT Methods to Acquire Feedback1                | softgoal |  0.5  |
+------------------------------------------------------------------------+----------+-------+
```