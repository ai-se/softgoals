## CSITDepartment
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,    76.32  ,   5.27 (    ----  * ---|-----         ),68.42, 73.68, 76.32, 78.95, 89.47
   2 ,     gen20_f1 ,    86.84  ,    7.9 (            ---|-    * --     ),78.95, 84.21, 89.47, 92.11, 94.74
   3 ,     gen40_f1 ,    89.47  ,   5.27 (              -|---  * --     ),81.58, 86.84, 89.47, 92.11, 94.74
   3 ,     gen80_f1 ,    89.47  ,   5.27 (              -|-----  *---   ),81.58, 89.47, 92.11, 92.11, 97.37
   3 ,     gen60_f1 ,    92.11  ,   5.27 (              -|-----  *---   ),81.58, 89.47, 92.11, 92.11, 97.37
   3 ,    gen100_f1 ,    92.11  ,   5.27 (              -|-----  * --   ),81.58, 89.47, 92.11, 94.74, 97.37

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,     91.3  ,   8.69 (            ---|-*            ),86.96, 91.30, 91.30, 95.65, 95.65
   2 ,     gen20_f2 ,    95.65  ,   4.35 (               |       *----- ),91.30, 91.30, 95.65, 95.65, 100.00
   2 ,     gen40_f2 ,    95.65  ,   4.35 (               | ------*----- ),91.30, 95.65, 95.65, 95.65, 100.00
   2 ,     gen60_f2 ,    95.65  ,    8.7 (               | ------*----- ),91.30, 95.65, 95.65, 95.65, 100.00
   2 ,     gen80_f2 ,    95.65  ,   4.35 (               | ------*----- ),91.30, 95.65, 95.65, 95.65, 100.00
   2 ,    gen100_f2 ,    95.65  ,    8.7 (               | ------*----- ),91.30, 95.65, 95.65, 95.65, 100.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f3 ,    63.23  ,  14.35 (   --  *   ----|-             ),53.17, 58.69, 63.43, 70.45, 84.21
   2 ,     gen20_f3 ,     77.8  ,  13.44 (         ---   * ---          ),66.62, 72.37, 79.54, 84.66, 89.95
   2 ,    gen100_f3 ,    81.55  ,  12.34 (           --- | * ----       ),70.62, 77.45, 82.79, 88.63, 95.69
   2 ,     gen40_f3 ,     83.1  ,  14.74 (           --- | *---         ),70.98, 77.48, 83.16, 86.74, 91.76
   2 ,     gen60_f3 ,    83.32  ,  11.97 (           ----| * --         ),70.62, 79.54, 83.92, 87.83, 93.11
   2 ,     gen80_f3 ,    83.32  ,   12.0 (           --- | * ----       ),70.62, 77.80, 83.92, 88.60, 95.69

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,     gen80_f4 ,      9.0  ,    2.0 (   ---   *   --|              ), 7.00,  8.00,  9.00, 10.00, 11.00
   1 ,    gen100_f4 ,      9.0  ,    3.0 (   ---   *   --|              ), 7.00,  8.00,  9.00, 10.00, 11.00
   2 ,      gen0_f4 ,      9.0  ,    4.0 (   ------    * |   -------    ), 7.00,  9.00, 10.00, 12.00, 14.00
   2 ,     gen20_f4 ,     10.0  ,    2.0 (      ---    * |-------       ), 8.00,  9.00, 10.00, 11.00, 13.00
   2 ,     gen40_f4 ,     10.0  ,    3.0 (   ------    *-|---           ), 7.00,  9.00, 10.00, 10.00, 12.00
   2 ,     gen60_f4 ,     10.0  ,    2.0 (   ---       *-|---           ), 7.00,  8.00, 10.00, 10.00, 12.00
