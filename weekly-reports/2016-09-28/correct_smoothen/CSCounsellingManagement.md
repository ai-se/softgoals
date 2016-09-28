## CSCounsellingManagement
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,    33.06  ,   5.78 (-------       *|-             ),22.31, 28.10, 33.88, 33.88, 35.54
   1 ,      gen2_f1 ,    36.36  ,   1.65 (          -----|-  *--        ),30.58, 35.54, 37.19, 37.19, 39.67
   2 ,      gen4_f1 ,     40.5  ,   2.48 (               |   --   *     ),37.19, 38.84, 41.32, 42.15, 42.15
   3 ,      gen6_f1 ,    42.15  ,   1.66 (               |     ---  *-  ),38.84, 41.32, 42.98, 43.80, 44.63
   3 ,      gen8_f1 ,    42.98  ,   1.65 (               |        -  *- ),41.32, 42.15, 43.80, 44.63, 45.45
   3 ,     gen10_f1 ,    42.98  ,   1.65 (               |        --  * ),41.32, 42.98, 44.63, 45.45, 45.45

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,    38.89  ,  13.89 (               |*      ---    ),38.89, 38.89, 52.78, 58.33, 61.11
   1 ,      gen2_f2 ,    52.78  ,   8.34 (------         |*             ),38.89, 44.44, 52.78, 61.11, 61.11
   1 ,      gen4_f2 ,    52.78  ,  11.11 (      -------  |          *-- ),44.44, 50.00, 61.11, 61.11, 63.89
   2 ,      gen6_f2 ,    58.33  ,  11.11 (               |             *),52.78, 52.78, 63.89, 63.89, 63.89
   2 ,      gen8_f2 ,    61.11  ,   5.56 (               |             *),58.33, 58.33, 63.89, 63.89, 63.89
   2 ,     gen10_f2 ,    61.11  ,   2.78 (               |       ---   *),58.33, 61.11, 63.89, 63.89, 63.89
