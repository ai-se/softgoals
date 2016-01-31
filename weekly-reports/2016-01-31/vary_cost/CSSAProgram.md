## CSSAProgram
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,    64.18  ,  17.91 (     ---      *|-----         ),47.76, 53.73, 64.18, 68.66, 79.10
   2 ,     gen20_f1 ,    85.07  ,  14.93 (               | ----    *  - ),71.64, 79.10, 86.57, 92.54, 95.52
   3 ,     gen40_f1 ,    88.06  ,   8.96 (               |    ----  * - ),77.61, 85.07, 89.55, 92.54, 95.52
   3 ,     gen60_f1 ,    89.55  ,   8.96 (               |     ---  *   ),79.10, 85.07, 89.55, 94.03, 95.52
   3 ,     gen80_f1 ,    89.55  ,  10.45 (               |     ---  *   ),79.10, 85.07, 89.55, 94.03, 95.52
   3 ,    gen100_f1 ,    89.55  ,  10.45 (               |     ---  * - ),79.10, 85.07, 89.55, 92.54, 95.52

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,     36.0  ,   11.0 (   ------ *    |---           ),26.00, 34.00, 36.00, 44.00, 48.00
   2 ,     gen20_f2 ,     50.0  ,   10.0 (              -|--   * ----   ),41.00, 46.00, 50.00, 53.00, 58.00
   2 ,     gen40_f2 ,     51.0  ,    7.0 (               |----   * ---  ),44.00, 49.00, 52.00, 55.00, 59.00
   2 ,     gen60_f2 ,     52.0  ,    6.0 (               |-----  * --   ),44.00, 50.00, 52.00, 55.00, 58.00
   2 ,     gen80_f2 ,     52.0  ,    6.0 (               |-----  * ---  ),44.00, 50.00, 52.00, 55.00, 59.00
   2 ,    gen100_f2 ,     52.0  ,    6.0 (               |-----  * ---  ),43.00, 50.00, 52.00, 55.00, 59.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,     gen80_f3 ,      8.0  ,    4.0 (  -  * -       |              ), 5.00,  6.00,  8.00, 10.00, 11.00
   1 ,    gen100_f3 ,      8.0  ,    3.0 ( --  *--       |              ), 4.00,  6.00,  8.00,  9.00, 11.00
   1 ,     gen60_f3 ,      9.0  ,    4.0 (  --  *--      |              ), 5.00,  7.00,  9.00, 10.00, 12.00
   2 ,     gen40_f3 ,     10.0  ,    4.0 (   --  *---    |              ), 6.00,  8.00, 10.00, 11.00, 13.00
   2 ,     gen20_f3 ,     11.0  ,    4.0 (   ---  *----  |              ), 6.00,  9.00, 11.00, 12.00, 15.00
   3 ,      gen0_f3 ,     14.0  ,    7.0 (    ----    * -|------        ), 7.00, 11.00, 14.00, 16.00, 23.00
