## [Model](https://github.com/ai-se/softgoals/blob/master/pdf/AOWS.pdf)
## sample
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,     gen20_f1 ,     9.04  ,  32.22 (*              |        --    ), 9.04,  9.04,  9.04, 41.26, 44.15
   1 ,     gen40_f1 ,     9.04  ,  32.22 (*              |        --    ), 9.04,  9.04,  9.04, 41.26, 44.15
   1 ,     gen60_f1 ,     9.04  ,  32.22 (*              |        --    ), 9.04,  9.04,  9.04, 41.26, 44.15
   1 ,     gen80_f1 ,     9.04  ,  32.22 (*              |        --    ), 9.04,  9.04,  9.04, 41.26, 44.15
   1 ,    gen100_f1 ,     9.04  ,  32.22 (*              |        --    ), 9.04,  9.04,  9.04, 41.26, 44.15
   1 ,      gen0_f1 ,    11.16  ,  31.06 (-*             |        ---   ), 9.04, 11.16, 11.16, 41.26, 46.37

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,     9.37  ,  53.76 (-*             |           -- ), 6.45,  9.37,  9.37, 60.00, 63.27
   1 ,     gen20_f2 ,     9.37  ,  51.56 ( *             |            - ), 9.37,  9.37,  9.37, 60.88, 63.27
   1 ,     gen40_f2 ,     9.37  ,  53.69 ( *             |            - ), 9.37,  9.37,  9.37, 60.88, 63.27
   1 ,     gen60_f2 ,     9.37  ,   53.9 ( *             |              ), 9.37,  9.37,  9.37, 63.06, 63.94
   1 ,     gen80_f2 ,     9.37  ,   53.9 ( *             |              ), 9.37,  9.37,  9.37, 63.06, 63.94
   1 ,    gen100_f2 ,     9.37  ,   53.9 ( *             |              ), 9.37,  9.37,  9.37, 63.06, 63.94

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f3 ,      0.0  ,    4.0 (*              |              ), 0.00,  0.00,  0.00,  4.00,  4.00
   1 ,     gen20_f3 ,      0.0  ,    4.0 (*              |              ), 0.00,  0.00,  0.00,  4.00,  4.00
   1 ,     gen40_f3 ,      0.0  ,    4.0 (*              |              ), 0.00,  0.00,  0.00,  4.00,  4.00
   1 ,     gen60_f3 ,      0.0  ,    4.0 (*              |              ), 0.00,  0.00,  0.00,  4.00,  4.00
   1 ,     gen80_f3 ,      0.0  ,    4.0 (*              |              ), 0.00,  0.00,  0.00,  4.00,  4.00
   1 ,    gen100_f3 ,      0.0  ,    4.0 (*              |              ), 0.00,  0.00,  0.00,  4.00,  4.00
```
![1](../../../src/img/junk/sample.png)
### Smoothened Plot
![1](../../../src/img/junk/sample_smooth.png)

### Decisions Ranked
```
+------+-------------------------------------------------------+----------+-------+-------+---------+
| rank |                          name                         |   type   | value |  cost | support |
+------+-------------------------------------------------------+----------+-------+-------+---------+
|  1   |                   J2EE Specification                  |   task   |   1   |  0.0  | 0.11505 |
|  2   |   External clients get exactly what they request(10)  |   goal   |   1   |  4.58 | 0.10433 |
|  3   |                   Documentation Tool                  | resource |   1   |  0.0  | 0.10312 |
|  4   |                    Monitoring Pilot                   |   task   |   1   |  0.0  | 0.10236 |
|  5   |                     Bakeoff Result                    |   task   |   1   |  0.0  | 0.10088 |
|  6   |                Access Control Assessed                |   task   |   1   |  0.0  | 0.10015 |
|  7   |                  Access Control Pilot                 |   task   |   1   |  0.0  | 0.09873 |
|  8   |                    General Test Env                   |   task   |   1   |  0.0  | 0.09873 |
|  9   |                      New Database                     |   goal   |   -1  | 11.16 | 0.09707 |
|  10  |                   DB Vendor Test Env                  |   task   |   1   |  0.0  |  0.0947 |
|  11  |                     Pnp Framework                     |   goal   |   -1  |  9.04 | 0.08645 |
|  12  |                   Data Service Pilot                  |   task   |   1   |  0.0  | 0.08612 |
|  13  |                         3 Tier                        |   goal   |   1   |  6.42 | 0.08339 |
|  14  | XXX coordinates and internal client does whatever(17) |   goal   |   1   |  4.54 | 0.08263 |
|  15  | XXX coordinates and external client does whatever(20) |   goal   |   1   |  7.54 | 0.07901 |
|  16  |                    Data Model Pilot                   |   task   |   1   |  0.0  | 0.07873 |
|  17  |       Provide logical data scheme internally(8)       |   goal   |   1   |  3.29 | 0.07822 |
|  18  |                   Data Service Spec                   |   task   |   1   |  0.0  |  0.0776 |
|  19  |       Define data model for all shared data(15)       |   goal   |   1   |  4.22 | 0.07682 |
|  20  |                         2 Tier                        |   goal   |   1   |  9.31 | 0.07438 |
|  21  |           Define ext mandatory data std(18)           |   goal   |   1   |  4.04 |  0.0626 |
|  22  |       Svc layer w/ extracted biz logic in DB(12)      |   goal   |   -1  |  5.26 | 0.05513 |
|  23  |          Svc layer w/ extracted biz logic(13)         |   goal   |   -1  |  5.95 | 0.05491 |
|  24  |        External data model can be extended(19)        |   goal   |   1   |  7.4  | 0.05424 |
+------+-------------------------------------------------------+----------+-------+-------+---------+
```

### Support Chart
![1](../../../src/img/junk/sample_support.png)
![1](../../../src/img/junk/sample_tree.png)
##[Recommendation](../../../src/img/junk/sample_choices.png)

### Decisions Clustered
```
+------------+-------------------------------------------------------+
| Cluster ID |                     Decision Name                     |
+------------+-------------------------------------------------------+
|     1      |                   J2EE Specification                  |
|    1,2     |   External clients get exactly what they request(10)  |
|     "      |                   Documentation Tool                  |
|     "      |                    Monitoring Pilot                   |
|     "      |                     Bakeoff Result                    |
|    1,3     |                Access Control Assessed                |
|     "      |                  Access Control Pilot                 |
|    1,4     |                    General Test Env                   |
|     "      |                      New Database                     |
|    1,5     |                   DB Vendor Test Env                  |
|     "      |                     Pnp Framework                     |
|    2,6     |                   Data Service Pilot                  |
|     "      |                         3 Tier                        |
|     "      | XXX coordinates and internal client does whatever(17) |
|     "      | XXX coordinates and external client does whatever(20) |
|     "      |                    Data Model Pilot                   |
|     "      |       Provide logical data scheme internally(8)       |
|     "      |                   Data Service Spec                   |
|     "      |       Define data model for all shared data(15)       |
|     "      |                         2 Tier                        |
|     "      |           Define ext mandatory data std(18)           |
|     "      |       Svc layer w/ extracted biz logic in DB(12)      |
|     "      |          Svc layer w/ extracted biz logic(13)         |
|     "      |        External data model can be extended(19)        |
+------------+-------------------------------------------------------+
```

### Time Taken : 51.5230050087
