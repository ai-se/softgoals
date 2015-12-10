## CSSimplified
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,    98.69  ,    0.0 (*--------------|------------- ),98.69, 98.69, 98.69, 98.69, 100.00
   1 ,     gen20_f1 ,    98.69  ,    0.0 (*--------------|------------- ),98.69, 98.69, 98.69, 98.69, 100.00
   1 ,     gen40_f1 ,    98.69  ,    0.0 (*--------------|------------- ),98.69, 98.69, 98.69, 98.69, 100.00
   1 ,     gen60_f1 ,    98.69  ,   1.31 (*              |              ),98.69, 98.69, 98.69, 100.00, 100.00
   1 ,     gen80_f1 ,    98.69  ,   1.31 (*              |              ),98.69, 98.69, 98.69, 100.00, 100.00
   1 ,    gen100_f1 ,    98.69  ,   1.31 (*              |              ),98.69, 98.69, 98.69, 100.00, 100.00

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
   1 ,    gen100_f3 ,    180.0  ,   16.0 (     --- *---- |              ),165.00, 176.00, 181.00, 184.00, 197.00
   2 ,     gen80_f3 ,    185.0  ,   20.0 (     ----  * --|              ),166.00, 180.00, 187.00, 195.00, 199.00
   2 ,     gen60_f3 ,    189.0  ,   16.0 (      ----  * -|              ),169.00, 182.00, 189.00, 198.00, 204.00
   3 ,     gen40_f3 ,    191.0  ,   15.0 (      -----  * |--            ),169.00, 187.00, 193.00, 200.00, 210.00
   3 ,     gen20_f3 ,    197.0  ,   19.0 (        ----  *| ----         ),177.00, 189.00, 198.00, 206.00, 219.00
   3 ,      gen0_f3 ,    199.0  ,   25.0 (        ----   |*  ------     ),177.00, 190.00, 202.00, 214.00, 234.00
```
### Time Taken : 105.251405001
![1](../../../src/img/conflict/CSSimplified.png)
```

