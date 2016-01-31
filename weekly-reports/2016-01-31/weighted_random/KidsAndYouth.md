## Kids and Youth
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,    100.0  ,   2.86 (               |             *),97.14, 97.14, 100.00, 100.00, 100.00
   1 ,     gen20_f1 ,    100.0  ,    0.0 (              -|-------------*),97.14, 100.00, 100.00, 100.00, 100.00
   1 ,     gen40_f1 ,    100.0  ,    0.0 (              -|-------------*),97.14, 100.00, 100.00, 100.00, 100.00
   1 ,     gen60_f1 ,    100.0  ,    0.0 (              -|-------------*),97.14, 100.00, 100.00, 100.00, 100.00
   1 ,     gen80_f1 ,    100.0  ,    0.0 (               |             *),100.00, 100.00, 100.00, 100.00, 100.00
   1 ,    gen100_f1 ,    100.0  ,    0.0 (               |             *),100.00, 100.00, 100.00, 100.00, 100.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,    100.0  ,    0.0 (---------------|-------------*),80.00, 100.00, 100.00, 100.00, 100.00
   1 ,     gen20_f2 ,    100.0  ,    0.0 (               |             *),100.00, 100.00, 100.00, 100.00, 100.00
   1 ,     gen40_f2 ,    100.0  ,    0.0 (               |             *),100.00, 100.00, 100.00, 100.00, 100.00
   1 ,     gen60_f2 ,    100.0  ,    0.0 (               |             *),100.00, 100.00, 100.00, 100.00, 100.00
   1 ,     gen80_f2 ,    100.0  ,    0.0 (               |             *),100.00, 100.00, 100.00, 100.00, 100.00
   1 ,    gen100_f2 ,    100.0  ,    0.0 (               |             *),100.00, 100.00, 100.00, 100.00, 100.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f3 ,    30.74  ,   1.96 (    ---------- | *-----       ),26.60, 29.90, 31.10, 31.38, 33.03
   2 ,     gen60_f3 ,    31.28  ,    1.6 (            ---|  *-----      ),29.40, 30.69, 31.28, 31.60, 33.38
   2 ,     gen20_f3 ,    31.28  ,    2.1 (            -- |  *----       ),29.30, 30.08, 31.30, 31.69, 33.14
   2 ,     gen40_f3 ,    31.28  ,   1.98 (            ---|  *----       ),29.40, 30.24, 31.38, 31.72, 33.18
   2 ,     gen80_f3 ,    31.34  ,    1.6 (            ---|  *-----      ),29.40, 30.69, 31.40, 31.60, 33.38
   2 ,    gen100_f3 ,    31.34  ,   1.42 (            ---|- *-----      ),29.50, 31.04, 31.40, 31.60, 33.38

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,     gen80_f4 ,      8.0  ,    3.0 (---*-          |              ), 4.00,  7.00,  8.00,  9.00, 10.00
   1 ,    gen100_f4 ,      8.0  ,    3.0 (---*-          |              ), 4.00,  7.00,  8.00,  9.00, 10.00
   2 ,     gen40_f4 ,      9.0  ,    4.0 ( -- * -        |              ), 5.00,  8.00,  9.00, 11.00, 13.00
   2 ,     gen60_f4 ,      9.0  ,    2.0 (--- *--        |              ), 4.00,  7.00,  9.00,  9.00, 12.00
   3 ,     gen20_f4 ,     13.0  ,    8.0 (   -    *  --- |              ), 8.00,  9.00, 14.00, 17.00, 21.00
   4 ,      gen0_f4 ,     24.0  ,    9.0 (           ----| *  ----      ),17.00, 23.00, 25.00, 29.00, 34.00