```

### Time Taken : 31.2475948334
![1](../../../src/img/weighted_uniform/CSITDepartment.png)

### Decisions Ranked
```
+------+-------------------------------------------------+----------+-------+------+
| rank |                       name                      |   type   | value | cost |
+------+-------------------------------------------------+----------+-------+------+
|  1   |                      Use T1                     |   task   |   1   |  1   |
|  2   |         Provide Online Donor Technology1        |   task   |   -1  |  1   |
|  3   |                     Use VPN                     |   task   |   -1  |  1   |
|  4   |                  Free Software                  | resource |   1   |  1   |
|  5   |                  Free Upgrades                  | resource |   -1  |  1   |
|  6   |  Perform Donor/Accounting Data Base Maintenance |   task   |   -1  |  1   |
|  7   |            Put Content Onto Website1            |   task   |   -1  |  1   |
|  8   |                   Network PCs                   |   task   |   -1  |  1   |
|  9   |                      Oracle                     | resource |   -1  |  1   |
|  10  |      Use Informal Buddy System for Training     |   task   |   1   |  1   |
|  11  |                Use Current Method               |   task   |   -1  |  1   |
|  12  |                   IT Resources                  | resource |   1   |  1   |
|  13  |                     Hardware                    | resource |   -1  |  1   |
|  14  |                     Upgrades                    | resource |   1   |  1   |
|  15  |            !Implement Phone Feedback1           |   task   |   1   |  1   |
|  16  | Provide Technology to Create and Send Documents |   task   |   -1  |  1   |
|  17  |                  Free Hardware                  | resource |   -1  |  1   |
|  18  |                     Software                    | resource |   1   |  1   |
|  19  |                   Web Server1                   | resource |   -1  |  1   |
|  20  |         *Implement Email for Counsellors        |   task   |   -1  |  1   |
|  21  |                 Free Web Server                 | resource |   1   |  1   |
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
|                     Hardware Be Acquired for Free                      |   task   |   -1  |
|                                Use VPN                                 |   task   |   -1  |
|    Sensitive to the Environment IT Equipment will Be Introduced to     | softgoal |  0.5  |
|                  !Calls Be Recorded into a Data Base1                  |   goal   |   1   |
|               IT Training/Support Be Given to Employees                |   goal   |   1   |
|                              IT Resources                              | resource |   1   |
|   Properly and Suitably Equipped in IT [to Accomplish Service Goals]   | softgoal |  -0.5 |
|                                 Oracle                                 | resource |   -1  |
|                    Decrease Clumsiness [Technology]                    | softgoal |   1   |
|                        Use Oracle for Data Base                        |   task   |   -1  |
|                    Provide Document Library System1                    |   task   |   1   |
|                       Cost Effective Technology                        | softgoal |  -0.5 |
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
|                            Free Web Server                             | resource |   -1  |
|               Easily Accessable Technology Instructions                | softgoal |   1   |
|                         *Hardware Be Acquired                          |   goal   |   -1  |
|                     *Implement Categorization Tool                     |   task   |   1   |
|                       !An IT Trainer Be Present                        |   goal   |   1   |
|                      Feedback Form Be Implemented                      |   task   |   1   |
|                       !Implement Phone Feedback1                       |   task   |   1   |
|                  Support Analysis [Counsellors Time]1                  | softgoal |  0.5  |
|            Provide Technology to Create and Send Documents             |   task   |   1   |
|                              Network PCs                               |   task   |   -1  |
|                             Free Software                              | resource |   1   |
|                          Simple [Technology]1                          | softgoal |  0.5  |
|                Increase IT Methods to Acquire Feedback                 | softgoal |  0.5  |
|                           *Pay for Software                            |   task   |   1   |
|          Implement Director Enterprise through Blue Pumpkin            |   task   |   1   |
|                 Telephony Be Implemented and Managed1                  |   goal   |   1   |
|                      *Implement Activity Manager                       |   task   |   1   |
|                Adequately Customizable [CS Technology]                 | softgoal |   1   |
|                          Simple [Technology]                           | softgoal |  0.5  |
|                           Use Current Method                           |   task   |   -1  |
| Properly and Suitably Equipped in IT [to Accomplish Fundraising Needs] | softgoal |  0.5  |
|                 Improve Quality Assurance Technology1                  | softgoal |  0.5  |
|      Increased Emphasis on IT in Hiring Process [of Counsellors]       | softgoal |   1   |
|           Increase Access Speed [  Regional Offices to DL]1            | softgoal |   1   |
|                    *Implement Email for Counsellors                    |   task   |   1   |
|                      Keep Up With New Technology                       | softgoal |  -0.5 |
|                          Acquire IT Resources                          |   task   |   1   |
|                                 Use T1                                 |   task   |   1   |
|                         *Effective IT Training                         | softgoal |  0.5  |
|                        Install Desktop Software                        |   task   |   1   |
|                   Decrease Clumsiness [Technology]1                    | softgoal |   1   |
|                 Use Informal Buddy System for Training                 |   task   |   1   |
|                       *Acquire Software for Free                       |   task   |   1   |
|                    !A Training Computer Be Present1                    |   goal   |   1   |
|                       Adjust to Software Changes                       | softgoal |  -0.5 |
|                             Free Hardware                              | resource |   -1  |
|                Consideration of Feedback [IT Providers]                | softgoal |   1   |
|                         Increase IT Resources1                         | softgoal |   1   |
|                  Telephony Be Implemented and Managed                  |   task   |   1   |
|                      *Implement Symposium System                       |   task   |   1   |
|                                Software                                | resource |   1   |
|                            Pay for Hardware                            |   task   |   -1  |
|                   Manage Donor/ Accounting Data Base                   |   task   |   -1  |
|                              Web Server1                               | resource |   1   |
|              *IT Providers have Knowledge of Counselling               |   goal   |   1   |
|       !Performance Review Information Be Collected in Data Base1       |   goal   |   1   |
|                       !IT Systems Be Integrated                        |   goal   |   1   |
|                          Expand IT Department                          | softgoal |  -0.5 |
|                            Acquire Software                            |   goal   |   1   |
|                        *Web Server Be Acquired                         |   goal   |   1   |
|                         CS Be Not for Profit1                          |   goal   |   1   |
|      Increased Emphasis on IT in Hiring Process [of Counsellors]1      | softgoal |   1   |
|                         Increase IT Resources                          | softgoal |  -0.5 |
|                      *Acquire Web Server for Free                      |   task   |   -1  |
|                   Improve [Call Recording Equipment]                   | softgoal |   1   |
|                                Hardware                                | resource |   -1  |
|                                Upgrades                                | resource |   1   |
|                  !Calls Be Recorded into a Data Base                   |   goal   |   1   |
|                       *Implement Bulletin Board                        |   task   |   1   |
|                             IT Be Upgraded                             |   goal   |   1   |
|             Perform Donor/Accounting Data Base Maintenance             |   task   |   -1  |
|              Consideration of Feedback [from Counsellors]              | softgoal |   1   |
|                *Increase [IT Training for Counsellors]                 | softgoal |  0.5  |
|                          *Pay for Web Server                           |   task   |   1   |
|                  Support Analysis [Counsellors Time]                   | softgoal |  0.5  |
|                    Provide Online Donor Technology1                    |   task   |   -1  |
|               IT Dept Provides Orientation and Training                |   task   |   1   |
|                       *Web Software Be Acquired                        |   goal   |   1   |
|                    !A Training Computer Be Present                     |   goal   |   1   |
|                     Increase IT Training Resources                     | softgoal |  -0.5 |
|              Provide Peer-to-Peer Access Regional Offices              |   goal   |   1   |
|                Increase IT Methods to Acquire Feedback1                | softgoal |  0.5  |
+------------------------------------------------------------------------+----------+-------+
```
