## CSFDandMarketingSD
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,    96.77  ,    0.0 (*--------------|------------- ),96.77, 96.77, 96.77, 96.77, 100.00
   1 ,     gen20_f1 ,    96.77  ,    0.0 (*--------------|------------- ),96.77, 96.77, 96.77, 96.77, 100.00
   1 ,     gen40_f1 ,    96.77  ,    0.0 (*--------------|------------- ),96.77, 96.77, 96.77, 96.77, 100.00
   1 ,     gen60_f1 ,    96.77  ,    0.0 (*--------------|------------- ),96.77, 96.77, 96.77, 96.77, 100.00
   1 ,     gen80_f1 ,    96.77  ,    0.0 (*--------------|------------- ),96.77, 96.77, 96.77, 96.77, 100.00
   1 ,    gen100_f1 ,    96.77  ,    0.0 (*              |              ),96.77, 96.77, 96.77, 96.77, 96.77

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,     29.0  ,    0.0 (*              |              ),29.00, 29.00, 29.00, 29.00, 29.00
   1 ,     gen20_f2 ,     29.0  ,    0.0 (*              |              ),29.00, 29.00, 29.00, 29.00, 29.00
   1 ,     gen40_f2 ,     29.0  ,    0.0 (*              |              ),29.00, 29.00, 29.00, 29.00, 29.00
   1 ,     gen60_f2 ,     29.0  ,    0.0 (*              |              ),29.00, 29.00, 29.00, 29.00, 29.00
   1 ,     gen80_f2 ,     29.0  ,    0.0 (*              |              ),29.00, 29.00, 29.00, 29.00, 29.00
   1 ,    gen100_f2 ,     29.0  ,    0.0 (*              |              ),29.00, 29.00, 29.00, 29.00, 29.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,    gen100_f3 ,     12.0  ,    5.0 ( -- *-         |              ), 7.00, 11.00, 13.00, 14.00, 17.00
   2 ,     gen80_f3 ,     14.0  ,    5.0 (   - *--       |              ),10.00, 12.00, 14.00, 17.00, 21.00
   3 ,     gen60_f3 ,     20.0  ,    9.0 (    -- * --    |              ),13.00, 18.00, 20.00, 24.00, 29.00
   4 ,     gen40_f3 ,     26.0  ,    9.0 (       --  *-- |              ),20.00, 23.00, 28.00, 30.00, 35.00
   5 ,     gen20_f3 ,     35.0  ,   12.0 (         --   *| ---          ),24.00, 29.00, 35.00, 41.00, 47.00
   6 ,      gen0_f3 ,     44.0  ,    9.0 (            ---|- * ----      ),31.00, 40.00, 44.00, 48.00, 56.00
