## [Model](https://github.com/ai-se/softgoals/blob/master/pdf/AOWS.pdf)
## sample
### Early Termination Cost = 29
```

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen2_f1 ,      5.0  ,   19.0 (*--------------|------------  ), 5.00,  5.00,  5.00,  6.00, 26.00
   1 ,      gen4_f1 ,      5.0  ,   19.0 (*--------------|------------  ), 5.00,  5.00,  5.00,  6.00, 26.00
   1 ,      gen6_f1 ,      5.0  ,   19.0 (*--------------|------------  ), 5.00,  5.00,  5.00,  6.00, 26.00
   1 ,      gen8_f1 ,      5.0  ,   19.0 (*--------------|------------  ), 5.00,  5.00,  5.00,  6.00, 26.00
   1 ,     gen10_f1 ,      5.0  ,   19.0 (*--------------|------------  ), 5.00,  5.00,  5.00,  5.00, 26.00
   1 ,      gen0_f1 ,      6.0  ,   19.0 ( *-------------|------------  ), 5.00,  5.00,  6.00,  6.00, 26.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f2 ,      5.0  ,   31.0 (*--------------|-----------   ), 5.00,  5.00,  5.00,  5.00, 38.00
   1 ,      gen2_f2 ,      5.0  ,   31.0 (*--------------|-----------   ), 5.00,  5.00,  5.00,  5.00, 38.00
   1 ,      gen4_f2 ,      5.0  ,   31.0 (*--------------|-----------   ), 5.00,  5.00,  5.00,  5.00, 38.00
   1 ,      gen6_f2 ,      5.0  ,   33.0 (*--------------|-----------   ), 5.00,  5.00,  5.00,  5.00, 38.00
   1 ,      gen8_f2 ,      5.0  ,   33.0 (*--------------|-----------   ), 5.00,  5.00,  5.00,  5.00, 38.00
   1 ,     gen10_f2 ,      5.0  ,   33.0 (*--------------|-----------   ), 5.00,  5.00,  5.00,  5.00, 38.00

rank ,         name ,    med   ,   iqr 
----------------------------------------------------
   1 ,      gen0_f3 ,      0.0  ,    4.0 (*--------------|------------- ), 0.00,  0.00,  0.00,  0.00,  4.00
   1 ,      gen2_f3 ,      0.0  ,    4.0 (*--------------|------------- ), 0.00,  0.00,  0.00,  0.00,  4.00
   1 ,      gen4_f3 ,      0.0  ,    4.0 (*--------------|------------- ), 0.00,  0.00,  0.00,  0.00,  4.00
   1 ,      gen6_f3 ,      0.0  ,    4.0 (*--------------|------------- ), 0.00,  0.00,  0.00,  0.00,  4.00
   1 ,      gen8_f3 ,      0.0  ,    4.0 (*--------------|------------- ), 0.00,  0.00,  0.00,  0.00,  4.00
   1 ,     gen10_f3 ,      0.0  ,    4.0 (*--------------|------------- ), 0.00,  0.00,  0.00,  0.00,  4.00
```
![1](../../../src/img/early_termination/sample.png)
### Smoothened Plot
![1](../../../src/img/early_termination/sample_smooth.png)

### Decisions Ranked
```
+------+-------------------------------------------------------+----------+-------+------+---------+
| rank |                          name                         |   type   | value | cost | support |
+------+-------------------------------------------------------+----------+-------+------+---------+
|  1   |                   J2EE Specification                  |   task   |   1   |  0   | 0.05348 |
|  2   |                    Data Model Pilot                   |   task   |   1   |  0   | 0.05306 |
|  3   |        External data model can be extended(19)        |   goal   |   1   |  4   | 0.05166 |
|  4   |                   Documentation Tool                  | resource |   1   |  0   | 0.05064 |
|  5   |                     Bakeoff Result                    |   task   |   1   |  0   |  0.0502 |
|  6   |                Access Control Assessed                |   task   |   1   |  0   | 0.04691 |
|  7   | XXX coordinates and internal client does whatever(17) |   goal   |   1   |  3   | 0.04672 |
|  8   |                     Pnp Framework                     |   goal   |   -1  |  5   | 0.04615 |
|  9   |                    General Test Env                   |   task   |   1   |  0   | 0.04615 |
|  10  |                  Access Control Pilot                 |   task   |   1   |  0   | 0.04542 |
|  11  |                    Monitoring Pilot                   |   task   |   1   |  0   | 0.04471 |
|  12  |                   DB Vendor Test Env                  |   task   |   1   |  0   | 0.04471 |
|  13  |                   Data Service Spec                   |   task   |   1   |  0   | 0.04256 |
|  14  |                         3 Tier                        |   goal   |   1   |  5   | 0.04206 |
|  15  |       Svc layer w/ extracted biz logic in DB(12)      |   goal   |   1   |  3   | 0.04149 |
|  16  |          Svc layer w/ extracted biz logic(13)         |   goal   |   1   |  5   | 0.03278 |
|  17  |       Provide logical data scheme internally(8)       |   goal   |   1   |  3   |  0.0301 |
|  18  |           Define ext mandatory data std(18)           |   goal   |   1   |  3   |  0.0301 |
|  19  |                         2 Tier                        |   goal   |   1   |  5   |  0.0292 |
|  20  |                   Data Service Pilot                  |   task   |   1   |  0   | 0.02884 |
|  21  | XXX coordinates and external client does whatever(20) |   goal   |   1   |  5   | 0.02717 |
|  22  |   External clients get exactly what they request(10)  |   goal   |   1   |  4   | 0.02657 |
|  23  |       Define data model for all shared data(15)       |   goal   |   1   |  3   | 0.02599 |
|  24  |                      New Database                     |   goal   |   1   |  6   | 0.02221 |
+------+-------------------------------------------------------+----------+-------+------+---------+
```

### Support Chart
![1](../../../src/img/early_termination/sample_support.png)
![1](../../../src/img/early_termination/sample_tree.png)
##[Recommendation](../../../src/img/early_termination/sample_choices.png)

### Decisions Clustered
```
+------------+-------------------------------------------------------+
| Cluster ID |                     Decision Name                     |
+------------+-------------------------------------------------------+
|     1      |                   J2EE Specification                  |
|     "      |                    Data Model Pilot                   |
|     "      |        External data model can be extended(19)        |
|     "      |                   Documentation Tool                  |
|     "      |                     Bakeoff Result                    |
|     "      |                Access Control Assessed                |
|     "      | XXX coordinates and internal client does whatever(17) |
|     "      |                     Pnp Framework                     |
|     "      |                    General Test Env                   |
|     "      |                  Access Control Pilot                 |
|     "      |                    Monitoring Pilot                   |
|     "      |                   DB Vendor Test Env                  |
|     "      |                   Data Service Spec                   |
|     2      |                         3 Tier                        |
|     3      |       Svc layer w/ extracted biz logic in DB(12)      |
|     4      |          Svc layer w/ extracted biz logic(13)         |
|     5      |       Provide logical data scheme internally(8)       |
|     6      |           Define ext mandatory data std(18)           |
|     7      |                         2 Tier                        |
|     "      |                   Data Service Pilot                  |
|     8      | XXX coordinates and external client does whatever(20) |
|     9      |   External clients get exactly what they request(10)  |
|     "      |       Define data model for all shared data(15)       |
|     "      |                      New Database                     |
+------------+-------------------------------------------------------+
```

### Time Taken : 37.573734045
