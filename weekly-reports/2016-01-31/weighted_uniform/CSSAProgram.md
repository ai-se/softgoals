## CSSAProgram
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,    59.02  ,  36.07 (    ---        *     ----     ),36.07, 44.26, 60.66, 75.41, 85.25
   2 ,     gen20_f1 ,    80.33  ,  13.11 (               | ----- *  -   ),67.21, 77.05, 80.33, 86.89, 90.16
   3 ,     gen40_f1 ,    83.61  ,   9.83 (               |   ----  * -- ),72.13, 80.33, 83.61, 90.16, 95.08
   3 ,     gen60_f1 ,    86.89  ,  11.47 (               |      --- * - ),77.05, 83.61, 86.89, 91.80, 95.08
   3 ,     gen80_f1 ,    86.89  ,  11.47 (               |    ----- * - ),73.77, 83.61, 86.89, 91.80, 95.08
   3 ,    gen100_f1 ,    86.89  ,   9.83 (               |       --  *- ),80.33, 83.61, 88.52, 91.80, 95.08

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,    100.0  ,    0.0 (*              |              ),100.00, 100.00, 100.00, 100.00, 100.00
   1 ,     gen20_f2 ,    100.0  ,    0.0 (*              |              ),100.00, 100.00, 100.00, 100.00, 100.00
   1 ,     gen40_f2 ,    100.0  ,    0.0 (*              |              ),100.00, 100.00, 100.00, 100.00, 100.00
   1 ,     gen60_f2 ,    100.0  ,    0.0 (*              |              ),100.00, 100.00, 100.00, 100.00, 100.00
   1 ,     gen80_f2 ,    100.0  ,    0.0 (*              |              ),100.00, 100.00, 100.00, 100.00, 100.00
   1 ,    gen100_f2 ,    100.0  ,    0.0 (*              |              ),100.00, 100.00, 100.00, 100.00, 100.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f3 ,    45.21  ,  22.59 (  ------     * | ----         ),24.15, 37.56, 46.87, 55.08, 63.94
   2 ,     gen20_f3 ,    61.18  ,  12.79 (              -|-   * ---     ),48.58, 55.14, 61.47, 66.51, 72.68
   2 ,     gen80_f3 ,    63.07  ,  12.77 (               |--   * --     ),52.23, 57.61, 63.47, 68.24, 73.99
   2 ,     gen40_f3 ,    63.47  ,  10.63 (               |---  * --     ),52.21, 60.41, 63.56, 68.00, 73.68
   2 ,     gen60_f3 ,    63.47  ,  10.39 (               |---  * --     ),52.23, 60.27, 63.92, 67.99, 73.68
   2 ,    gen100_f3 ,    63.47  ,  11.94 (               |---  * ---    ),54.49, 59.11, 63.92, 69.46, 75.19

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,     gen40_f4 ,      5.0  ,    2.0 (  ---   *  --- |              ), 3.00,  4.00,  5.00,  6.00,  7.00
   1 ,     gen60_f4 ,      5.0  ,    2.0 (  ---   *--    |              ), 3.00,  4.00,  5.00,  5.00,  6.00
   1 ,     gen80_f4 ,      5.0  ,    1.0 (  ---   *--    |              ), 3.00,  4.00,  5.00,  5.00,  6.00
   1 ,    gen100_f4 ,      5.0  ,    1.0 (  ---   *--    |              ), 3.00,  4.00,  5.00,  5.00,  6.00
   2 ,      gen0_f4 ,      6.0  ,    3.0 (     ---   *---|----          ), 4.00,  5.00,  6.00,  6.00,  9.00
   2 ,     gen20_f4 ,      6.0  ,    2.0 (     ---   *---|-             ), 4.00,  5.00,  6.00,  6.00,  8.00