```

### Time Taken : 26.553442955
![1](../../../src/img/vary_cost/CSSAProgram.png)

### Decisions Ranked
```
+------+-------------------------------+----------+-------+------+
| rank |              name             |   type   | value | cost |
+------+-------------------------------+----------+-------+------+
|  1   |       Plan Social Events      |   task   |   -1  |  5   |
|  2   |       Attend SA Meetings      |   task   |   -1  |  5   |
|  3   | School Initiates Presenation1 |   task   |   -1  |  5   |
|  4   |  Write Articles for Newspaper |   task   |   1   |  1   |
|  5   |        Send out Emails        |   task   |   1   |  1   |
|  6   |           Train SA s          |   task   |   1   |  1   |
|  7   |    Help with Presentations    |   task   |   1   |  3   |
|  8   |       Attend CS Meetings      |   task   |   1   |  2   |
|  9   |          Retrain SA s         |   task   |   1   |  2   |
|  10  |        Provide Speaches       |   task   |   -1  |  2   |
|  11  |   Run Fundraiser in Schools1  |   task   |   -1  |  2   |
|  12  |      Promotion Resources1     | resource |   1   |  1   |
+------+-------------------------------+----------+-------+------+
```

### Top 6 Decisions from above table.
```
+--------------------------------------------------------+----------+-------+
|                          name                          |   type   | value |
+--------------------------------------------------------+----------+-------+
|           Acquire Volunteer Outreach Skills1           | softgoal |  -0.5 |
|                 Experience for Resume                  | softgoal |  -0.5 |
|                 Improve Image to Kids1                 | softgoal |  0.5  |
|                  Speak at Fundraisers                  |   task   |   1   |
|            Acquire Public Speaking Skills1             | softgoal |  0.5  |
|                   Attend SA Meetings                   |   task   |   -1  |
|                 Increased SA Resources                 | softgoal |   1   |
|               Acquire Fundraising Skills               | softgoal |  -0.5 |
|              Increase Involvement of SA s              | softgoal |  -0.5 |
|                   Make New Friends1                    | softgoal |  -0.5 |
|           Community Service Hours Completed            |   goal   |   1   |
|                    Increase Skills                     | softgoal |  -0.5 |
|                    Trust [of Kids]                     | softgoal |  0.5  |
|                    Send out Emails1                    |   task   |   1   |
|          Help Put on SA Training Conferences           |   task   |   1   |
|             Write Articles for Newspaper2              |   task   |   1   |
|              Provide Promotion Resources               |   task   |   -1  |
|              Acquire Fundraising Skills2               | softgoal |  -0.5 |
|           Create Life Long Volunteer Spirit            | softgoal |  -0.5 |
|                  SA s are Organized1                   | softgoal |  -0.5 |
|               *Expansion of SA Services                | softgoal |  -0.5 |
|               Run Fundraiser in Schools                |   task   |   -1  |
|             School Initiates Presenation1              |   task   |   -1  |
|           Create Life Long Volunteer Spirit1           | softgoal |  -0.5 |
|                 Give CS Presentations1                 |   task   |   1   |
|                   Plan Social Events                   |   task   |   -1  |
|               Run Fundraiser in Schools2               |   task   |   -1  |
|                      Be Confident                      | softgoal |  -0.5 |
|                 Give CS Presentations                  |   task   |   1   |
|                Increased SA Resources1                 | softgoal |   1   |
|                   SA s are Outgoing1                   | softgoal |  0.5  |
|                   SA s are Organized                   | softgoal |  -0.5 |
|            Happiness [Student Ambassadors]             | softgoal |  -0.5 |
|             Keep in Touch with Volunteers              | softgoal |  0.5  |
|       Plan and Put on Reconnection Conferences1        |   task   |   -1  |
|                      Retrain SA s                      |   task   |   -1  |
|              Find Help with Presentations              |   task   |   1   |
|                    Be Enthusiastic                     | softgoal |  0.5  |
|                 Have Time for School2                  | softgoal |  -0.5 |
|             Put on SA Training Conferences             |   task   |   1   |
|                 Improve Image to Kids                  | softgoal |  0.5  |
|                Positive Reputation [CS]                | softgoal |   1   |
|                 Have Time for School1                  | softgoal |  -0.5 |
|            Put on SA Training Conferences1             |   task   |   1   |
|             Write Articles for Newspaper1              |   task   |   1   |
|                Help with Presentations1                |   task   |   1   |
|            Ask for Help with Presentations             |   task   |   1   |
|                   Spread Awareness1                    | softgoal |  0.5  |
|                    Send out Emails2                    |   task   |   1   |
|                    Trust [of Kids]1                    | softgoal |  0.5  |
|           Acquire Volunteer Outreach Skills            | softgoal |  -0.5 |
|       Plan and Put on Reconnection Conferences2        |   task   |   -1  |
|                   SA s are Outgoing                    | softgoal |  0.5  |
|            Happiness [Student Ambassadors]2            | softgoal |  -0.5 |
|                      Be Outgoing                       | softgoal |  0.5  |
|             Acquire Public Speaking Skills             | softgoal |  0.5  |
|           Community Service Hours Completed2           |   goal   |   1   |
|                  SA s are Confident1                   | softgoal |  -0.5 |
|                       Train SA s                       |   task   |   1   |
|         Permission for Presentations Be Given          |   goal   |   1   |
|           More Promotion Resources Available           | softgoal |  0.5  |
|                   SA s are Confident                   | softgoal |  -0.5 |
|                    Provide Speaches                    |   task   |   -1  |
|                  Have Time for School                  | softgoal |  -0.5 |
|                Give Back to Community2                 | softgoal |  -0.5 |
|               Run Fundraiser in Schools1               |   task   |   -1  |
|                *Increase Writing Skills                | softgoal |  0.5  |
|      Kids Be Used to Communicate with Other Kids       |   goal   |   1   |
|        Plan and Put on Reconnection Conferences        |   task   |   -1  |
|     Help Plan and Put on Reconnection Conferences1     |   task   |   -1  |
|               *Increase Writing Skills1                | softgoal |  0.5  |
|                 Speak at Fundraisers2                  |   task   |   1   |
|                Give Back to Community1                 | softgoal |  -0.5 |
|               *Increase Writing Skills2                | softgoal |  0.5  |
|                    Spread Awareness                    | softgoal |  0.5  |
|                    Send out Emails                     |   task   |   1   |
|                 Reduce Misconceptions                  | softgoal |  0.5  |
|          Help Put on SA Training Conferences1          |   task   |   1   |
|                Help with Presentations                 |   task   |   1   |
|                   Attend CS Meetings                   |   task   |   -1  |
|                      Be Organized                      | softgoal |  -0.5 |
|                    Make New Friends                    | softgoal |  -0.5 |
|                  Quality SA Services1                  | softgoal |  -0.5 |
| *Engagement Student Ambassadors in promoting awareness | softgoal |  0.5  |
|              Acquire Fundraising Skills1               | softgoal |  -0.5 |
|                 SA s are Enthusiastic1                 | softgoal |  0.5  |
|                  Promotion Resources1                  | resource |   -1  |
|            Put on SA Training Conferences2             |   task   |   1   |
|                Presenation Be Initiated                |   goal   |   1   |
|           Initiate Presentation With Schools           |   task   |   1   |
|                  Quality SA Services                   | softgoal |  -0.5 |
|              School Initiates Presenation              |   task   |   -1  |
|              Write Articles for Newspaper              |   task   |   1   |
|            Happiness [Student Ambassadors]1            | softgoal |  -0.5 |
|                   Engage Volunteers                    | softgoal |  -0.5 |
|                 Give Back to Community                 | softgoal |  -0.5 |
|           Acquire Volunteer Outreach Skills2           | softgoal |  -0.5 |
|                 Give CS Presentations2                 |   task   |   1   |
|              High Presentation Attendance              | softgoal |  0.5  |
|     Help Plan and Put on Reconnection Conferences      |   task   |   -1  |
|           Community Service Hours Completed1           |   goal   |   1   |
|            Acquire Public Speaking Skills2             | softgoal |  0.5  |
|               Positive Reputation [CS]1                | softgoal |   1   |
|             Find Help with Presentations1              |   task   |   1   |
|                   Make New Friends2                    | softgoal |  -0.5 |
|                 Reduce Misconceptions1                 | softgoal |  0.5  |
|                 SA s are Enthusiastic                  | softgoal |  -0.5 |
|                 Speak at Fundraisers1                  |   task   |   1   |
+--------------------------------------------------------+----------+-------+
```
