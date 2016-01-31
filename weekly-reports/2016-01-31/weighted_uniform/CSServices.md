## CSServices
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,    51.08  ,    8.6 (    ---   *  --|-             ),41.94, 46.24, 51.08, 54.30, 61.29
   2 ,     gen20_f1 ,    61.83  ,   9.68 (          -----|  * ---       ),50.54, 58.06, 62.37, 65.59, 69.35
   2 ,     gen40_f1 ,    63.44  ,   6.45 (             --|-  *------    ),55.38, 61.29, 63.44, 65.59, 73.66
   3 ,     gen60_f1 ,    65.05  ,   6.99 (               |--  * -----   ),59.14, 62.37, 65.05, 68.82, 75.81
   3 ,     gen80_f1 ,    65.59  ,   6.98 (               |--- * -----   ),59.14, 63.44, 65.59, 68.82, 75.81
   3 ,    gen100_f1 ,    65.59  ,   7.53 (               |--- *  ----   ),59.14, 63.44, 66.13, 69.35, 75.81

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,    69.57  ,  30.43 (--           * |  -------     ),43.48, 47.83, 69.57, 78.26, 91.30
   2 ,     gen20_f2 ,    86.96  ,  17.39 (               |----   *   -- ),73.91, 82.61, 86.96, 95.65, 100.00
   3 ,     gen40_f2 ,     91.3  ,   8.69 (               |  -----    *- ),78.26, 86.96, 95.65, 95.65, 100.00
   3 ,     gen60_f2 ,    95.65  ,   8.69 (               |  -----    *- ),78.26, 86.96, 95.65, 95.65, 100.00
   3 ,     gen80_f2 ,    95.65  ,  13.04 (               |  -----    *  ),78.26, 86.96, 95.65, 100.00, 100.00
   3 ,    gen100_f2 ,    95.65  ,  13.04 (               |    ---    *  ),82.61, 86.96, 95.65, 100.00, 100.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f3 ,    169.98  ,  90.04 ( ---     * --  |              ),80.76, 116.26, 171.95, 186.52, 215.74
   2 ,     gen20_f3 ,    215.74  ,  58.62 (         ---  *|--            ),172.51, 201.76, 223.97, 246.51, 271.70
   2 ,     gen40_f3 ,    230.92  ,  50.28 (           --  * ---          ),189.11, 214.85, 232.64, 254.12, 285.92
   3 ,     gen60_f3 ,    238.72  ,  59.83 (            -- *  ---         ),203.65, 227.45, 239.67, 268.21, 295.58
   3 ,     gen80_f3 ,    238.72  ,  48.41 (            ---*  ---         ),205.36, 229.33, 239.67, 268.21, 295.58
   3 ,    gen100_f3 ,    239.67  ,  50.82 (            ---|* ---         ),206.94, 229.33, 242.23, 268.64, 299.31

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f4 ,     24.0  ,    5.0 (    ---- *  ---|-             ),20.00, 23.00, 24.00, 26.00, 29.00
   2 ,     gen20_f4 ,     27.0  ,    5.0 (        ---    *  ----        ),23.00, 25.00, 28.00, 30.00, 33.00
   2 ,     gen40_f4 ,     28.0  ,    6.0 (        ----   *  -------     ),23.00, 26.00, 28.00, 30.00, 35.00
   2 ,     gen60_f4 ,     28.0  ,    5.0 (        ----   | * -----      ),23.00, 26.00, 29.00, 31.00, 34.00
   2 ,     gen80_f4 ,     28.0  ,    5.0 (         ---   | * ------     ),24.00, 26.00, 29.00, 31.00, 35.00
   2 ,    gen100_f4 ,     28.0  ,    5.0 (         ----- | * -----      ),24.00, 27.00, 29.00, 31.00, 34.00