```

### Time Taken : 6.91798901558
![1](../../../src/img/vary_cost/CSFDandMarketingSD.png)

### Decisions Ranked
```
+------+----------------------------------------------+----------+-------+------+
| rank |                     name                     |   type   | value | cost |
+------+----------------------------------------------+----------+-------+------+
|  1   |             Manage Receivables               |   task   |   -1  |  4   |
|  2   |                  Agreement                   | resource |   -1  |  4   |
|  3   |            Participate in events             |   task   |   -1  |  5   |
|  4   |         ! Provide money for services         |   task   |   -1  |  4   |
|  5   |               Manage Accounts                |   task   |   -1  |  5   |
|  6   |                 Sponsor Logo                 | resource |   -1  |  3   |
|  7   |         Manage\nPartner Relationship         |   task   |   -1  |  4   |
|  8   |        ! Write Articles for Website          |   task   |   -1  |  5   |
|  9   |                    Funds                     | resource |   -1  |  3   |
|  10  |             Pledge\nDuring event             |   task   |   -1  |  5   |
|  11  |         Provide fundraising services         |   task   |   -1  |  3   |
|  12  |         Provide fundraising services         |   task   |   -1  |  3   |
|  13  |           Philanthropic donations            |   task   |   -1  |  4   |
|  14  |             ! Market CS Service              |   task   |   -1  |  5   |
|  15  |        Use sponsor marketing channels        |   task   |   1   |  1   |
|  16  |           Create General Ledgers             |   task   |   -1  |  4   |
|  17  |               Provide receipts               |   task   |   1   |  1   |
|  18  |            Provide free services             |   task   |   -1  |  3   |
|  19  |           National Event Calendar            | resource |   -1  |  3   |
|  20  |        ! Provide compiled call data          |   task   |   -1  |  3   |
|  21  | ! Counselor Speak on Kids Issues in General  |   task   |   1   |  1   |
|  22  |       Provide Online Donor Technology        |   task   |   1   |  1   |
|  23  |    Single charitable registration number     | resource |   -1  |  5   |
|  24  |       Provide Document Library System        |   task   |   1   |  2   |
|  25  |              Free advertisement              | resource |   1   |  2   |
|  26  |       ! Write Articles for Magazines         |   task   |   1   |  1   |
|  27  |            Collect Pledge online             |   task   |   -1  |  1   |
|  28  |           Get sponsors for events            |   task   |   -1  |  3   |
|  29  |             Sponsorship proposal             |   task   |   -1  |  2   |
|  30  |  Get Corporate Partner Information from DL   |   task   |   -1  |  3   |
|  31  |                Pledge online                 |   task   |   -1  |  2   |
|  32  |                Provide funds                 |   task   |   1   |  1   |
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
|                Provide Online Donor Technology                 |   task   |   1   |
|                      Pledge\nDuring event                      |   task   |   -1  |
|                   Accountability of services                   | softgoal |   1   |
|                Recognize\nSponsor contribution                 | softgoal |   1   |
|                ! Write Articles for Magazines                  |   task   |   1   |
|                  Exclusive Brand and Logo use                  | softgoal |   1   |
|               High Response [Individual Donors]                | softgoal |   1   |
|             Single charitable registration number              | resource |   -1  |
|                    National Event Calendar                     | resource |   -1  |
|                      Quality [Services]                        | softgoal |   1   |
|                  *Engage employees in events                   | softgoal |   1   |
|                           CS Stories                           | softgoal |   1   |
|                        Provide receipts                        |   task   |   1   |
|                     Collect Pledge online                      |   task   |   -1  |
|                       Free advertisement                       | resource |   1   |
|                      Published CS Stories                      | softgoal |   1   |
| Increase Access Speed [  Regional Offices to Document Library] | softgoal |   1   |
|                   Engage Employees in events                   | softgoal |   1   |
|                             Funds                              | resource |   -1  |
|                  Regional Staff feel included                  | softgoal |   1   |
|                      Sponsorship proposal                      |   task   |   1   |
|               Follow Highest Ethical Guidelines                | softgoal |   1   |
|                !Acquire public speaking skills                 | softgoal |   1   |
|                    Create General Ledgers                      |   task   |   -1  |
|                  Regional\nContact management                  | softgoal |   1   |
|                  Regional\nContact management                  | softgoal |   -1  |
|                          Sponsor Logo                          | resource |   -1  |
|                 ! Provide compiled call data                   |   task   |   -1  |
|                 Use sponsor marketing channels                 |   task   |   1   |
|           Get Corporate Partner Information from DL            |   task   |   1   |
|                      Manage Receivables                        |   task   |   -1  |
|                     Demonstrable Services                      | softgoal |   1   |
|                  Provide fundraising services                  |   task   |   -1  |
|                Provide Document Library System                 |   task   |   1   |
|                  ! Provide money for services                  |   task   |   -1  |
|                        Manage Accounts                         |   task   |   -1  |
|          ! Counselor Speak on Kids Issues in General           |   task   |   1   |
|                      [Increase] Awareness                      | softgoal |   1   |
|                         Provide funds                          |   task   |   -1  |
|                      Promotion Resources                       | softgoal |   1   |
|                     Provide free services                      |   task   |   -1  |
|                Experienced [marketing partners]                | softgoal |   1   |
|                    Credibility [CS Brand]                      | softgoal |   1   |
|                    Get sponsors for events                     |   task   |   -1  |
|         ! Services be provided for Kids Bullying Line          |   goal   |   1   |
|                         Pledge online                          |   task   |   -1  |
|                       Retain [Sponsors]                        | softgoal |   1   |
|                      Presentation Skills                       | softgoal |   1   |
|                    Philanthropic donations                     |   task   |   -1  |
|                  Manage\nPartner Relationship                  |   task   |   -1  |
|                 ! Write Articles for Website                   |   task   |   -1  |
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
