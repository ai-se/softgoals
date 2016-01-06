## CSFDandMarketingSD
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,    96.67  ,    0.0 (*--------------|------------- ),96.67, 96.67, 96.67, 96.67, 100.00
   1 ,     gen20_f1 ,    96.67  ,   3.33 (*              |              ),96.67, 96.67, 96.67, 100.00, 100.00
   1 ,     gen40_f1 ,    96.67  ,   3.33 (*              |              ),96.67, 96.67, 96.67, 100.00, 100.00
   2 ,     gen60_f1 ,    100.0  ,   3.33 (               |             *),96.67, 96.67, 100.00, 100.00, 100.00
   2 ,     gen80_f1 ,    100.0  ,   3.33 (               |             *),96.67, 96.67, 100.00, 100.00, 100.00
   2 ,    gen100_f1 ,    100.0  ,   3.33 (               |             *),96.67, 96.67, 100.00, 100.00, 100.00

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
   1 ,    gen100_f3 ,      3.0  ,    2.0 ( ---*          |              ), 1.00,  3.00,  3.00,  4.00,  4.00
   2 ,     gen80_f3 ,      5.0  ,    1.0 (    -  *       |              ), 3.00,  4.00,  5.00,  5.00,  6.00
   3 ,     gen60_f3 ,      7.0  ,    2.0 (        -* -   |              ), 6.00,  7.00,  7.00,  8.00,  9.00
   4 ,     gen40_f3 ,      9.0  ,    3.0 (         ---  *|-             ), 7.00,  9.00, 10.00, 10.00, 12.00
   5 ,     gen20_f3 ,     12.0  ,    3.0 (              -| * --         ),10.00, 11.00, 12.00, 14.00, 15.00
   6 ,      gen0_f3 ,     15.0  ,    2.0 (               |---  *-----   ),11.00, 14.00, 15.00, 16.00, 19.00