```
![1](../../../src/img/correction/CSCounsellingManagement.png)
### Smoothened Plot
![1](../../../src/img/correction/CSCounsellingManagement_smooth.png)

### Decisions Ranked
```
+------+--------------------------------------------------------------------+----------+-------+------+---------+
| rank |                                name                                |   type   | value | cost | support |
+------+--------------------------------------------------------------------+----------+-------+------+---------+
|  1   |        Write Yearly Peformance Evaluations for Counsellors         |   task   |   1   |  1   | 0.00601 |
|  2   |         Three Months of Review Be Given to New Counsellors         |   goal   |   1   |  1   | 0.00601 |
|  3   |               Create Call Classification Catagories                |   task   |   1   |  1   | 0.00569 |
|  4   |    Clear Communication About the Purpose of IT [to Counselors]     | softgoal |   1   |  1   | 0.00541 |
|  5   |                          Double Head Set                           | resource |   1   |  1   | 0.00515 |
|  6   |          Increase Comfortableness [with Learning Process]          | softgoal |   1   |  1   | 0.00491 |
|  7   |                     !Hire Counselling Managers                     |   task   |   1   |  1   | 0.00491 |
|  8   |               Reduce Spending on Employees Salaries                | softgoal |   1   |  1   | 0.00491 |
|  9   |                      Set Counselling Policies                      |   task   |   1   |  1   | 0.00491 |
|  10  |                   Put on Web Moderator Meetings                    |   task   |   1   |  1   |  0.0045 |
|  11  |        Support Day to Day on the Floor Needs of Counsellors        | softgoal |   1   |  1   |  0.0045 |
|  12  |                  Professional Counsellors Be Used                  |   goal   |   1   |  1   | 0.00432 |
|  13  |             Provide One-on-One Support to Counsellors              |   task   |   1   |  1   | 0.00432 |
|  14  |                Feedback to Counsellors Be Provided                 |   goal   |   1   |  1   | 0.00416 |
|  15  |                            Review Tape                             |   task   |   -1  |  1   | 0.00416 |
|  16  |              !Improve Job Descriptions [Counsellors]               | softgoal |   1   |  1   |  0.004  |
|  17  |                   !A Training Program Be Present                   |   goal   |   1   |  1   |  0.004  |
|  18  |                    !A Training Room Be Present                     |   goal   |   1   |  1   | 0.00386 |
|  19  |                           Request Shifts                           |   task   |   1   |  1   | 0.00386 |
|  20  |                  Historical Data of Call Volumes                   | resource |   1   |  1   | 0.00373 |
|  21  |                  Rigorous [Employee Evaluations]                   | softgoal |   1   |  1   | 0.00349 |
|  22  |             Put on Orientation Process for Cousellors              |   task   |   1   |  1   | 0.00328 |
|  23  |                   Bilingual Counsellors Be Hired                   |   goal   |   1   |  1   | 0.00309 |
|  24  |                       Counselling Resources                        | resource |   -1  |  1   |  0.003  |
|  25  |                !Calls Be Recorded into a Data Base1                |   goal   |   -1  |  1   | 0.00292 |
|  26  |             Communicate CS Information to Counsellors              |   task   |   -1  |  1   | 0.00292 |
|  27  |                       Contracts Be Reviewed                        |   goal   |   1   |  1   | 0.00292 |
|  28  |                Acquire Web Training from Operations                |   task   |   -1  |  1   | 0.00292 |
|  29  |                     Positive Internal Opinion                      | softgoal |   -1  |  1   | 0.00292 |
|  30  |                         Debrief Web Posts                          |   task   |   -1  |  1   | 0.00292 |
|  31  |                      Happiness [Counsellors]1                      | softgoal |   -1  |  1   | 0.00292 |
|  32  |               Improved Writing Skills [Counsellors]                | softgoal |   -1  |  1   | 0.00292 |
|  33  |   Perform Counselling as Instructed By Supervisor [Counsellors]    | softgoal |   -1  |  1   | 0.00292 |
|  34  |                     !An IT Trainer Be Present1                     |   goal   |   1   |  1   | 0.00292 |
|  35  |                  Increased Counselling Resources                   | softgoal |   -1  |  1   | 0.00292 |
|  36  |                   Consider Counsellors Feedback                    | softgoal |   -1  |  1   | 0.00292 |
|  37  |            Counsellors Pass Probation within Six Months            |   goal   |   1   |  1   | 0.00292 |
|  38  |                     Avoid Liability Problems1                      | softgoal |   -1  |  1   | 0.00292 |
|  39  |                        Improve [IT Skills]                         | softgoal |   -1  |  1   | 0.00292 |
|  40  |                   Increase Funding for Training                    | softgoal |   -1  |  1   | 0.00292 |
|  41  |                Support Analysis [Counsellors Time]1                | softgoal |   -1  |  1   | 0.00292 |
|  42  |                  Negotiate with Counsellors Union                  |   task   |   -1  |  1   | 0.00292 |
|  43  |     !Performance Review Information Be Collected in Data Base1     |   goal   |   -1  |  1   | 0.00292 |
|  44  |              Increase IT Methods to Acquire Feedback               | softgoal |   -1  |  1   | 0.00292 |
|  45  |                     *High Quality Counselling2                     | softgoal |   -1  |  1   | 0.00292 |
|  46  |                        Policies Be Reviewed                        |   goal   |   1   |  1   | 0.00292 |
|  47  |         Pressure Counsellors [to Provide Online Services]          | softgoal |   -1  |  1   | 0.00292 |
|  48  |                  !A Training Computer Be Present1                  |   goal   |   -1  |  1   | 0.00292 |
|  49  |                  Counselling Policies Be Followed                  |   goal   |   1   |  1   | 0.00292 |
|  50  |            Avoid Relationships with Specific Counsellor            | softgoal |   -1  |  1   | 0.00292 |
|  51  |                      Analyze Staffing Levels                       |   goal   |   -1  |  1   | 0.00292 |
|  52  |                           Debrief Calls                            |   task   |   -1  |  1   | 0.00292 |
|  53  |                       Analyze Service Levels                       |   goal   |   -1  |  1   | 0.00292 |
|  54  |                   Professional Work Environment1                   | softgoal |   -1  |  1   | 0.00292 |
|  55  |              Holes in Operations Managing Be Removed               |   goal   |   -1  |  1   | 0.00292 |
|  56  |          Facilitate Faster Changes in Counsellor Duties1           | softgoal |   -1  |  1   | 0.00292 |
|  57  |                 Improve [Call Recording Equipment]                 | softgoal |   -1  |  1   | 0.00292 |
|  58  |               Full Time Night Complement Be Acquired               |   goal   |   1   |  1   | 0.00292 |
|  59  |                        Counsellors Be Paid                         |   task   |   -1  |  1   | 0.00292 |
|  60  |              *Increase [IT Training for Counsellors]               | softgoal |   -1  |  1   | 0.00292 |
|  61  |               Clearer Call Classification Catagories               | softgoal |   -1  |  1   | 0.00292 |
|  62  |          Supervision Be Performed At Least Every 3 Months          |   goal   |   -1  |  1   | 0.00292 |
|  63  | Technology Be Used to Ensure Counsellors are Keeping Correct Hours |   goal   |   1   |  1   | 0.00292 |
|  64  |                          Use Blue Pumpkin                          |   task   |   -1  |  1   | 0.00292 |
|  65  |                         !Hire Counsellors                          |   task   |   1   |  1   | 0.00225 |
|  66  |                    Put On Counselling Workshops                    |   task   |   1   |  1   | 0.00193 |
|  67  |                     Attend Part Time Meetings                      |   task   |   1   |  1   | 0.00193 |
|  68  |         Increase Counsellors Experience [with Technology]          | softgoal |   -1  |  1   |  0.0018 |
|  69  |    !Increased Emphasis on IT in Hiring Process [of Counsellors]    | softgoal |   1   |  1   |  0.0018 |
|  70  |                          Call Statistics                           | resource |   -1  |  1   | 0.00159 |
+------+--------------------------------------------------------------------+----------+-------+------+---------+
```

### Time Taken : 13.4992139339