```

### Time Taken : 13.0320980549
![1](../../../src/img/weighted_random/Kids and Youth.png)

### Decisions Ranked
```
+------+-------------------------------------------+------+-------+------+
| rank |                    name                   | type | value | cost |
+------+-------------------------------------------+------+-------+------+
|  1   |     Maintain Ask a Counsellor Section     | task |   -1  |  2   |
|  2   |        Implement Video Counselling        | task |   -1  |  5   |
|  3   |         !Implement Text Messaging         | task |   -1  |  5   |
|  4   | Maintain Get Informed Section of Web Site | task |   -1  |  5   |
|  5   |      !Implement One-On-One Chat Rooms     | task |   -1  |  4   |
|  6   |           Contact CS in Crisis            | task |   -1  |  4   |
|  7   |        Implement Email Counselling        | task |   -1  |  5   |
|  8   |              Provide Feedback             | task |   -1  |  3   |
|  9   |   !Implement Cyber Café/Portal/Chat Room  | task |   -1  |  3   |
|  10  |  !Implement General Questions and Answers | task |   -1  |  4   |
|  11  |        !Implement Polls about Kids        | task |   1   |  1   |
|  12  |   !Implement Bulletin Board with Replies  | task |   1   |  1   |
|  13  |   Contact CS about Non-Crisis Situation   | task |   -1  |  3   |
|  14  |         Maintain Phone Counselling        | task |   -1  |  3   |
|  15  |        Implement Voice Counselling        | task |   -1  |  2   |
+------+-------------------------------------------+------+-------+------+
```

### Top 4 Decisions from above table.
```
+-------------------------------------------+----------+-------+
|                    name                   |   type   | value |
+-------------------------------------------+----------+-------+
|            *Get Effective Help            | softgoal |  0.5  |
|              Help be acquired             |   goal   |   1   |
|              Services Be Free             |   goal   |   1   |
|        Implement Voice Counselling        |   task   |   -1  |
|         Maintain Phone Counselling        |   task   |   -1  |
|          *Safety of service usage         | softgoal |  0.5  |
|        Implement Video Counselling        |   task   |   -1  |
|        Implement Email Counselling        |   task   |   1   |
|          High Quality [Service]           | softgoal |   1   |
|     Maintain Ask a Counsellor Section     |   task   |   -1  |
|        Ownership of Service [Kids]        | softgoal |   1   |
|        Easy [Access to Post Reply]        | softgoal |   1   |
|               Vent Emotions               | softgoal |  0.5  |
|   !Implement Cyber Café/Portal/Chat Room  |   task   |   1   |
|                  *Privacy                 | softgoal |  0.5  |
|            Patient [Counselor]            | softgoal |   1   |
|   Contact CS about Non-Crisis Situation   |   task   |   1   |
|        Confidentiality [Services]         | softgoal |   1   |
|           Read Polls about Kids           |   task   |   -1  |
|       Decrease [Phone Waiting Time]       | softgoal |   1   |
|         Confidentiality [Service]         | softgoal |   1   |
|         !Implement Text Messaging         |   task   |   -1  |
|             Use Text Messaging            |   task   |   -1  |
|  Children Decide When to Hang Up and Call | softgoal |   1   |
| Maintain Get Informed Section of Web Site |   task   |   -1  |
|           Use voice Counselling           |   task   |   -1  |
|           Friendly [Web site] 1           | softgoal |   1   |
|          High Quality [Services]          | softgoal |   1   |
|          Availability [Service]           | softgoal |   1   |
|      Connect Back to the Community 1      | softgoal |   1   |
|            Anonymity [Service]            | softgoal |   1   |
|            Immediacy [Service]            | softgoal |   1   |
|        !Implement Polls about Kids        |   task   |   -1  |
|   Similarity with other kids  problems    | softgoal |   1   |
|   !Implement Bulletin Board with Replies  |   task   |   -1  |
|  Support and Be Supported By Other Kids   | softgoal |  0.5  |
|     Read General Questions and Answers    |   task   |   -1  |
|   Similarity with other kids  problems 1  | softgoal |   1   |
|       Ownership of Services [Kids]        | softgoal |   1   |
|          Availability [Services]          | softgoal |   1   |
|      Decrease [Phone Waiting Time] 1      | softgoal |   1   |
|      Use Cyber Café/Portal/Chat Room      |   task   |   1   |
|  !Implement General Questions and Answers |   task   |   -1  |
|     Information be acquired on website    |   goal   |   -1  |
|      !Implement One-On-One Chat Rooms     |   task   |   -1  |
|              Provide Feedback             |   task   |   1   |
|        Use Ask a Counsellor Section       |   task   |   -1  |
|           Anonymity [Services]            | softgoal |   1   |
|             Services Be Free1             |   goal   |   1   |
|           Contact CS in Crisis            |   task   |   -1  |
|          Effective Help in Crisis         | softgoal |  0.5  |
|   Effective Help in Non Crisis Situation  | softgoal |  0.5  |
|       Connect Back to the Community       | softgoal |   1   |
|         Use One-On-One Chat Rooms         |   task   |   -1  |
|         Connect with Other Kids 1         | softgoal |   1   |
|            Friendly [Web site]            | softgoal |   1   |
|           Immediacy [Services]            | softgoal |   1   |
|           Patient [Counselor] 1           | softgoal |   1   |
|       Easy [Access to Post Reply] 1       | softgoal |   1   |
|      Be informed of service anonymity     |   goal   |   1   |
|       Comfortableness with service        | softgoal |  0.5  |
|          Connect with Other Kids          | softgoal |   1   |
|   Read Get Informed Section of Web Site   |   task   |   -1  |
+-------------------------------------------+----------+-------+
```
