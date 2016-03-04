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
   1 ,      gen6_f2 ,      5.0  ,   31.0 (*--------------|-----------   ), 5.00,  5.00,  5.00,  5.00, 38.00
   1 ,      gen8_f2 ,      5.0  ,   31.0 (*--------------|-----------   ), 5.00,  5.00,  5.00,  5.00, 38.00
   1 ,     gen10_f2 ,      5.0  ,   31.0 (*--------------|-----------   ), 5.00,  5.00,  5.00,  5.00, 38.00

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
|  1   |                     Pnp Framework                     |   goal   |   -1  |  5   |  0.0581 |
|  2   |                      New Database                     |   goal   |   -1  |  6   | 0.05664 |
|  3   |                    Data Model Pilot                   |   task   |   1   |  0   | 0.04751 |
|  4   |        External data model can be extended(19)        |   goal   |   1   |  4   |  0.0468 |
|  5   |                   J2EE Specification                  |   task   |   1   |  0   |  0.0459 |
|  6   |                   Documentation Tool                  | resource |   1   |  0   | 0.04147 |
|  7   |                    Monitoring Pilot                   |   task   |   1   |  0   | 0.03907 |
|  8   |                    General Test Env                   |   task   |   1   |  0   | 0.03843 |
|  9   |                Access Control Assessed                |   task   |   1   |  0   | 0.03812 |
|  10  |                     Bakeoff Result                    |   task   |   1   |  0   | 0.03812 |
|  11  |                   DB Vendor Test Env                  |   task   |   1   |  0   | 0.03636 |
|  12  |                  Access Control Pilot                 |   task   |   1   |  0   | 0.03528 |
|  13  | XXX coordinates and internal client does whatever(17) |   goal   |   1   |  3   | 0.03316 |
|  14  |                         2 Tier                        |   goal   |   1   |  5   | 0.03291 |
|  15  |   External clients get exactly what they request(10)  |   goal   |   1   |  4   | 0.03179 |
|  16  |                   Data Service Pilot                  |   task   |   1   |  0   | 0.02868 |
|  17  |                   Data Service Spec                   |   task   |   1   |  0   | 0.02797 |
|  18  |                         3 Tier                        |   goal   |   1   |  5   | 0.02517 |
|  19  | XXX coordinates and external client does whatever(20) |   goal   |   1   |  5   | 0.02137 |
|  20  |       Define data model for all shared data(15)       |   goal   |   -1  |  3   | 0.02077 |
|  21  |           Define ext mandatory data std(18)           |   goal   |   -1  |  3   | 0.02073 |
|  22  |       Provide logical data scheme internally(8)       |   goal   |   -1  |  3   | 0.01865 |
|  23  |          Svc layer w/ extracted biz logic(13)         |   goal   |   1   |  5   | 0.01803 |
|  24  |       Svc layer w/ extracted biz logic in DB(12)      |   goal   |   -1  |  3   | 0.01735 |
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
|     1      |                     Pnp Framework                     |
|     "      |                      New Database                     |
|     2      |                    Data Model Pilot                   |
|     "      |        External data model can be extended(19)        |
|     "      |                   J2EE Specification                  |
|     "      |                   Documentation Tool                  |
|     "      |                    Monitoring Pilot                   |
|     "      |                    General Test Env                   |
|     "      |                Access Control Assessed                |
|     "      |                     Bakeoff Result                    |
|     "      |                   DB Vendor Test Env                  |
|     "      |                  Access Control Pilot                 |
|     "      | XXX coordinates and internal client does whatever(17) |
|     "      |                         2 Tier                        |
|     "      |   External clients get exactly what they request(10)  |
|     "      |                   Data Service Pilot                  |
|     "      |                   Data Service Spec                   |
|     "      |                         3 Tier                        |
|     "      | XXX coordinates and external client does whatever(20) |
|     "      |       Define data model for all shared data(15)       |
|     "      |           Define ext mandatory data std(18)           |
|     "      |       Provide logical data scheme internally(8)       |
|     "      |          Svc layer w/ extracted biz logic(13)         |
|     "      |       Svc layer w/ extracted biz logic in DB(12)      |
+------------+-------------------------------------------------------+
```

### Time Taken : 56.8417711258
