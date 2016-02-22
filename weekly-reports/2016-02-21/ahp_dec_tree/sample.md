## sample
```
..........32 41

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f1 ,      6.0  ,   23.0 (-*             |          --- ), 5.00,  6.00,  6.00, 29.00, 32.00
   1 ,      gen2_f1 ,      6.0  ,   24.0 (-*             |        ---   ), 5.00,  6.00,  6.00, 27.00, 30.00
   1 ,      gen4_f1 ,      6.0  ,   24.0 ( *             |        ---   ), 5.00,  5.00,  6.00, 27.00, 30.00
   1 ,      gen6_f1 ,      6.0  ,   22.0 ( *             |        --    ), 5.00,  5.00,  6.00, 27.00, 29.00
   1 ,      gen8_f1 ,      6.0  ,   22.0 ( *             |        --    ), 5.00,  5.00,  6.00, 27.00, 29.00
   1 ,     gen10_f1 ,      6.0  ,   22.0 ( *             |        --    ), 5.00,  5.00,  6.00, 27.00, 29.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,      5.0  ,   34.0 (*              |            - ), 5.00,  5.00,  5.00, 39.00, 41.00
   1 ,      gen2_f2 ,      5.0  ,   34.0 (*              |            - ), 5.00,  5.00,  5.00, 39.00, 41.00
   1 ,      gen4_f2 ,      5.0  ,   34.0 (*              |            - ), 5.00,  5.00,  5.00, 39.00, 41.00
   1 ,      gen6_f2 ,      5.0  ,   36.0 (*              |            - ), 5.00,  5.00,  5.00, 39.00, 41.00
   1 ,      gen8_f2 ,      5.0  ,   36.0 (*              |            - ), 5.00,  5.00,  5.00, 39.00, 41.00
   1 ,     gen10_f2 ,      5.0  ,   36.0 (*              |            - ), 5.00,  5.00,  5.00, 39.00, 41.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f3 ,      4.0  ,    1.0 (---------------|-------------*), 0.00,  4.00,  4.00,  4.00,  4.00
   1 ,      gen2_f3 ,      4.0  ,    0.0 (       --------|-------------*), 1.00,  4.00,  4.00,  4.00,  4.00
   1 ,      gen4_f3 ,      4.0  ,    0.0 (              -|-------------*), 2.00,  4.00,  4.00,  4.00,  4.00
   1 ,      gen6_f3 ,      4.0  ,    0.0 (              -|-------------*), 2.00,  4.00,  4.00,  4.00,  4.00
   1 ,      gen8_f3 ,      4.0  ,    0.0 (               |      -------*), 3.00,  4.00,  4.00,  4.00,  4.00
   1 ,     gen10_f3 ,      4.0  ,    0.0 (               |      -------*), 3.00,  4.00,  4.00,  4.00,  4.00
```

### Time Taken : 2.27139902115
![1](../../../src/img/ahp_dec_tree/sample.png)

### Decisions Ranked
```
+------+-------------------------------------------------------+----------+-------+------+---------+
| rank |                          name                         |   type   | value | cost | support |
+------+-------------------------------------------------------+----------+-------+------+---------+
|  1   |                   J2EE Specification                  |   task   |   1   |  0   | 0.10997 |
|  2   |                   Documentation Tool                  | resource |   1   |  0   | 0.10848 |
|  3   |                     Bakeoff Result                    |   task   |   1   |  0   | 0.10848 |
|  4   |                Access Control Assessed                |   task   |   1   |  0   |  0.1057 |
|  5   |                  Access Control Pilot                 |   task   |   1   |  0   | 0.10511 |
|  6   |                    General Test Env                   |   task   |   1   |  0   | 0.10494 |
|  7   |                   DB Vendor Test Env                  |   task   |   1   |  0   | 0.10358 |
|  8   |                    Monitoring Pilot                   |   task   |   1   |  0   | 0.10159 |
|  9   |                   Data Service Pilot                  |   task   |   1   |  0   | 0.10012 |
|  10  |       Provide logical data scheme internally(8)       |   goal   |   1   |  3   | 0.09264 |
|  11  |           Define ext mandatory data std(18)           |   goal   |   1   |  3   | 0.08794 |
|  12  |       Define data model for all shared data(15)       |   goal   |   1   |  3   | 0.08301 |
|  13  |                         2 Tier                        |   goal   |   1   |  5   | 0.07877 |
|  14  | XXX coordinates and internal client does whatever(17) |   goal   |   1   |  3   | 0.07613 |
|  15  |   External clients get exactly what they request(10)  |   goal   |   1   |  4   | 0.07545 |
|  16  |                   Data Service Spec                   |   task   |   1   |  0   | 0.07477 |
|  17  | XXX coordinates and external client does whatever(20) |   goal   |   1   |  5   | 0.07413 |
|  18  |                         3 Tier                        |   goal   |   1   |  5   | 0.07076 |
|  19  |                      New Database                     |   goal   |   -1  |  6   | 0.06124 |
|  20  |                     Pnp Framework                     |   goal   |   -1  |  5   | 0.05935 |
|  21  |                    Data Model Pilot                   |   task   |   1   |  0   | 0.05596 |
|  22  |       Svc layer w/ extracted biz logic in DB(12)      |   goal   |   1   |  3   | 0.05422 |
|  23  |          Svc layer w/ extracted biz logic(13)         |   goal   |   -1  |  5   | 0.05172 |
|  24  |        External data model can be extended(19)        |   goal   |   -1  |  4   | 0.05136 |
+------+-------------------------------------------------------+----------+-------+------+---------+
```
![1](../../../src/img/ahp_dec_tree/sample_tree.png)
