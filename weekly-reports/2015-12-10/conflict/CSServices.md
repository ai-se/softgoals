## CSServices
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,    53.23  ,   8.07 (      -----  * |-----         ),45.70, 51.08, 53.23, 55.91, 60.75
   1 ,     gen20_f1 ,    53.76  ,   7.52 (       ----   *|  ---         ),46.24, 51.08, 53.76, 58.06, 61.29
   1 ,     gen40_f1 ,    55.91  ,    8.6 (        ----   | * ----       ),47.31, 52.15, 56.45, 58.60, 63.44
   2 ,     gen60_f1 ,    56.99  ,   9.14 (        -----  | *  ----      ),47.85, 53.23, 56.99, 60.22, 63.98
   2 ,     gen80_f1 ,    58.06  ,   6.99 (        ------ |  * -----     ),47.85, 54.30, 58.06, 60.22, 65.59
   2 ,    gen100_f1 ,    58.06  ,    8.6 (          -----|   * ------   ),49.46, 54.84, 58.60, 61.29, 67.74

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,    78.26  ,  13.04 (  -----------  |  * ---       ),47.83, 69.57, 78.26, 82.61, 86.96
   1 ,     gen20_f2 ,    78.26  ,    8.7 (    -----------|--* ---       ),52.17, 78.26, 78.26, 82.61, 86.96
   2 ,     gen40_f2 ,    78.26  ,    8.7 (           ----|--  *----     ),65.22, 78.26, 82.61, 82.61, 91.30
   2 ,     gen60_f2 ,    82.61  ,    8.7 (             --|--  *  --     ),69.57, 78.26, 82.61, 86.96, 91.30
   2 ,     gen80_f2 ,    82.61  ,    8.7 (             --|--  *  ----   ),69.57, 78.26, 82.61, 86.96, 95.65
   2 ,    gen100_f2 ,    82.61  ,  13.04 (             --|--  *  ----   ),69.57, 78.26, 82.61, 86.96, 95.65

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,     gen80_f3 ,    101.0  ,   18.0 (     ----    * | ------       ),88.00, 96.00, 102.00, 111.00, 121.00
   1 ,    gen100_f3 ,    101.0  ,   16.0 (     ----    * | ------       ),88.00, 96.00, 102.00, 110.00, 121.00
   1 ,     gen60_f3 ,    102.0  ,   17.0 (     -----   * | ------       ),88.00, 97.00, 103.00, 111.00, 121.00
   1 ,     gen40_f3 ,    104.0  ,   16.0 (      -----    *  -----       ),90.00, 99.00, 107.00, 112.00, 122.00
   2 ,     gen20_f3 ,    107.0  ,   19.0 (       -----   |*   ----      ),92.00, 101.00, 108.00, 116.00, 124.00
   2 ,      gen0_f3 ,    109.0  ,   20.0 (       ------  | *   ----     ),92.00, 102.00, 110.00, 117.00, 125.00
```
### Time Taken : 250.293451071
![1](../../../src/img/conflict/CSServices.png)
```