```

### Time Taken : 29.6304750443
![1](../../../src/img/weighted_uniform/CSSAProgram.png)

### Decisions Ranked
```
+------+-------------------------------+----------+-------+------+
| rank |              name             |   type   | value | cost |
+------+-------------------------------+----------+-------+------+
|  1   |       Attend CS Meetings      |   task   |   -1  |  1   |
|  2   |        Provide Speaches       |   task   |   -1  |  1   |
|  3   | School Initiates Presenation1 |   task   |   -1  |  1   |
|  4   |    Help with Presentations    |   task   |   1   |  1   |
|  5   |  Write Articles for Newspaper |   task   |   1   |  1   |
|  6   |       Attend SA Meetings      |   task   |   -1  |  1   |
|  7   |           Train SA s          |   task   |   1   |  1   |
|  8   |      Promotion Resources1     | resource |   -1  |  1   |
|  9   |   Run Fundraiser in Schools1  |   task   |   -1  |  1   |
|  10  |       Plan Social Events      |   task   |   -1  |  1   |
|  11  |        Send out Emails        |   task   |   -1  |  1   |
|  12  |          Retrain SA s         |   task   |   1   |  1   |
+------+-------------------------------+----------+-------+------+
```

### Top 6 Decisions from above table.
```
+--------------------------------------------------------+----------+-------+
|                          name                          |   type   | value |
+--------------------------------------------------------+----------+-------+
|           Acquire Volunteer Outreach Skills1           | softgoal |  0.5  |
|                 Experience for Resume                  | softgoal |  0.5  |
|                 Improve Image to Kids1                 | softgoal |  0.5  |
|                  Speak at Fundraisers                  |   task   |   -1  |
|            Acquire Public Speaking Skills1             | softgoal |  0.5  |
|                   Attend SA Meetings                   |   task   |   -1  |
|                 Increased SA Resources                 | softgoal |   1   |
|               Acquire Fundraising Skills               | softgoal |  -0.5 |
|              Increase Involvement of SA s              | softgoal |  0.5  |
|                   Make New Friends1                    | softgoal |  0.5  |
|           Community Service Hours Completed            |   goal   |   1   |
|                    Increase Skills                     | softgoal |  0.5  |
|                    Trust [of Kids]                     | softgoal |  0.5  |
|                    Send out Emails1                    |   task   |   -1  |
|          Help Put on SA Training Conferences           |   task   |   -1  |
|             Write Articles for Newspaper2              |   task   |   1   |
|              Provide Promotion Resources               |   task   |   1   |
|              Acquire Fundraising Skills2               | softgoal |  -0.5 |
|           Create Life Long Volunteer Spirit            | softgoal |  0.5  |
|                  SA s are Organized1                   | softgoal |  -0.5 |
|               *Expansion of SA Services                | softgoal |  0.5  |
|               Run Fundraiser in Schools                |   task   |   1   |
|             School Initiates Presenation1              |   task   |   -1  |
|           Create Life Long Volunteer Spirit1           | softgoal |  0.5  |
|                 Give CS Presentations1                 |   task   |   1   |
|                   Plan Social Events                   |   task   |   1   |
|               Run Fundraiser in Schools2               |   task   |   1   |
|                      Be Confident                      | softgoal |  0.5  |
|                 Give CS Presentations                  |   task   |   1   |
|                Increased SA Resources1                 | softgoal |   1   |
|                   SA s are Outgoing1                   | softgoal |  -0.5 |
|                   SA s are Organized                   | softgoal |  -0.5 |
|            Happiness [Student Ambassadors]             | softgoal |  0.5  |
|             Keep in Touch with Volunteers              | softgoal |  0.5  |
|       Plan and Put on Reconnection Conferences1        |   task   |   1   |
|                      Retrain SA s                      |   task   |   1   |
|              Find Help with Presentations              |   task   |   -1  |
|                    Be Enthusiastic                     | softgoal |  -0.5 |
|                 Have Time for School2                  | softgoal |  -0.5 |
|             Put on SA Training Conferences             |   task   |   -1  |
|                 Improve Image to Kids                  | softgoal |  0.5  |
|                Positive Reputation [CS]                | softgoal |   1   |
|                 Have Time for School1                  | softgoal |  -0.5 |
|            Put on SA Training Conferences1             |   task   |   -1  |
|             Write Articles for Newspaper1              |   task   |   1   |
|                Help with Presentations1                |   task   |   1   |
|            Ask for Help with Presentations             |   task   |   -1  |
|                   Spread Awareness1                    | softgoal |  0.5  |
|                    Send out Emails2                    |   task   |   -1  |
|                    Trust [of Kids]1                    | softgoal |  0.5  |
|           Acquire Volunteer Outreach Skills            | softgoal |  0.5  |
|       Plan and Put on Reconnection Conferences2        |   task   |   1   |
|                   SA s are Outgoing                    | softgoal |  -0.5 |
|            Happiness [Student Ambassadors]2            | softgoal |  0.5  |
|                      Be Outgoing                       | softgoal |  -0.5 |
|             Acquire Public Speaking Skills             | softgoal |  0.5  |
|           Community Service Hours Completed2           |   goal   |   1   |
|                  SA s are Confident1                   | softgoal |  0.5  |
|                       Train SA s                       |   task   |   -1  |
|         Permission for Presentations Be Given          |   goal   |   1   |
|           More Promotion Resources Available           | softgoal |  0.5  |
|                   SA s are Confident                   | softgoal |  0.5  |
|                    Provide Speaches                    |   task   |   -1  |
|                  Have Time for School                  | softgoal |  -0.5 |
|                Give Back to Community2                 | softgoal |  -0.5 |
|               Run Fundraiser in Schools1               |   task   |   1   |
|                *Increase Writing Skills                | softgoal |  0.5  |
|      Kids Be Used to Communicate with Other Kids       |   goal   |   1   |
|        Plan and Put on Reconnection Conferences        |   task   |   1   |
|     Help Plan and Put on Reconnection Conferences1     |   task   |   1   |
|               *Increase Writing Skills1                | softgoal |  0.5  |
|                 Speak at Fundraisers2                  |   task   |   -1  |
|                Give Back to Community1                 | softgoal |  -0.5 |
|               *Increase Writing Skills2                | softgoal |  0.5  |
|                    Spread Awareness                    | softgoal |  0.5  |
|                    Send out Emails                     |   task   |   -1  |
|                 Reduce Misconceptions                  | softgoal |  -0.5 |
|          Help Put on SA Training Conferences1          |   task   |   -1  |
|                Help with Presentations                 |   task   |   1   |
|                   Attend CS Meetings                   |   task   |   -1  |
|                      Be Organized                      | softgoal |  -0.5 |
|                    Make New Friends                    | softgoal |  -0.5 |
|                  Quality SA Services1                  | softgoal |  0.5  |
| *Engagement Student Ambassadors in promoting awareness | softgoal |  0.5  |
|              Acquire Fundraising Skills1               | softgoal |  -0.5 |
|                 SA s are Enthusiastic1                 | softgoal |  -0.5 |
|                  Promotion Resources1                  | resource |   1   |
|            Put on SA Training Conferences2             |   task   |   -1  |
|                Presenation Be Initiated                |   goal   |   1   |
|           Initiate Presentation With Schools           |   task   |   1   |
|                  Quality SA Services                   | softgoal |  0.5  |
|              School Initiates Presenation              |   task   |   -1  |
|              Write Articles for Newspaper              |   task   |   1   |
|            Happiness [Student Ambassadors]1            | softgoal |  0.5  |
|                   Engage Volunteers                    | softgoal |  0.5  |
|                 Give Back to Community                 | softgoal |  -0.5 |
|           Acquire Volunteer Outreach Skills2           | softgoal |  0.5  |
|                 Give CS Presentations2                 |   task   |   1   |
|              High Presentation Attendance              | softgoal |  0.5  |
|     Help Plan and Put on Reconnection Conferences      |   task   |   1   |
|           Community Service Hours Completed1           |   goal   |   1   |
|            Acquire Public Speaking Skills2             | softgoal |  0.5  |
|               Positive Reputation [CS]1                | softgoal |   1   |
|             Find Help with Presentations1              |   task   |   -1  |
|                   Make New Friends2                    | softgoal |  0.5  |
|                 Reduce Misconceptions1                 | softgoal |  -0.5 |
|                 SA s are Enthusiastic                  | softgoal |  -0.5 |
|                 Speak at Fundraisers1                  |   task   |   -1  |
+--------------------------------------------------------+----------+-------+
```