```

### Time Taken : 7.69220614433
![1](../../../src/img/optimals/CSFDandMarketingSD.png)
```
+------+----------------------------------------------+----------+-------+------+
| rank |                     name                     |   type   | value | cost |
+------+----------------------------------------------+----------+-------+------+
|  1   |           National Event Calendar            | resource |   -1  |  1   |
|  2   |               Manage Accounts                |   task   |   -1  |  1   |
|  3   |               Provide receipts               |   task   |   -1  |  1   |
|  4   |           Philanthropic donations            |   task   |   -1  |  1   |
|  5   |             Manage Receivables               |   task   |   -1  |  1   |
|  6   |                Provide funds                 |   task   |   -1  |  1   |
|  7   |    Single charitable registration number     | resource |   1   |  1   |
|  8   |             ! Market CS Service              |   task   |   -1  |  1   |
|  9   |                Pledge online                 |   task   |   -1  |  1   |
|  10  |                 Sponsor Logo                 | resource |   -1  |  1   |
|  11  |              Free advertisement              | resource |   -1  |  1   |
|  12  |            Provide free services             |   task   |   -1  |  1   |
|  13  |        ! Provide compiled call data          |   task   |   -1  |  1   |
|  14  |       Provide Document Library System        |   task   |   -1  |  1   |
|  15  |        Use sponsor marketing channels        |   task   |   -1  |  1   |
|  16  |           Create General Ledgers             |   task   |   -1  |  1   |
|  17  |         Manage\nPartner Relationship         |   task   |   -1  |  1   |
|  18  |                    Funds                     | resource |   -1  |  1   |
|  19  |         ! Provide money for services         |   task   |   -1  |  1   |
|  20  |             Pledge\nDuring event             |   task   |   -1  |  1   |
|  21  |       Provide Online Donor Technology        |   task   |   -1  |  1   |
|  22  |                  Agreement                   | resource |   -1  |  1   |
|  23  |         Provide fundraising services         |   task   |   -1  |  1   |
|  24  |         Provide fundraising services         |   task   |   -1  |  1   |
|  25  | ! Counselor Speak on Kids Issues in General  |   task   |   -1  |  1   |
|  26  |  Get Corporate Partner Information from DL   |   task   |   1   |  1   |
|  27  |            Participate in events             |   task   |   -1  |  1   |
|  28  |           Get sponsors for events            |   task   |   -1  |  1   |
|  29  |            Collect Pledge online             |   task   |   -1  |  1   |
|  30  |             Sponsorship proposal             |   task   |   -1  |  1   |
|  31  |        ! Write Articles for Website          |   task   |   -1  |  1   |
|  32  |       ! Write Articles for Magazines         |   task   |   -1  |  1   |
+------+----------------------------------------------+----------+-------+------+
```

### Top 26 Decisions from above table.
```
+----------------------------------------------------------------+----------+-------+
|                              name                              |   type   | value |
+----------------------------------------------------------------+----------+-------+
|                      ! Market CS Service                       |   task   |   -1  |
|          Exclusive Relationships [Official Partners]           | softgoal |   1   |
|            Up to date corporate partner information            | softgoal |   1   |
|                Provide Online Donor Technology                 |   task   |   -1  |
|                      Pledge\nDuring event                      |   task   |   -1  |
|                   Accountability of services                   | softgoal |   1   |
|                Recognize\nSponsor contribution                 | softgoal |   1   |
|                ! Write Articles for Magazines                  |   task   |   1   |
|                  Exclusive Brand and Logo use                  | softgoal |   1   |
|               High Response [Individual Donors]                | softgoal |   1   |
|             Single charitable registration number              | resource |   1   |
|                    National Event Calendar                     | resource |   -1  |
|                      Quality [Services]                        | softgoal |   1   |
|                  *Engage employees in events                   | softgoal |   1   |
|                           CS Stories                           | softgoal |   1   |
|                        Provide receipts                        |   task   |   -1  |
|                     Collect Pledge online                      |   task   |   -1  |
|                       Free advertisement                       | resource |   -1  |
|                      Published CS Stories                      | softgoal |   1   |
| Increase Access Speed [  Regional Offices to Document Library] | softgoal |   1   |
|                   Engage Employees in events                   | softgoal |   1   |
|                             Funds                              | resource |   -1  |
|                  Regional Staff feel included                  | softgoal |   1   |
|                      Sponsorship proposal                      |   task   |   -1  |
|               Follow Highest Ethical Guidelines                | softgoal |   1   |
|                !Acquire public speaking skills                 | softgoal |   1   |
|                    Create General Ledgers                      |   task   |   -1  |
|                  Regional\nContact management                  | softgoal |   1   |
|                  Regional\nContact management                  | softgoal |   1   |
|                          Sponsor Logo                          | resource |   -1  |
|                 ! Provide compiled call data                   |   task   |   -1  |
|                 Use sponsor marketing channels                 |   task   |   -1  |
|           Get Corporate Partner Information from DL            |   task   |   1   |
|                      Manage Receivables                        |   task   |   -1  |
|                     Demonstrable Services                      | softgoal |   1   |
|                  Provide fundraising services                  |   task   |   -1  |
|                Provide Document Library System                 |   task   |   -1  |
|                  ! Provide money for services                  |   task   |   -1  |
|                        Manage Accounts                         |   task   |   -1  |
|          ! Counselor Speak on Kids Issues in General           |   task   |   -1  |
|                      [Increase] Awareness                      | softgoal |   1   |
|                         Provide funds                          |   task   |   -1  |
|                      Promotion Resources                       | softgoal |   1   |
|                     Provide free services                      |   task   |   -1  |
|                Experienced [marketing partners]                | softgoal |   1   |
|                    Credibility [CS Brand]                      | softgoal |   1   |
|                    Get sponsors for events                     |   task   |   1   |
|         ! Services be provided for Kids Bullying Line          |   goal   |   1   |
|                         Pledge online                          |   task   |   -1  |
|                       Retain [Sponsors]                        | softgoal |   1   |
|                      Presentation Skills                       | softgoal |   1   |
|                    Philanthropic donations                     |   task   |   -1  |
|                  Manage\nPartner Relationship                  |   task   |   -1  |
|                 ! Write Articles for Website                   |   task   |   1   |
|                        Timely services                         | softgoal |   1   |
|             Up to Date [Information on programs]               | softgoal |   1   |
|                   Sponsor partner\ncontacts                    | softgoal |   1   |
|                           Agreement                            | resource |   -1  |
|                   Project Management Skills                    | softgoal |   1   |
|                 Quick [Response to Sponsors]                   | softgoal |   1   |
|               Responsible Usage [Sponsor Funds]                | softgoal |   1   |
|                     Participate in events                      |   task   |   -1  |
+----------------------------------------------------------------+----------+-------+
```