```

### Time Taken : 275.130558968
![1](../../../src/img/weighted_uniform/CSServices.png)

### Decisions Ranked
```
+------+------------------------------------------------------------+----------+-------+------+
| rank |                            name                            |   type   | value | cost |
+------+------------------------------------------------------------+----------+-------+------+
|  1   |                     Service Resources                      | resource |   1   |  1   |
|  2   |           Kids Use Ask a Counsellor Section\ns1            |   task   |   1   |  1   |
|  3   |                  Create Counselling Posts                  |   task   |   1   |  1   |
|  4   |                      Implement Delay                       |   task   |   1   |  1   |
|  5   |                Kids Use Phone Counselling1                 |   task   |   1   |  1   |
|  6   |                    Strategic Blue Print                    | resource |   1   |  1   |
|  7   |               Voice Counselling be Performed               |   task   |   1   |  1   |
|  8   |                !Moderate Discussion Boards                 |   task   |   1   |  1   |
|  9   |              Parents Use Information Section1              |   task   |   1   |  1   |
|  10  |             Provide Web Counselling with Video             |   task   |   1   |  1   |
|  11  |                      !Moderate a Chat                      |   task   |   1   |  1   |
|  12  |                Provide Written Counselling                 |   task   |   1   |  1   |
|  13  |               *Maintain PHL Phone Services4                |   task   |   1   |  1   |
|  14  |           Implement Bulletin Board with Replies1           |   task   |   1   |  1   |
|  15  |             Provide Web Counselling with Audio             |   task   |   -1  |  1   |
|  16  |                     Implement Filters                      |   task   |   1   |  1   |
|  17  |                         Web Server                         | resource |   1   |  1   |
|  18  |              Schedule Chat at Specific Times               |   task   |   -1  |  1   |
|  19  |           Kids Use Bulletin Board with Replies1            |   task   |   1   |  1   |
|  20  |             Maintain Ask a Counsellor Section1             |   task   |   1   |  1   |
|  21  |             !Implement One-On-One Chat Rooms1              |   task   |   1   |  1   |
|  22  |  !Implement\nTool to Allow Parents to Talk to Each Other   |   task   |   1   |  1   |
|  23  |      Kids Use Bulletin Board with Delayed Moderation1      |   task   |   -1  |  1   |
|  24  |                 *Provide Recorded Messages                 |   task   |   1   |  1   |
|  25  |               Implement Information Section                |   task   |   1   |  1   |
|  26  |         Kids use get Informed Section of Web Site          |   task   |   1   |  1   |
|  27  |                        Web Software                        | resource |   -1  |  1   |
|  28  |           Kids Use Cyber Café/Portal/Chat Room1            |   task   |   1   |  1   |
|  29  |                Kids Use Video Counselling1                 |   task   |   1   |  1   |
|  30  |          Parents Use Bulletin Board with Replies1          |   task   |   -1  |  1   |
|  31  |     Implement Bulletin Board with Delayed Moderation1      |   task   |   -1  |  1   |
|  32  |                        Trace Calls                         |   task   |   1   |  1   |
|  33  |                 !Perform Email Counselling                 |   task   |   1   |  1   |
|  34  |                Kids Use Email Counselling1                 |   task   |   1   |  1   |
|  35  |       Block Kids who Display Inappropriate Behavoir        |   task   |   -1  |  1   |
|  36  |                   Feedback Form Software                   | resource |   1   |  1   |
|  37  |              Implement Anti-Pranking Message               |   task   |   1   |  1   |
|  38  |          Kids Read General Questions and Answers1          |   task   |   1   |  1   |
|  39  |                 !Implement Text Messaging1                 |   task   |   -1  |  1   |
|  40  |                !Kids Read Polls about Kids1                |   task   |   1   |  1   |
|  41  | Parents Use\nTool to Allow Parents to Talk to Each Other 1 |   task   |   -1  |  1   |
|  42  |                 !Implement Phone Feedback3                 |   task   |   1   |  1   |
|  43  |    Inform Kids about Anonymity [Kids] of Web Services1     |   task   |   1   |  1   |
|  44  |                 Put Content Onto Website1                  |   task   |   1   |  1   |
|  45  |                      Web Site Content                      | resource |   1   |  1   |
|  46  |                          Feedback                          | resource |   1   |  1   |
|  47  |                Implement Board with Replies                |   task   |   1   |  1   |
|  48  |                         Feedback1                          | resource |   1   |  1   |
|  49  |                Implement Voice Counselling1                |   task   |   1   |  1   |
|  50  |                Kids Use Voice Counselling1                 |   task   |   1   |  1   |
+------+------------------------------------------------------------+----------+-------+------+
```

### Top 21 Decisions from above table.
```
+---------------------------------------------------------------+----------+-------+
|                              name                             |   type   | value |
+---------------------------------------------------------------+----------+-------+
|    Answer 80% of Calls within 30 Seconds of Message Ending    |   goal   |   1   |
|                    Implement Feedback Form                    |   task   |   1   |
|                    Decrease Response TIme1                    | softgoal |  -0.5 |
|                    *Increased Web Services3                   | softgoal |  -0.5 |
|                    Increase Web Resources2                    | softgoal |   1   |
|               !Implement One-On-One Chat Rooms1               |   task   |   1   |
|            Kids Read General Questions and Answers            |   task   |   -1  |
|                       Friendly Web Site1                      | softgoal |  0.5  |
|                   Kids Use Voice Counselling                  |   task   |   -1  |
|              Kids Use Ask a Counsellor Section\ns             |   task   |   1   |
|                    Confidentiality [Kids]6                    | softgoal |  0.5  |
|                 Kids Use One-On-One Chat Rooms                |   task   |   1   |
|                 Connect Back to the Community5                | softgoal |  0.5  |
|             Kids Use Cyber Café/Portal/Chat Room1             |   task   |   -1  |
|                      Strategic Blue Print                     | resource |   1   |
|                   !Implement Phone Feedback                   |   task   |   -1  |
|                    Similarity of Problems1                    | softgoal |  0.5  |
|                           Immediacy2                          | softgoal |  0.5  |
|                 Maintain/Implement CS Services                |   task   |   1   |
|                   Accommodate Phone Traffic                   | softgoal |  0.5  |
|            Similarity with other parents  problems            | softgoal |  -0.5 |
|                   !Implement Text Messaging                   |   task   |   1   |
|                 *Anonymous Technology Be Used                 |   goal   |   1   |
|               Maintain Ask a Counsellor Section1              |   task   |   1   |
|                  Accommodate Web Site Traffic                 | softgoal |  -0.5 |
|                 *Maintain PHL Phone Services4                 |   task   |   1   |
|                Kids Have Ownership of Services1               | softgoal |   1   |
|                     Services Be Bilingual1                    |   goal   |   1   |
|                  !Moderate Discussion Boards                  |   task   |   1   |
|              Easier Navigation [CS Web Services]1             | softgoal |  0.5  |
|               *Sufficient Counselling Resources1              | softgoal |   1   |
|                  Measure Success of Services4                 | softgoal |  0.5  |
|                       Anonymity [Kids]3                       | softgoal |   -1  |
|                    *High Quality Services2                    | softgoal |  0.5  |
|         Easier to Find Posts [Web Posting Technology]1        | softgoal |  0.5  |
|              Kids Use Cyber Café/Portal/Chat Room             |   task   |   -1  |
|                   !Implement Phone Feedback3                  |   task   |   -1  |
|                      Quality [Services]                       | softgoal |  0.5  |
|                  Kids Use Phone Counselling1                  |   task   |   1   |
|                    Web Services Self Serve1                   | softgoal |  -0.5 |
|                   *Efficient Phone Services                   | softgoal |  0.5  |
|             Counsellors Be Professionally Trained             |   goal   |   1   |
|                        Web Site Content                       | resource |   1   |
|                 Connect Back to the Community8                | softgoal |  0.5  |
|               Provide Web Counselling with Video              |   task   |   1   |
|              Non-Real Time E-Counselling Be Used              |   goal   |   1   |
|                  Control of Counselling Work1                 | softgoal |  -0.5 |
|                    *Increased Web Services4                   | softgoal |  -0.5 |
|                    Decrease Response TIme2                    | softgoal |  -0.5 |
|           Implement Get Informed Section of Web Site          |   task   |   -1  |
|                    Increase Web Resources1                    | softgoal |   1   |
|                 Connect Back to the Community1                | softgoal |  0.5  |
|    Encourage Kids Using Web Services to Use Phone Services1   | softgoal |  0.5  |
|                     Decrease Response TIme                    | softgoal |  -0.5 |
|   Parents Use\nTool to Allow Parents to Talk to Each Other    |   task   |   -1  |
|             Implement Bulletin Board with Replies             |   task   |   1   |
|               Provide Web Counselling with Audio              |   task   |   -1  |
|                      Anonymity [Parents]4                     | softgoal |   1   |
|                     Services Be Bilingual                     |   goal   |   1   |
|                    Confidentiality [Kids]1                    | softgoal |   1   |
|                 Connect Back to the Community6                | softgoal |  0.5  |
|                       Avoid Bad Advice2                       | softgoal |  -0.5 |
|                    *Obtain Needed Software                    |   task   |   1   |
|                  Effective Chat Room Filters                  | softgoal |   1   |
|                    Web Services Self Serve                    | softgoal |  -0.5 |
|                     Available [Services] 2                    | softgoal |  -0.5 |
|                Non-Anonymous Technology Be Used               |   goal   |   1   |
|                Kids Have Ownership of Services5               | softgoal |   1   |
|                  *Maintain PHL Web Services2                  |   task   |   1   |
|                       Anonymity [Kids]6                       | softgoal |  0.5  |
|                    Improve Website Content1                   | softgoal |  0.5  |
|         ! Services be provided for Kids Bullying Line         |   goal   |   1   |
|                Confidential Technology Be Used                |   goal   |   1   |
|                   *Efficient Phone Services1                  | softgoal |  0.5  |
|                        Acquire Feedback                       |   task   |   -1  |
|                   Kids Use Video Counselling                  |   task   |   -1  |
|                           Immediacy7                          | softgoal |  -0.5 |
|                      Reduce Prank Calls1                      | softgoal |  -0.5 |
|                       Anonymity [Kids]5                       | softgoal |   1   |
|               *Sufficient Counselling Resources2              | softgoal |   1   |
|                    Control [Web Services]2                    | softgoal |  0.5  |
|                  Kids Use Email Counselling1                  |   task   |   1   |
|               Maintain Ask a Counsellor Section               |   task   |   1   |
|                    *Maintain Phone Services                   |   task   |   1   |
| Technology that Does Not Allow Dialogues Between Kids Be Used |   goal   |   1   |
|                  Confidentiality [Services]                   | softgoal |   -1  |
|                  Implement Email Counselling1                 |   task   |   -1  |
|         ! Services be provided for Kids Bullying Line1        |   goal   |   1   |
|                  Implement Voice Counselling                  |   task   |   -1  |
|                        Implement Delay                        |   task   |   1   |
|           Kids Read Get Informed Section of Web Site          |   task   |   -1  |
|                Implement Anti-Pranking Message                |   task   |   -1  |
|    Encourage Kids Using Web Services to Use Phone Services    | softgoal |  0.5  |
|                     Feedback Form Software                    | resource |   1   |
|                Schedule Chat at Specific Times                |   task   |   -1  |
|                   Increase Phone Resources2                   | softgoal |   1   |
|                !Implement One-On-One Chat Rooms               |   task   |   1   |
|                      Efficient Services1                      | softgoal |  0.5  |
|        Kids Use Bulletin Board with Delayed Moderation        |   task   |   -1  |
|                      Friendly [Web site]                      | softgoal |  -0.5 |
|                   Confidentiality [Parents]5                  | softgoal |  0.5  |
|                    Confidentiality [Kids]5                    | softgoal |   1   |
|                     Available [Services] 1                    | softgoal |  -0.5 |
|            Kids Read General Questions and Answers1           |   task   |   -1  |
|                    Relevance in Kids Lives                    | softgoal |  0.5  |
|              Maintain Services above Competition              | softgoal |  0.5  |
|                   Acquire Service Resources                   |   task   |   1   |
|          Only Online Request from Canadians Accepted          |   goal   |   1   |
|                    Anonymity [Counsellors]                    | softgoal |  0.5  |
|                 Connect Back to the Community2                | softgoal |  0.5  |
|                     Connect to Other Kids                     | softgoal |   1   |
|                           Immediacy3                          | softgoal |  -0.5 |
|                    Direct Response to Kids1                   | softgoal |  0.5  |
|                  Maintain CS Phone Services1                  |   task   |   1   |
|                     Available [Services]                      | softgoal |  -0.5 |
|                    Put Content Onto Website                   |   task   |   -1  |
|                     Control [Web Services]                    | softgoal |  0.5  |
|             Implement Bulletin Board with Replies1            |   task   |   1   |
|                    Improve Website Content                    | softgoal |  0.5  |
|              Non-Confidential Technology Be Used              |   goal   |   1   |
|                   *Efficient Phone Services2                  | softgoal |  0.5  |
|                  *Maintain PHL Web Services1                  |   task   |   1   |
|                 Decrease [Phone Waiting Time]                 | softgoal |  0.5  |
|                    Improve Website Content2                   | softgoal |  0.5  |
|                    *High Quality Services1                    | softgoal |  0.5  |
|      Inform Kids about Anonymity [Kids] of Web Services1      |   task   |   -1  |
|                       Anonymity [Kids]2                       | softgoal |   -1  |
|                  Maintain CS Phone Services2                  |   task   |   1   |
|                    Direct Response to Kids                    | softgoal |  0.5  |
|                           Immediacy4                          | softgoal |  -0.5 |
|              Sufficiently Moderated Web Services1             | softgoal |  0.5  |
|               *Sufficient Counselling Resources               | softgoal |   1   |
|                Kids Have Ownership of Services6               | softgoal |   1   |
|    !Implement\nTool to Allow Parents to Talk to Each Other    |   task   |   1   |
|          *Kids Get Information through E-Counselling          |   task   |   1   |
|                 Connect Back to the Community                 | softgoal |  0.5  |
|                   Confidentiality [Parents]1                  | softgoal |   -1  |
|                      Anonymity [Parents]2                     | softgoal |   -1  |
|                     Efficient Web Services                    | softgoal |  -0.5 |
|                Maintain/Implement CS Services2                |   task   |   1   |
|                  !Kids Read Polls about Kids                  |   task   |   -1  |
|                   Kids Use Phone Counselling                  |   task   |   1   |
|                 Voice Counselling be Performed                |   task   |   1   |
|                        Confidentiality                        | softgoal |  -0.5 |
|                  Maintain CS Phone Services3                  |   task   |   1   |
|                     Maintain Web Services                     |   task   |   1   |
|                    Decrease Response TIme3                    | softgoal |   1   |
|           Kids use get Informed Section of Web Site           |   task   |   1   |
|                    Decrease Response TIme4                    | softgoal |   1   |
|                 Avoid Dialogues [Between Kids]                | softgoal |   -1  |
|            Parents Use Bulletin Board with Replies            |   task   |   1   |
|                      Anonymity [Parents]5                     | softgoal |   -1  |
|              Kids Use Online Information Provided             |   goal   |   1   |
|                   !Perform Email Counselling                  |   task   |   -1  |
|                 Connect Back to the Community7                | softgoal |  0.5  |
|                       Avoid Bad Advice3                       | softgoal |  0.5  |
|                     Similarity of Problems                    | softgoal |  0.5  |
|       Implement Bulletin Board with Delayed Moderation1       |   task   |   -1  |
|                     Available [Services] 5                    | softgoal |  -0.5 |
|           Increase Emphasis on Online Feedback Form1          | softgoal |   1   |
|                  Control of Counselling Work                  | softgoal |  -0.5 |
|                        Avoid Bad Advice                       | softgoal |  -0.5 |
|                Kids Have Ownership of Services4               | softgoal |   1   |
|                  Measure Success of Services1                 | softgoal |  0.5  |
|         Reduce Contagion Effect [Of Harmful Actions]1         | softgoal |  0.5  |
|                       Anonymity [Kids]1                       | softgoal |   -1  |
|                     Improve Image to Kids1                    | softgoal |  0.5  |
|                  Avoid Presence of Pedofiles                  | softgoal |  0.5  |
|                   Confidentiality [Parents]                   | softgoal |   -1  |
|                  Measure Success of Services                  | softgoal |  -0.5 |
|           Similarity with other parents  problems 1           | softgoal |  -0.5 |
|                       Avoid Bad Advice4                       | softgoal |  -0.5 |
|                 Increase Resources [Services]1                | softgoal |   1   |
|                    Control [Web Services]1                    | softgoal |  0.5  |
|                           Web Server                          | resource |   1   |
|                    Anonymity [Counsellors]1                   | softgoal |  0.5  |
|         Block Kids who Display Inappropriate Behavoir         |   task   |   -1  |
|        Reduce Number of Steps [Web Posting Technology]1       | softgoal |  -0.5 |
|                       Friendly Web Site                       | softgoal |  0.5  |
|                     Increase Web Resources                    | softgoal |  0.5  |
|                   Increase Phone Resources1                   | softgoal |   1   |
|                            Feedback                           | resource |   -1  |
|                     *High Quality Services                    | softgoal |  0.5  |
|                    *Increased Web Services1                   | softgoal |  -0.5 |
|                 Implement Information Section                 |   task   |   1   |
|              Sufficiently Moderated Web Services              | softgoal |  0.5  |
|     Technology that Allows Dialogues Between Kids Be Used     |   goal   |   1   |
|          Strategic Blue Print for Website Be Followed         |   goal   |   1   |
|   Avoid Dialogues Between [Kids and Counsellors on the Web]   | softgoal |  0.5  |
|                     Friendly [Web site] 1                     | softgoal |  -0.5 |
|                   Confidentiality [Parents]4                  | softgoal |   -1  |
|                     Improve Image to Kids                     | softgoal |  0.5  |
|                 *Increase Number of Services1                 | softgoal |  -0.5 |
|                    Confidentiality [Kids]4                    | softgoal |   1   |
|          Reduce Contagion Effect [Of Harmful Actions]         | softgoal |  0.5  |
|                   Confidentiality [Parents]2                  | softgoal |   -1  |
|                Kids Have Ownership of Services                | softgoal |  0.5  |
|               Web Site Content Be Updated Daily               |   goal   |   1   |
|                  Implement Voice Counselling1                 |   task   |   -1  |
|                 Connect Back to the Community3                | softgoal |  0.5  |
|                  !Kids Read Polls about Kids1                 |   task   |   1   |
|               Empowering Kids to Help Themselves              | softgoal |  0.5  |
|                           Feedback1                           | resource |   -1  |
|                    Direct Response to Kids2                   | softgoal |  0.5  |
|                    Confidentiality [Kids]3                    | softgoal |   1   |
|                        Anonymity [Kids]                       | softgoal |   -1  |
|                 Increase Resources [Services]                 | softgoal |  0.5  |
|                       Reduce Prank Calls                      | softgoal |   1   |
|                   *Maintain PHL Web Services                  |   task   |   1   |
|               Correct Interpretation of Counsel               | softgoal |  -0.5 |
|                 *Maintain PHL Phone Services2                 |   task   |   1   |
|                Kids Have Ownership of Services3               | softgoal |   1   |
|                       Anonymity [Kids]4                       | softgoal |   -1  |
|                  Measure Success of Services2                 | softgoal |  -0.5 |
|                  Easier Access to Post Reply                  | softgoal |  0.5  |
|                 Connect Back to the Community9                | softgoal |  0.5  |
|                Real Time E-Counselling Be Used                |   goal   |   1   |
|              Easier Navigation [CS Web Services]2             | softgoal |  0.5  |
|              Easier Navigation [CS Web Services]              | softgoal |  0.5  |
|                           Immediacy5                          | softgoal |  -0.5 |
|                          Web Software                         | resource |   1   |
|              Sufficiently Moderated Web Services2             | softgoal |  0.5  |
|                  Easier Access to Post Reply1                 | softgoal |  0.5  |
|                      Anonymity [Parents]1                     | softgoal |   -1  |
|                Parents Use Information Section1               |   task   |   1   |
|                    Relevance in Kids Lives1                   | softgoal |   1   |
|                  Avoid Presence of Pedofiles1                 | softgoal |   1   |
|                    Web Services Self Serve3                   | softgoal |   1   |
|                    Increase Phone Resources                   | softgoal |   1   |
|                Maintain/Implement CS Services1                |   task   |   1   |
|             Counsellors Be Professionally Trained1            |   goal   |   1   |
|                          Trace Calls                          |   task   |   1   |
|                    *Increased Web Services2                   | softgoal |  -0.5 |
|                    Efficient Web Services2                    | softgoal |  -0.5 |
|           Increase Emphasis on Online Feedback Form           | softgoal |   1   |
|                  Provide Written Counselling                  |   task   |   1   |
|                 Connect Back to the Community                 | softgoal |  0.5  |
|                   *Provide Recorded Messages                  |   task   |   1   |
|                   Put Content Onto Website1                   |   task   |   -1  |
|                    Confidentiality [Kids]7                    | softgoal |   1   |
|                  Kids Use Video Counselling1                  |   task   |   -1  |
|                           Immediacy8                          | softgoal |  -0.5 |
|                  *Increase Number of Services                 | softgoal |  -0.5 |
|                 Connect Back to the Community4                | softgoal |  0.5  |
|                     Confidentiality [Kids]                    | softgoal |   1   |
|                     Available [Services] 4                    | softgoal |  -0.5 |
|                  !Implement Polls about Kids                  |   task   |   -1  |
|                    *Increased Web Services                    | softgoal |  -0.5 |
|              Maintain Services above Competition1             | softgoal |  0.5  |
|                    Kids Use Text Messaging                    |   task   |   1   |
|                 Parents Use Phone Counselling1                |   task   |   1   |
|              Kids Use Bulletin Board with Replies             |   task   |   1   |
|                           Immediacy1                          | softgoal |  -0.5 |
|                       Avoid Bad Advice5                       | softgoal |  -0.5 |
|                  Implement Board with Replies                 |   task   |   1   |
|                   !Implement Text Messaging1                  |   task   |   1   |
|                  Kids Use Voice Counselling1                  |   task   |   1   |
|        Reduce Number of Steps [Web Posting Technology]        | softgoal |  -0.5 |
|                      Anonymity [Parents]                      | softgoal |   -1  |
|                Parents Use Information Section                |   task   |   1   |
|              Empowering Kids to Help Themselves1              | softgoal |  0.5  |
|                       Service Resources                       | resource |   1   |
|             Telephony Be Implemented and Managed1             |   goal   |   1   |
|                       Implement Filters                       |   task   |   1   |
|                Moderated E-Counselling Be Used                |   goal   |   1   |
|                   Kids Use Email Counselling                  |   task   |   -1  |
|                    Relevance in Kids Lives2                   | softgoal |   1   |
|                     Immediacy [Services]                      | softgoal |  -0.5 |
|                      Anonymity [Parents]3                     | softgoal |  0.5  |
|                        !Moderate a Chat                       |   task   |   1   |
|                           Anonymity                           | softgoal |  -0.5 |
|                     Available [Services] 3                    | softgoal |   1   |
|                Connect Back to the Community10                | softgoal |  0.5  |
|                  Easy [Access to Post Reply]                  | softgoal |  -0.5 |
|                        Avoid Dialogues                        | softgoal |   -1  |
|                    Create Counselling Posts                   |   task   |   1   |
|                    Efficient Web Services1                    | softgoal |  -0.5 |
|   Parents Use\nTool to Allow Parents to Talk to Each Other 1  |   task   |   -1  |
|                  Decrease Phone Waiting Time                  | softgoal |  0.5  |
|              Telephony Be Implemented and Managed             |   goal   |   1   |
|                    Availability [Services]                    | softgoal |  -0.5 |
|         Easier to Find Posts [Web Posting Technology]         | softgoal |  0.5  |
|                    Confidentiality [Kids]2                    | softgoal |   1   |
|                       Avoid Bad Advice1                       | softgoal |  -0.5 |
|                Kids Have Ownership of Services2               | softgoal |   1   |
|                       Anonymity [Kids]7                       | softgoal |   -1  |
|               Correct Interpretation of Counsel1              | softgoal |   1   |
|                  Decrease Phone Waiting Time1                 | softgoal |  0.5  |
|                     Service Levels Be Met                     |   goal   |   1   |
|                  Measure Success of Services3                 | softgoal |  0.5  |
|             Kids Use Ask a Counsellor Section\ns1             |   task   |   1   |
|                           Immediacy                           | softgoal |  -0.5 |
|                           Immediacy6                          | softgoal |  -0.5 |
|              Sufficiently Moderated Web Services3             | softgoal |  0.5  |
|            Parents Use Bulletin Board with Replies1           |   task   |   1   |
|        Kids Use Bulletin Board with Delayed Moderation1       |   task   |   -1  |
|                    Web Services Self Serve2                   | softgoal |  -0.5 |
|                   Confidentiality [Parents]3                  | softgoal |   -1  |
|                  Avoid Presence of Pedofiles2                 | softgoal |   1   |
|                 Easy [Access to Post Reply] 1                 | softgoal |  -0.5 |
|             Kids Use Bulletin Board with Replies1             |   task   |   1   |
|              Sufficiently Moderated Web Services4             | softgoal |  0.5  |
|                       Efficient Services                      | softgoal |  0.5  |
+---------------------------------------------------------------+----------+-------+
```