+------+----------------------------------------------------------+----------+-------+------+
| rank |                           name                           |   type   | value | cost |
+------+----------------------------------------------------------+----------+-------+------+
|  1   |             Provide Document Library System              |   task   |   1   |  1   |
|  2   |            Maintain Ask a Counsellor Section             |   task   |   1   |  1   |
|  3   |                Kids Use Email Counselling                |   task   |   -1  |  4   |
|  4   |           Kids Use Cyber Café/Portal/Chat Room           |   task   |   -1  |  5   |
|  5   |                          Funds                           | resource |   -1  |  4   |
|  6   |             Parents Use Information Section              |   task   |   -1  |  4   |
|  7   |                 *Maintain Phone Services                 |   task   |   -1  |  2   |
|  8   |                      Free Hardware                       | resource |   -1  |  4   |
|  9   |                Kids Use Video Counselling                |   task   |   -1  |  1   |
|  10  |            Provide Web Counselling with Audio            |   task   |   1   |  3   |
|  11  |               Write Articles for Newspaper               |   task   |   1   |  1   |
|  12  |          !Implement Cyber Café/Portal/Chat Room          |   task   |   -1  |  4   |
|  13  |               Implement Voice Counselling                |   task   |   1   |  2   |
|  14  |              Maintain/Implement CS Services              |   task   |   1   |  2   |
|  15  |              Elaborate Fundraising targets               |   task   |   1   |  2   |
|  16  |              ! Provide compiled call data                |   task   |   1   |  1   |
|  17  |             Historical Data of Call Volumes              | resource |   -1  |  3   |
|  18  |                        Agreement                         | resource |   -1  |  4   |
|  19  |            Phone Library of Recorded Messages            | resource |   -1  |  3   |
|  20  |                     Double Head Set                      | resource |   -1  |  1   |
|  21  |                   Manage Receivables                     |   task   |   -1  |  4   |
|  22  |              ! Write Articles for Website                |   task   |   1   |  1   |
|  23  |              Voice Counselling be Performed              |   task   |   1   |  1   |
|  24  |        Get Corporate Partner Information from DL         |   task   |   1   |  1   |
|  25  |                  Provide free services                   |   task   |   1   |  2   |
|  26  |                  Collect Pledge online                   |   task   |   1   |  1   |
|  27  |              Use sponsor marketing channels              |   task   |   -1  |  3   |
|  28  |                       Web Server1                        | resource |   -1  |  5   |
|  29  |                   Provide Information                    |   task   |   -1  |  4   |
|  30  |                          Tapes                           | resource |   1   |  2   |
|  31  |               Find Help with Presentations               |   task   |   1   |  3   |
|  32  |                 Undergo Clinical Review                  |   task   |   1   |  2   |
|  33  |                       Information                        | resource |   -1  |  5   |
|  34  |         Kids read General Questions and Answers          |   task   |   -1  |  3   |
|  35  |         Plan and Put on Reconnection Conferences         |   task   |   -1  |  3   |
|  36  |                         Software                         | resource |   -1  |  5   |
|  37  |             Maintain/ Implement PHL Services             |   task   |   1   |  1   |
|  38  |       ! Counselor Speak on Kids Issues in General        |   task   |   1   |  2   |
|  39  |           Kids Use Ask a Counsellor Section\ns           |   task   |   -1  |  1   |
|  40  |              Parents Use Phone Counselling               |   task   |   -1  |  3   |
|  41  |                     Provide receipts                     |   task   |   -1  |  5   |
|  42  |                Kids Use Phone Counselling                |   task   |   -1  |  3   |
|  43  |               Manage\nPartner Relationship               |   task   |   -1  |  4   |
|  44  |               Second Reading of Web Posts                |   task   |   -1  |  4   |
|  45  |                       Sponsor Logo                       | resource |   -1  |  1   |
|  46  |                        Web Server                        | resource |   1   |  1   |
|  47  |                Donor/Accounting Data Base                | resource |   -1  |  5   |
|  48  |                   Pledge\nDuring event                   |   task   |   1   |  3   |
|  49  |          Inform kids about anonymity of service          |   task   |   -1  |  3   |
|  50  |               Implement Board with Replies               |   task   |   -1  |  5   |
|  51  |                     Send out Emails                      |   task   |   -1  |  4   |
|  52  |              *Implement Categorization Tool              |   task   |   1   |  3   |
|  53  |           Kids Use Bulletin Board with Replies           |   task   |   -1  |  4   |
|  54  |         !Implement General Questions and Answers         |   task   |   1   |  2   |
|  55  |               Implement Email Counselling                |   task   |   -1  |  4   |
|  56  |        Maintain Get Informed Section of Web Site         |   task   |   -1  |  5   |
|  57  |                 Philanthropic donations                  |   task   |   1   |  2   |
|  58  |                     Call Statistics                      | resource |   -1  |  2   |
|  59  |             ! Write Articles for Magazines               |   task   |   -1  |  4   |
|  60  |                  Give CS Presentations                   |   task   |   -1  |  1   |
|  61  |                   Counselling Policies                   | resource |   1   |  3   |
|  62  |                 Create General Ledgers                   |   task   |   1   |  1   |
|  63  |                !Implement Phone Feedback                 |   task   |   -1  |  2   |
|  64  |      Help Plan and Put on Reconnection Conferences       |   task   |   -1  |  3   |
|  65  |                         Speaches                         | resource |   -1  |  4   |
|  66  |       !Parents Use Service to Talk to Each Other         |   task   |   -1  |  2   |
|  67  |                   Promotion Resources                    | resource |   1   |  2   |
|  68  |                  Counselling Workshops                   | resource |   1   |  2   |
|  69  |                  Participate in events                   |   task   |   1   |  1   |
|  70  |              Share PAP in Document Library               |   task   |   1   |  2   |
|  71  |                         Hardware                         | resource |   -1  |  5   |
|  72  |                   Speak at Fundraisers                   |   task   |   -1  |  2   |
|  73  |                       IT Resources                       | resource |   1   |  2   |
|  74  |                        Promote CS                        |   task   |   -1  |  3   |
|  75  |                         Feedback                         | resource |   1   |  2   |
|  76  |                          Oracle                          | resource |   1   |  1   |
|  77  |          Single charitable registration number           | resource |   1   |  3   |
|  78  |                   Strategic Blue Print                   | resource |   -1  |  4   |
|  79  |                 Help with Presentations                  |   task   |   1   |  1   |
|  80  |                  Speak at Fundraisers1                   |   task   |   -1  |  5   |
|  81  |                       Web Software                       | resource |   -1  |  1   |
|  82  |                     Web Site Content                     | resource |   -1  |  4   |
|  83  |               Implement Video Counselling                |   task   |   -1  |  3   |
|  84  |                  Feedback Form Software                  | resource |   1   |  2   |
|  85  |                  Counsellor Experience                   | resource |   1   |  4   |
|  86  |             Provide Online Donor Technology              |   task   |   1   |  2   |
|  87  |                Maintain Phone Counselling                |   task   |   -1  |  4   |
|  88  |                  Give CS Presentations1                  |   task   |   -1  |  3   |
|  89  |           Help Put on SA Training Conferences            |   task   |   1   |  3   |
|  90  |                     Free Web Server                      | resource |   1   |  2   |
|  91  |                     !Moderate a Chat                     |   task   |   -1  |  2   |
|  92  |               !Moderate Discussion Boards                |   task   |   -1  |  5   |
|  93  |               *Maintain PHL Phone Services               |   task   |   -1  |  5   |
|  94  |         Parents Use Bulletin Board with Replies          |   task   |   -1  |  5   |
|  95  |                    Caller Statistics                     | resource |   -1  |  4   |
|  96  |               Diffuse Conflict with Parent               |   task   |   -1  |  3   |
|  97  |                *Implement Bulletin Board                 |   task   |   -1  |  3   |
|  98  | !Implement\nTool to Allow Parents to Talk to Each Other  |   task   |   1   |  1   |
|  99  |                        Feedback1                         | resource |   -1  |  4   |
| 100  |                         Upgrades                         | resource |   -1  |  3   |
| 101  |                   ! Market CS Service                    |   task   |   -1  |  3   |
| 102  |                  Web Moderator Meetings                  | resource |   -1  |  2   |
| 103  |                   Promotion Resources1                   | resource |   1   |  2   |
| 104  |                 Put Content Onto Website                 |   task   |   -1  |  3   |
| 105  |                    Service Resources                     | resource |   -1  |  3   |
| 106  |                 Get web event technology                 |   task   |   1   |  1   |
| 107  |                Kids read Polls about Kids                |   task   |   1   |  1   |
| 108  |             Negotiate with Counsellors Union             |   task   |   -1  |  1   |
| 109  |               !Implement Polls about Kids                |   task   |   -1  |  5   |
| 110  |                !Implement Text Messaging                 |   task   |   1   |  1   |
| 111  |                    Free advertisement                    | resource |   -1  |  5   |
| 112  |               Provide fundraising services               |   task   |   1   |  5   |
| 113  |               ! Provide money for services               |   task   |   1   |  3   |
| 114  |                 Get sponsors for events                  |   task   |   -1  |  5   |
| 115  |          !Implement Bulletin Board with Replies          |   task   |   1   |  3   |
| 116  |                      Free Upgrades                       | resource |   1   |  2   |
| 117  |                      Sign Contract                       |   task   |   1   |  2   |
| 118  |              Put on SA Training Conferences              |   task   |   1   |  4   |
| 119  |                         *Salary                          | resource |   1   |  5   |
| 120  |                      Pledge online                       |   task   |   1   |  1   |
| 121  |                   Sponsorship proposal                   |   task   |   -1  |  3   |
| 122  |                 Kids Use Text Messaging                  |   task   |   -1  |  2   |
| 123  |             *Implement Email for Counsellors             |   task   |   -1  |  5   |
| 124  |                  Maintain Web Services                   |   task   |   1   |  2   |
| 125  |                     Manage Accounts                      |   task   |   -1  |  3   |
| 126  |                      Provide funds                       |   task   |   -1  |  5   |
| 127  |              Implement Information Section               |   task   |   1   |  1   |
| 128  |            Provide Web Counselling with Video            |   task   |   1   |  5   |
| 129  |                      Free Software                       | resource |   1   |  2   |
| 130  |                 Create Counselling Posts                 |   task   |   1   |  1   |
| 131  |                Kids Use Voice Counselling                |   task   |   1   |  3   |
| 132  |             !Implement One-On-One Chat Rooms             |   task   |   1   |  1   |
| 133  |                Run Fundraiser in Schools                 |   task   |   -1  |  5   |
| 134  |               Provide Written Counselling                |   task   |   1   |  3   |
| 135  |        Kids use get Informed Section of Web Site         |   task   |   1   |  3   |
| 136  |                Tape Recording Technology                 | resource |   -1  |  5   |
| 137  |              Kids Use One-On-One Chat Rooms              |   task   |   -1  |  5   |
| 138  |                   Provide Counselling                    |   task   |   -1  |  4   |
| 139  |                       Training CDs                       | resource |   1   |  2   |
| 140  |                !Perform Email Counselling                |   task   |   -1  |  4   |
| 141  |               School Initiates Presenation               |   task   |   -1  |  4   |
+------+----------------------------------------------------------+----------+-------+------+
```