+------+------------------------------------------------------------+----------+-------+------+
| rank |                            name                            |   type   | value | cost |
+------+------------------------------------------------------------+----------+-------+------+
|  1   |                Kids Use Phone Counselling1                 |   task   |   1   |  3   |
|  2   |                    Strategic Blue Print                    | resource |   1   |  2   |
|  3   |                  Create Counselling Posts                  |   task   |   1   |  2   |
|  4   |           Kids Use Ask a Counsellor Section\ns1            |   task   |   1   |  1   |
|  5   |          Parents Use Bulletin Board with Replies1          |   task   |   -1  |  5   |
|  6   |                     Anonymity [Kids]3                      | softgoal |   -1  |  5   |
|  7   |                !Moderate Discussion Boards                 |   task   |   1   |  4   |
|  8   |                !Kids Read Polls about Kids1                |   task   |   1   |  2   |
|  9   |                         Immediacy6                         | softgoal |   1   |  1   |
|  10  |                  Confidentiality [Kids]1                   | softgoal |   1   |  5   |
|  11  |                Avoid Presence of Pedofiles                 | softgoal |   -1  |  5   |
|  12  |        Reduce Contagion Effect [Of Harmful Actions]        | softgoal |   -1  |  5   |
|  13  |                     Service Resources                      | resource |   1   |  1   |
|  14  |                         Immediacy7                         | softgoal |   1   |  5   |
|  15  |    Inform Kids about Anonymity [Kids] of Web Services1     |   task   |   1   |  2   |
|  16  | Avoid Dialogues Between [Kids and Counsellors on the Web]  | softgoal |   -1  |  4   |
|  17  |              Implement Anti-Pranking Message               |   task   |   -1  |  3   |
|  18  |                  Anonymity [Counsellors]                   | softgoal |   1   |  3   |
|  19  |           Kids Use Bulletin Board with Replies1            |   task   |   1   |  5   |
|  20  |                      Implement Delay                       |   task   |   1   |  2   |
|  21  |                        Trace Calls                         |   task   |   -1  |  1   |
|  22  |                   Control [Web Services]                   | softgoal |   1   |  2   |
|  23  |               Voice Counselling be Performed               |   task   |   1   |  4   |
|  24  |                   Decrease Response TIme                   | softgoal |   -1  |  3   |
|  25  |          Kids Read General Questions and Answers1          |   task   |   -1  |  2   |
|  26  |                Implement Board with Replies                |   task   |   -1  |  2   |
|  27  |             Maintain Ask a Counsellor Section1             |   task   |   1   |  2   |
|  28  | Parents Use\nTool to Allow Parents to Talk to Each Other 1 |   task   |   1   |  5   |
|  29  |              Schedule Chat at Specific Times               |   task   |   -1  |  1   |
|  30  |                    Reduce Prank Calls1                     | softgoal |   1   |  4   |
|  31  |                         Anonymity                          | softgoal |   1   |  3   |
|  32  |           Implement Bulletin Board with Replies1           |   task   |   1   |  5   |
|  33  |                Kids Use Email Counselling1                 |   task   |   -1  |  3   |
|  34  |                      !Moderate a Chat                      |   task   |   1   |  5   |
|  35  |  !Implement\nTool to Allow Parents to Talk to Each Other   |   task   |   -1  |  1   |
|  36  |                          Feedback                          | resource |   -1  |  5   |
|  37  |               Implement Information Section                |   task   |   -1  |  5   |
|  38  |                     Implement Filters                      |   task   |   1   |  3   |
|  39  |                Provide Written Counselling                 |   task   |   1   |  5   |
|  40  |                   Similarity of Problems                   | softgoal |   -1  |  1   |
|  41  |                        Web Software                        | resource |   -1  |  4   |
|  42  |                         Web Server                         | resource |   -1  |  3   |
|  43  |                      Web Site Content                      | resource |   1   |  2   |
|  44  |             Correct Interpretation of Counsel              | softgoal |   -1  |  4   |
|  45  |                         Feedback1                          | resource |   -1  |  3   |
|  46  |                Implement Voice Counselling1                |   task   |   1   |  2   |
|  47  |                 !Implement Phone Feedback3                 |   task   |   1   |  3   |
|  48  |             Provide Web Counselling with Video             |   task   |   -1  |  3   |
|  49  |                   Feedback Form Software                   | resource |   1   |  3   |
|  50  |         Kids use get Informed Section of Web Site          |   task   |   -1  |  2   |
|  51  |               *Maintain PHL Phone Services4                |   task   |   -1  |  5   |
|  52  |                      Avoid Bad Advice                      | softgoal |   -1  |  3   |
|  53  |                 !Perform Email Counselling                 |   task   |   1   |  4   |
|  54  |       Block Kids who Display Inappropriate Behavoir        |   task   |   -1  |  3   |
|  55  |                 !Implement Text Messaging1                 |   task   |   -1  |  1   |
|  56  |       Easier to Find Posts [Web Posting Technology]        | softgoal |   1   |  2   |
|  57  |             !Implement One-On-One Chat Rooms1              |   task   |   1   |  3   |
|  58  |               Avoid Dialogues [Between Kids]               | softgoal |   -1  |  3   |
|  59  |                      Confidentiality                       | softgoal |   -1  |  2   |
|  60  |                 *Provide Recorded Messages                 |   task   |   -1  |  2   |
|  61  |                Kids Use Voice Counselling1                 |   task   |   1   |  1   |
|  62  |             Provide Web Counselling with Audio             |   task   |   -1  |  4   |
|  63  |              Parents Use Information Section1              |   task   |   -1  |  3   |
|  64  |                Kids Use Video Counselling1                 |   task   |   -1  |  5   |
|  65  |                  Direct Response to Kids                   | softgoal |   -1  |  5   |
|  66  |                 Put Content Onto Website1                  |   task   |   1   |  5   |
|  67  |      Kids Use Bulletin Board with Delayed Moderation1      |   task   |   -1  |  3   |
|  68  |           Kids Use Cyber Café/Portal/Chat Room1            |   task   |   -1  |  2   |
|  69  |      Reduce Number of Steps [Web Posting Technology]1      | softgoal |   -1  |  5   |
|  70  |     Implement Bulletin Board with Delayed Moderation1      |   task   |   1   |  3   |
+------+------------------------------------------------------------+----------+-------+------+
```
