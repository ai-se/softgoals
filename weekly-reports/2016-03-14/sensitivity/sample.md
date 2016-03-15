

### Cluster 1
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |  0.0   |  0  |
|     costs     |  6.0   | 0.0 |
|    benefits   |  10.0  | 0.0 |
| decisions_set |  1.0   |  1  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+----------------+----------------+
|                          Node                         |      Cost      |    Benefit     |
+-------------------------------------------------------+----------------+----------------+
|                    Data Service(7)                    | 3.00 +/- 6.00  | 10.00 +/- 5.00 |
|                     Pnp Framework                     | 10.00 +/- 5.00 | 5.00 +/- 5.00  |
|                      New Database                     | 6.00 +/- 0.00  | 10.00 +/- 0.00 |
|       Provide logical data scheme internally(8)       | 3.00 +/- 6.00  | 3.00 +/- 6.00  |
|        External data model can be extended(19)        | 8.00 +/- 4.00  | 5.00 +/- 5.00  |
|       Svc layer w/ extracted biz logic in DB(12)      | 3.00 +/- 6.00  | 10.00 +/- 5.00 |
|          Svc layer w/ extracted biz logic(13)         | 5.00 +/- 0.00  | 6.00 +/- 3.00  |
|   External clients get exactly what they request(10)  | 4.00 +/- 8.00  | 3.00 +/- 6.00  |
| XXX coordinates and internal client does whatever(17) | 3.00 +/- 3.00  | 3.00 +/- 3.00  |
|                    Regression Test                    | 6.00 +/- 3.00  | 10.00 +/- 5.00 |
|       Define data model for all shared data(15)       | 6.00 +/- 3.00  | 3.00 +/- 6.00  |
|                     Documentation                     | 6.00 +/- 3.00  | 10.00 +/- 5.00 |
|                         2 Tier                        | 10.00 +/- 5.00 | 5.00 +/- 10.00 |
|           Define ext mandatory data std(18)           | 3.00 +/- 6.00  | 10.00 +/- 5.00 |
|                      Monitor(11)                      | 1.00 +/- 1.00  | 5.00 +/- 10.00 |
| XXX coordinates and external client does whatever(20) | 10.00 +/- 5.00 | 6.00 +/- 3.00  |
|        Build internal extensible data model(16)       | 4.00 +/- 2.00  | 6.00 +/- 3.00  |
|                    App Framework(6)                   | 10.00 +/- 5.00 | 5.00 +/- 10.00 |
|                         3 Tier                        | 5.00 +/- 10.00 | 10.00 +/- 5.00 |
+-------------------------------------------------------+----------------+----------------+
```

### Cluster 2
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |   0    |  0  |
|     costs     |  6.0   | 1.0 |
|    benefits   |  5.0   | 0.0 |
| decisions_set |   2    |  0  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+-----------------+-----------------+
|                          Node                         |       Cost      |     Benefit     |
+-------------------------------------------------------+-----------------+-----------------+
|                    Data Service(7)                    |  3.00 +/- 3.00  |  10.00 +/- 5.00 |
|                     Pnp Framework                     | 10.00 +/- 10.00 |  5.00 +/- 0.00  |
|                      New Database                     |  6.00 +/- 6.00  |  5.00 +/- 0.00  |
|       Provide logical data scheme internally(8)       |  6.00 +/- 3.00  |  6.00 +/- 3.00  |
|        External data model can be extended(19)        |  8.00 +/- 0.00  |  15.00 +/- 5.00 |
|       Svc layer w/ extracted biz logic in DB(12)      |  6.00 +/- 6.00  |  10.00 +/- 5.00 |
|          Svc layer w/ extracted biz logic(13)         |  10.00 +/- 5.00 |  6.00 +/- 3.00  |
|   External clients get exactly what they request(10)  |  8.00 +/- 4.00  |  6.00 +/- 6.00  |
| XXX coordinates and internal client does whatever(17) |  9.00 +/- 3.00  |  6.00 +/- 6.00  |
|                    Regression Test                    |  6.00 +/- 0.00  | 10.00 +/- 10.00 |
|       Define data model for all shared data(15)       |  6.00 +/- 3.00  |  9.00 +/- 3.00  |
|                     Documentation                     |  6.00 +/- 0.00  | 10.00 +/- 10.00 |
|                         2 Tier                        |  10.00 +/- 5.00 |  5.00 +/- 0.00  |
|           Define ext mandatory data std(18)           |  6.00 +/- 3.00  |  10.00 +/- 5.00 |
|                      Monitor(11)                      |  2.00 +/- 2.00  |  15.00 +/- 5.00 |
| XXX coordinates and external client does whatever(20) |  10.00 +/- 5.00 |  6.00 +/- 3.00  |
|        Build internal extensible data model(16)       |  6.00 +/- 2.00  |  6.00 +/- 6.00  |
|                    App Framework(6)                   |  10.00 +/- 0.00 |  10.00 +/- 0.00 |
|                         3 Tier                        |  10.00 +/- 5.00 | 10.00 +/- 10.00 |
+-------------------------------------------------------+-----------------+-----------------+
```

### Cluster 3
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |  0.0   |  0  |
|     costs     |  5.0   | 1.0 |
|    benefits   |  10.0  | 0.0 |
| decisions_set |  2.0   |  0  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+----------------+----------------+
|                          Node                         |      Cost      |    Benefit     |
+-------------------------------------------------------+----------------+----------------+
|                    Data Service(7)                    | 6.00 +/- 3.00  | 5.00 +/- 10.00 |
|                     Pnp Framework                     | 5.00 +/- 5.00  | 10.00 +/- 0.00 |
|                      New Database                     | 6.00 +/- 12.00 | 5.00 +/- 5.00  |
|       Provide logical data scheme internally(8)       | 3.00 +/- 6.00  | 3.00 +/- 3.00  |
|        External data model can be extended(19)        | 4.00 +/- 8.00  | 5.00 +/- 5.00  |
|       Svc layer w/ extracted biz logic in DB(12)      | 6.00 +/- 3.00  | 5.00 +/- 5.00  |
|          Svc layer w/ extracted biz logic(13)         | 5.00 +/- 10.00 | 3.00 +/- 3.00  |
|   External clients get exactly what they request(10)  | 4.00 +/- 8.00  | 6.00 +/- 3.00  |
| XXX coordinates and internal client does whatever(17) | 3.00 +/- 6.00  | 3.00 +/- 6.00  |
|                    Regression Test                    | 9.00 +/- 0.00  | 10.00 +/- 5.00 |
|       Define data model for all shared data(15)       | 3.00 +/- 6.00  | 3.00 +/- 6.00  |
|                     Documentation                     | 7.50 +/- 0.00  | 7.50 +/- 5.00  |
|                         2 Tier                        | 7.50 +/- 5.00  | 10.00 +/- 5.00 |
|           Define ext mandatory data std(18)           | 3.00 +/- 3.00  | 5.00 +/- 10.00 |
|                      Monitor(11)                      | 2.00 +/- 1.00  | 10.00 +/- 5.00 |
| XXX coordinates and external client does whatever(20) | 5.00 +/- 5.00  | 3.00 +/- 3.00  |
|        Build internal extensible data model(16)       | 2.00 +/- 2.00  | 6.00 +/- 3.00  |
|                    App Framework(6)                   | 7.50 +/- 0.00  | 10.00 +/- 5.00 |
|                         3 Tier                        | 5.00 +/- 5.00  | 5.00 +/- 0.00  |
+-------------------------------------------------------+----------------+----------------+
```

### Cluster 4
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |   0    |  0  |
|     costs     |  5.0   | 0.0 |
|    benefits   |  15.0  | 0.0 |
| decisions_set |   2    |  0  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+-----------------+-----------------+
|                          Node                         |       Cost      |     Benefit     |
+-------------------------------------------------------+-----------------+-----------------+
|                    Data Service(7)                    |  6.00 +/- 3.00  |  10.00 +/- 5.00 |
|                     Pnp Framework                     |  5.00 +/- 0.00  |  15.00 +/- 0.00 |
|                      New Database                     |  12.00 +/- 6.00 | 10.00 +/- 10.00 |
|       Provide logical data scheme internally(8)       |  6.00 +/- 3.00  |  9.00 +/- 0.00  |
|        External data model can be extended(19)        |  4.00 +/- 0.00  | 10.00 +/- 10.00 |
|       Svc layer w/ extracted biz logic in DB(12)      |  6.00 +/- 6.00  | 10.00 +/- 10.00 |
|          Svc layer w/ extracted biz logic(13)         |  5.00 +/- 0.00  |  6.00 +/- 6.00  |
|   External clients get exactly what they request(10)  |  8.00 +/- 4.00  |  9.00 +/- 3.00  |
| XXX coordinates and internal client does whatever(17) |  9.00 +/- 3.00  |  6.00 +/- 6.00  |
|                    Regression Test                    |  6.00 +/- 6.00  | 10.00 +/- 10.00 |
|       Define data model for all shared data(15)       |  9.00 +/- 3.00  |  6.00 +/- 3.00  |
|                     Documentation                     |  6.00 +/- 3.00  | 10.00 +/- 10.00 |
|                         2 Tier                        |  10.00 +/- 5.00 | 10.00 +/- 10.00 |
|           Define ext mandatory data std(18)           |  9.00 +/- 0.00  | 15.00 +/- 10.00 |
|                      Monitor(11)                      |  2.00 +/- 0.00  |  10.00 +/- 5.00 |
| XXX coordinates and external client does whatever(20) |  10.00 +/- 5.00 |  6.00 +/- 6.00  |
|        Build internal extensible data model(16)       |  4.00 +/- 2.00  |  3.00 +/- 6.00  |
|                    App Framework(6)                   | 10.00 +/- 10.00 |  10.00 +/- 5.00 |
|                         3 Tier                        | 10.00 +/- 10.00 |  5.00 +/- 5.00  |
+-------------------------------------------------------+-----------------+-----------------+
```

### Cluster 5
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |  0.0   |  0  |
|     costs     |  10.0  | 0.0 |
|    benefits   |  10.0  | 5.0 |
| decisions_set |  2.0   |  0  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+----------------+----------------+
|                          Node                         |      Cost      |    Benefit     |
+-------------------------------------------------------+----------------+----------------+
|                    Data Service(7)                    | 6.00 +/- 3.00  | 5.00 +/- 5.00  |
|                     Pnp Framework                     | 10.00 +/- 0.00 | 10.00 +/- 5.00 |
|                      New Database                     | 18.00 +/- 0.00 | 5.00 +/- 10.00 |
|       Provide logical data scheme internally(8)       | 3.00 +/- 6.00  | 3.00 +/- 3.00  |
|        External data model can be extended(19)        | 4.00 +/- 4.00  | 5.00 +/- 10.00 |
|       Svc layer w/ extracted biz logic in DB(12)      | 3.00 +/- 3.00  | 5.00 +/- 10.00 |
|          Svc layer w/ extracted biz logic(13)         | 5.00 +/- 5.00  | 3.00 +/- 6.00  |
|   External clients get exactly what they request(10)  | 4.00 +/- 8.00  | 3.00 +/- 6.00  |
| XXX coordinates and internal client does whatever(17) | 6.00 +/- 3.00  | 3.00 +/- 3.00  |
|                    Regression Test                    | 3.00 +/- 3.00  | 5.00 +/- 10.00 |
|       Define data model for all shared data(15)       | 3.00 +/- 6.00  | 6.00 +/- 3.00  |
|                     Documentation                     | 6.00 +/- 3.00  | 10.00 +/- 5.00 |
|                         2 Tier                        | 5.00 +/- 10.00 | 5.00 +/- 5.00  |
|           Define ext mandatory data std(18)           | 6.00 +/- 3.00  | 10.00 +/- 5.00 |
|                      Monitor(11)                      | 2.00 +/- 1.00  | 10.00 +/- 5.00 |
| XXX coordinates and external client does whatever(20) | 10.00 +/- 5.00 | 9.00 +/- 0.00  |
|        Build internal extensible data model(16)       | 2.00 +/- 4.00  | 6.00 +/- 0.00  |
|                    App Framework(6)                   | 10.00 +/- 5.00 | 5.00 +/- 5.00  |
|                         3 Tier                        | 10.00 +/- 5.00 | 10.00 +/- 5.00 |
+-------------------------------------------------------+----------------+----------------+
```

### Cluster 6
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |   0    |  0  |
|     costs     |  12.0  | 0.0 |
|    benefits   |  10.0  | 5.0 |
| decisions_set |   2    |  0  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+-----------------+-----------------+
|                          Node                         |       Cost      |     Benefit     |
+-------------------------------------------------------+-----------------+-----------------+
|                    Data Service(7)                    |  6.00 +/- 3.00  |  10.00 +/- 0.00 |
|                     Pnp Framework                     |  15.00 +/- 5.00 |  5.00 +/- 5.00  |
|                      New Database                     |  12.00 +/- 0.00 |  10.00 +/- 5.00 |
|       Provide logical data scheme internally(8)       |  3.00 +/- 3.00  |  6.00 +/- 6.00  |
|        External data model can be extended(19)        |  8.00 +/- 4.00  | 10.00 +/- 10.00 |
|       Svc layer w/ extracted biz logic in DB(12)      |  6.00 +/- 3.00  |  5.00 +/- 5.00  |
|          Svc layer w/ extracted biz logic(13)         | 10.00 +/- 10.00 |  6.00 +/- 0.00  |
|   External clients get exactly what they request(10)  |  8.00 +/- 4.00  |  3.00 +/- 3.00  |
| XXX coordinates and internal client does whatever(17) |  6.00 +/- 3.00  |  9.00 +/- 6.00  |
|                    Regression Test                    |  6.00 +/- 6.00  | 10.00 +/- 10.00 |
|       Define data model for all shared data(15)       |  6.00 +/- 3.00  |  3.00 +/- 3.00  |
|                     Documentation                     |  9.00 +/- 3.00  |  10.00 +/- 5.00 |
|                         2 Tier                        | 10.00 +/- 10.00 |  5.00 +/- 5.00  |
|           Define ext mandatory data std(18)           |  6.00 +/- 3.00  |  10.00 +/- 5.00 |
|                      Monitor(11)                      |  3.00 +/- 1.00  |  10.00 +/- 5.00 |
| XXX coordinates and external client does whatever(20) |  10.00 +/- 0.00 |  9.00 +/- 3.00  |
|        Build internal extensible data model(16)       |  4.00 +/- 4.00  |  6.00 +/- 3.00  |
|                    App Framework(6)                   |  15.00 +/- 5.00 |  15.00 +/- 5.00 |
|                         3 Tier                        | 10.00 +/- 10.00 |  10.00 +/- 5.00 |
+-------------------------------------------------------+-----------------+-----------------+
```

### Cluster 7
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |  0.0   |  0  |
|     costs     |  12.0  | 3.0 |
|    benefits   |  10.0  | 0.0 |
| decisions_set |  1.5   |  0  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+----------------+----------------+
|                          Node                         |      Cost      |    Benefit     |
+-------------------------------------------------------+----------------+----------------+
|                    Data Service(7)                    | 3.00 +/- 6.00  | 5.00 +/- 10.00 |
|                     Pnp Framework                     | 15.00 +/- 0.00 | 10.00 +/- 0.00 |
|                      New Database                     | 12.00 +/- 6.00 | 7.50 +/- 5.00  |
|       Provide logical data scheme internally(8)       | 3.00 +/- 6.00  | 3.00 +/- 3.00  |
|        External data model can be extended(19)        | 8.00 +/- 4.00  | 7.50 +/- 5.00  |
|       Svc layer w/ extracted biz logic in DB(12)      | 3.00 +/- 3.00  | 5.00 +/- 10.00 |
|          Svc layer w/ extracted biz logic(13)         | 5.00 +/- 10.00 | 6.00 +/- 3.00  |
|   External clients get exactly what they request(10)  | 4.00 +/- 8.00  | 4.50 +/- 0.00  |
| XXX coordinates and internal client does whatever(17) | 4.50 +/- 0.00  | 3.00 +/- 6.00  |
|                    Regression Test                    | 4.50 +/- 3.00  | 5.00 +/- 10.00 |
|       Define data model for all shared data(15)       | 3.00 +/- 6.00  | 3.00 +/- 6.00  |
|                     Documentation                     | 6.00 +/- 3.00  | 5.00 +/- 10.00 |
|                         2 Tier                        | 10.00 +/- 5.00 | 5.00 +/- 10.00 |
|           Define ext mandatory data std(18)           | 3.00 +/- 6.00  | 10.00 +/- 5.00 |
|                      Monitor(11)                      | 2.00 +/- 1.00  | 5.00 +/- 5.00  |
| XXX coordinates and external client does whatever(20) | 5.00 +/- 5.00  | 3.00 +/- 3.00  |
|        Build internal extensible data model(16)       | 3.00 +/- 2.00  | 6.00 +/- 3.00  |
|                    App Framework(6)                   | 10.00 +/- 5.00 | 10.00 +/- 5.00 |
|                         3 Tier                        | 5.00 +/- 10.00 | 7.50 +/- 0.00  |
+-------------------------------------------------------+----------------+----------------+
```

### Cluster 8
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |   0    |  4   |
|     costs     |  18.0  | 31.0 |
|    benefits   |  15.0  | 54.0 |
| decisions_set |   2    |  13  |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+-----------------+-----------------+
|                          Node                         |       Cost      |     Benefit     |
+-------------------------------------------------------+-----------------+-----------------+
|                    Data Service(7)                    |  9.00 +/- 3.00  | 10.00 +/- 10.00 |
|                     Pnp Framework                     |  10.00 +/- 5.00 |  15.00 +/- 5.00 |
|                      New Database                     | 18.00 +/- 12.00 | 10.00 +/- 10.00 |
|       Provide logical data scheme internally(8)       |  6.00 +/- 3.00  |  3.00 +/- 6.00  |
|        External data model can be extended(19)        |  8.00 +/- 4.00  |  10.00 +/- 5.00 |
|       Svc layer w/ extracted biz logic in DB(12)      |  6.00 +/- 3.00  |  10.00 +/- 0.00 |
|          Svc layer w/ extracted biz logic(13)         | 15.00 +/- 10.00 |  9.00 +/- 3.00  |
|   External clients get exactly what they request(10)  |  4.00 +/- 4.00  |  6.00 +/- 6.00  |
| XXX coordinates and internal client does whatever(17) |  6.00 +/- 3.00  |  6.00 +/- 6.00  |
|                    Regression Test                    |  6.00 +/- 6.00  |  15.00 +/- 5.00 |
|       Define data model for all shared data(15)       |  6.00 +/- 6.00  |  9.00 +/- 3.00  |
|                     Documentation                     |  6.00 +/- 3.00  |  10.00 +/- 5.00 |
|                         2 Tier                        |  10.00 +/- 5.00 |  5.00 +/- 5.00  |
|           Define ext mandatory data std(18)           |  6.00 +/- 3.00  | 15.00 +/- 10.00 |
|                      Monitor(11)                      |  2.00 +/- 1.00  | 10.00 +/- 10.00 |
| XXX coordinates and external client does whatever(20) |  10.00 +/- 5.00 |  6.00 +/- 3.00  |
|        Build internal extensible data model(16)       |  6.00 +/- 4.00  |  3.00 +/- 3.00  |
|                    App Framework(6)                   |  10.00 +/- 5.00 |  5.00 +/- 10.00 |
|                         3 Tier                        |  5.00 +/- 5.00  |  5.00 +/- 5.00  |
+-------------------------------------------------------+-----------------+-----------------+
```

### Cluster 9
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |  4.0   |  0  |
|     costs     |  48.0  | 6.0 |
|    benefits   |  73.0  | 1.0 |
| decisions_set |  17.0  |  0  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+----------------+----------------+
|                          Node                         |      Cost      |    Benefit     |
+-------------------------------------------------------+----------------+----------------+
|                    Data Service(7)                    | 6.00 +/- 3.00  | 5.00 +/- 5.00  |
|                     Pnp Framework                     | 5.00 +/- 5.00  | 5.00 +/- 10.00 |
|                      New Database                     | 6.00 +/- 6.00  | 10.00 +/- 0.00 |
|       Provide logical data scheme internally(8)       | 6.00 +/- 3.00  | 3.00 +/- 6.00  |
|        External data model can be extended(19)        | 4.00 +/- 8.00  | 5.00 +/- 10.00 |
|       Svc layer w/ extracted biz logic in DB(12)      | 6.00 +/- 3.00  | 5.00 +/- 5.00  |
|          Svc layer w/ extracted biz logic(13)         | 10.00 +/- 5.00 | 3.00 +/- 6.00  |
|   External clients get exactly what they request(10)  | 4.00 +/- 8.00  | 6.00 +/- 0.00  |
| XXX coordinates and internal client does whatever(17) | 3.00 +/- 3.00  | 6.00 +/- 0.00  |
|                    Regression Test                    | 3.00 +/- 3.00  | 5.00 +/- 10.00 |
|       Define data model for all shared data(15)       | 3.00 +/- 6.00  | 6.00 +/- 0.00  |
|                     Documentation                     | 6.00 +/- 3.00  | 5.00 +/- 5.00  |
|                         2 Tier                        | 5.00 +/- 5.00  | 5.00 +/- 10.00 |
|           Define ext mandatory data std(18)           | 3.00 +/- 6.00  | 5.00 +/- 10.00 |
|                      Monitor(11)                      | 2.00 +/- 1.00  | 5.00 +/- 10.00 |
| XXX coordinates and external client does whatever(20) | 10.00 +/- 0.00 | 3.00 +/- 6.00  |
|        Build internal extensible data model(16)       | 2.00 +/- 4.00  | 3.00 +/- 3.00  |
|                    App Framework(6)                   | 5.00 +/- 10.00 | 5.00 +/- 10.00 |
|                         3 Tier                        | 10.00 +/- 0.00 | 5.00 +/- 10.00 |
+-------------------------------------------------------+----------------+----------------+
```

### Cluster 10
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |   4    |  0  |
|     costs     |  51.0  | 3.0 |
|    benefits   |  73.0  | 4.0 |
| decisions_set |   19   |  1  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+-----------------+-----------------+
|                          Node                         |       Cost      |     Benefit     |
+-------------------------------------------------------+-----------------+-----------------+
|                    Data Service(7)                    |  9.00 +/- 6.00  |  10.00 +/- 5.00 |
|                     Pnp Framework                     |  10.00 +/- 0.00 |  5.00 +/- 5.00  |
|                      New Database                     | 18.00 +/- 12.00 |  10.00 +/- 5.00 |
|       Provide logical data scheme internally(8)       |  6.00 +/- 6.00  |  6.00 +/- 6.00  |
|        External data model can be extended(19)        |  4.00 +/- 8.00  |  15.00 +/- 5.00 |
|       Svc layer w/ extracted biz logic in DB(12)      |  6.00 +/- 3.00  |  10.00 +/- 5.00 |
|          Svc layer w/ extracted biz logic(13)         | 15.00 +/- 10.00 |  6.00 +/- 3.00  |
|   External clients get exactly what they request(10)  |  12.00 +/- 4.00 |  6.00 +/- 3.00  |
| XXX coordinates and internal client does whatever(17) |  6.00 +/- 6.00  |  9.00 +/- 6.00  |
|                    Regression Test                    |  6.00 +/- 0.00  |  5.00 +/- 5.00  |
|       Define data model for all shared data(15)       |  6.00 +/- 3.00  |  9.00 +/- 6.00  |
|                     Documentation                     |  6.00 +/- 3.00  |  10.00 +/- 5.00 |
|                         2 Tier                        |  15.00 +/- 5.00 | 15.00 +/- 10.00 |
|           Define ext mandatory data std(18)           |  6.00 +/- 6.00  |  10.00 +/- 0.00 |
|                      Monitor(11)                      |  3.00 +/- 2.00  |  5.00 +/- 5.00  |
| XXX coordinates and external client does whatever(20) | 10.00 +/- 10.00 |  6.00 +/- 3.00  |
|        Build internal extensible data model(16)       |  2.00 +/- 2.00  |  6.00 +/- 6.00  |
|                    App Framework(6)                   |  10.00 +/- 5.00 |  10.00 +/- 5.00 |
|                         3 Tier                        | 10.00 +/- 10.00 | 10.00 +/- 10.00 |
+-------------------------------------------------------+-----------------+-----------------+
```

### Cluster 11
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |  4.0   |  0   |
|     costs     |  41.0  | 5.0  |
|    benefits   |  72.0  | 11.0 |
| decisions_set |  20.0  |  1   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+----------------+----------------+
|                          Node                         |      Cost      |    Benefit     |
+-------------------------------------------------------+----------------+----------------+
|                    Data Service(7)                    | 3.00 +/- 3.00  | 5.00 +/- 5.00  |
|                     Pnp Framework                     | 10.00 +/- 5.00 | 5.00 +/- 5.00  |
|                      New Database                     | 12.00 +/- 6.00 | 10.00 +/- 5.00 |
|       Provide logical data scheme internally(8)       | 3.00 +/- 6.00  | 6.00 +/- 3.00  |
|        External data model can be extended(19)        | 4.00 +/- 4.00  | 10.00 +/- 0.00 |
|       Svc layer w/ extracted biz logic in DB(12)      | 3.00 +/- 6.00  | 5.00 +/- 10.00 |
|          Svc layer w/ extracted biz logic(13)         | 10.00 +/- 0.00 | 3.00 +/- 6.00  |
|   External clients get exactly what they request(10)  | 4.00 +/- 8.00  | 3.00 +/- 6.00  |
| XXX coordinates and internal client does whatever(17) | 3.00 +/- 6.00  | 3.00 +/- 6.00  |
|                    Regression Test                    | 3.00 +/- 6.00  | 10.00 +/- 5.00 |
|       Define data model for all shared data(15)       | 6.00 +/- 3.00  | 6.00 +/- 3.00  |
|                     Documentation                     | 3.00 +/- 3.00  | 5.00 +/- 5.00  |
|                         2 Tier                        | 5.00 +/- 5.00  | 5.00 +/- 10.00 |
|           Define ext mandatory data std(18)           | 3.00 +/- 3.00  | 5.00 +/- 10.00 |
|                      Monitor(11)                      | 1.00 +/- 2.00  | 5.00 +/- 10.00 |
| XXX coordinates and external client does whatever(20) | 10.00 +/- 5.00 | 6.00 +/- 3.00  |
|        Build internal extensible data model(16)       | 2.00 +/- 4.00  | 3.00 +/- 3.00  |
|                    App Framework(6)                   | 5.00 +/- 5.00  | 10.00 +/- 5.00 |
|                         3 Tier                        | 10.00 +/- 0.00 | 5.00 +/- 10.00 |
+-------------------------------------------------------+----------------+----------------+
```

### Cluster 12
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |   4    |  0   |
|     costs     |  48.0  | 4.0  |
|    benefits   |  74.0  | 10.0 |
| decisions_set |   19   |  3   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+-----------------+-----------------+
|                          Node                         |       Cost      |     Benefit     |
+-------------------------------------------------------+-----------------+-----------------+
|                    Data Service(7)                    |  6.00 +/- 6.00  |  5.00 +/- 5.00  |
|                     Pnp Framework                     |  10.00 +/- 5.00 |  10.00 +/- 5.00 |
|                      New Database                     | 12.00 +/- 12.00 | 10.00 +/- 10.00 |
|       Provide logical data scheme internally(8)       |  6.00 +/- 3.00  |  9.00 +/- 3.00  |
|        External data model can be extended(19)        |  8.00 +/- 8.00  | 10.00 +/- 10.00 |
|       Svc layer w/ extracted biz logic in DB(12)      |  6.00 +/- 3.00  |  10.00 +/- 5.00 |
|          Svc layer w/ extracted biz logic(13)         |  5.00 +/- 5.00  |  6.00 +/- 6.00  |
|   External clients get exactly what they request(10)  |  8.00 +/- 8.00  |  6.00 +/- 3.00  |
| XXX coordinates and internal client does whatever(17) |  6.00 +/- 6.00  |  6.00 +/- 3.00  |
|                    Regression Test                    |  6.00 +/- 6.00  |  5.00 +/- 5.00  |
|       Define data model for all shared data(15)       |  6.00 +/- 3.00  |  6.00 +/- 3.00  |
|                     Documentation                     |  6.00 +/- 3.00  |  5.00 +/- 10.00 |
|                         2 Tier                        |  10.00 +/- 5.00 |  5.00 +/- 10.00 |
|           Define ext mandatory data std(18)           |  9.00 +/- 6.00  |  10.00 +/- 5.00 |
|                      Monitor(11)                      |  2.00 +/- 1.00  | 10.00 +/- 10.00 |
| XXX coordinates and external client does whatever(20) |  10.00 +/- 0.00 |  9.00 +/- 6.00  |
|        Build internal extensible data model(16)       |  2.00 +/- 4.00  |  9.00 +/- 3.00  |
|                    App Framework(6)                   |  5.00 +/- 5.00  |  10.00 +/- 5.00 |
|                         3 Tier                        |  15.00 +/- 5.00 | 10.00 +/- 10.00 |
+-------------------------------------------------------+-----------------+-----------------+
```

### Cluster 13
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |  4.0   |  0  |
|     costs     |  43.0  | 3.0 |
|    benefits   |  80.0  | 4.0 |
| decisions_set |  17.0  |  1  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+----------------+----------------+
|                          Node                         |      Cost      |    Benefit     |
+-------------------------------------------------------+----------------+----------------+
|                    Data Service(7)                    | 3.00 +/- 3.00  | 5.00 +/- 10.00 |
|                     Pnp Framework                     | 5.00 +/- 10.00 | 5.00 +/- 10.00 |
|                      New Database                     | 6.00 +/- 6.00  | 7.50 +/- 5.00  |
|       Provide logical data scheme internally(8)       | 6.00 +/- 3.00  | 3.00 +/- 6.00  |
|        External data model can be extended(19)        | 4.00 +/- 8.00  | 5.00 +/- 10.00 |
|       Svc layer w/ extracted biz logic in DB(12)      | 3.00 +/- 6.00  | 5.00 +/- 5.00  |
|          Svc layer w/ extracted biz logic(13)         | 7.50 +/- 5.00  | 3.00 +/- 6.00  |
|   External clients get exactly what they request(10)  | 6.00 +/- 4.00  | 3.00 +/- 3.00  |
| XXX coordinates and internal client does whatever(17) | 3.00 +/- 3.00  | 6.00 +/- 3.00  |
|                    Regression Test                    | 3.00 +/- 3.00  | 10.00 +/- 5.00 |
|       Define data model for all shared data(15)       | 3.00 +/- 6.00  | 3.00 +/- 3.00  |
|                     Documentation                     | 3.00 +/- 6.00  | 5.00 +/- 10.00 |
|                         2 Tier                        | 5.00 +/- 10.00 | 10.00 +/- 5.00 |
|           Define ext mandatory data std(18)           | 6.00 +/- 3.00  | 5.00 +/- 0.00  |
|                      Monitor(11)                      | 1.00 +/- 2.00  | 5.00 +/- 10.00 |
| XXX coordinates and external client does whatever(20) | 5.00 +/- 5.00  | 6.00 +/- 0.00  |
|        Build internal extensible data model(16)       | 4.00 +/- 0.00  | 3.00 +/- 6.00  |
|                    App Framework(6)                   | 5.00 +/- 10.00 | 5.00 +/- 10.00 |
|                         3 Tier                        | 10.00 +/- 5.00 | 5.00 +/- 10.00 |
+-------------------------------------------------------+----------------+----------------+
```

### Cluster 14
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |   4    |  0  |
|     costs     |  48.0  | 2.0 |
|    benefits   |  84.0  | 5.0 |
| decisions_set |   17   |  1  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+-----------------+-----------------+
|                          Node                         |       Cost      |     Benefit     |
+-------------------------------------------------------+-----------------+-----------------+
|                    Data Service(7)                    |  6.00 +/- 3.00  | 10.00 +/- 10.00 |
|                     Pnp Framework                     | 10.00 +/- 10.00 |  10.00 +/- 5.00 |
|                      New Database                     |  18.00 +/- 6.00 | 10.00 +/- 10.00 |
|       Provide logical data scheme internally(8)       |  9.00 +/- 6.00  |  9.00 +/- 3.00  |
|        External data model can be extended(19)        |  4.00 +/- 4.00  |  5.00 +/- 10.00 |
|       Svc layer w/ extracted biz logic in DB(12)      |  9.00 +/- 6.00  |  15.00 +/- 5.00 |
|          Svc layer w/ extracted biz logic(13)         |  10.00 +/- 5.00 |  6.00 +/- 3.00  |
|   External clients get exactly what they request(10)  |  8.00 +/- 4.00  |  6.00 +/- 3.00  |
| XXX coordinates and internal client does whatever(17) |  6.00 +/- 3.00  |  9.00 +/- 6.00  |
|                    Regression Test                    |  6.00 +/- 3.00  |  15.00 +/- 5.00 |
|       Define data model for all shared data(15)       |  3.00 +/- 6.00  |  9.00 +/- 3.00  |
|                     Documentation                     |  6.00 +/- 6.00  |  10.00 +/- 5.00 |
|                         2 Tier                        |  5.00 +/- 5.00  | 10.00 +/- 10.00 |
|           Define ext mandatory data std(18)           |  6.00 +/- 6.00  | 10.00 +/- 10.00 |
|                      Monitor(11)                      |  2.00 +/- 0.00  | 10.00 +/- 10.00 |
| XXX coordinates and external client does whatever(20) | 15.00 +/- 10.00 |  6.00 +/- 3.00  |
|        Build internal extensible data model(16)       |  4.00 +/- 2.00  |  6.00 +/- 3.00  |
|                    App Framework(6)                   | 10.00 +/- 10.00 | 10.00 +/- 10.00 |
|                         3 Tier                        |  15.00 +/- 0.00 |  15.00 +/- 5.00 |
+-------------------------------------------------------+-----------------+-----------------+
```

### Cluster 15
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |  4.0   |  0   |
|     costs     |  45.5  | 2.0  |
|    benefits   |  83.0  | 13.0 |
| decisions_set |  18.5  |  0   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+----------------+----------------+
|                          Node                         |      Cost      |    Benefit     |
+-------------------------------------------------------+----------------+----------------+
|                    Data Service(7)                    | 3.00 +/- 6.00  | 10.00 +/- 5.00 |
|                     Pnp Framework                     | 10.00 +/- 5.00 | 10.00 +/- 5.00 |
|                      New Database                     | 6.00 +/- 12.00 | 10.00 +/- 5.00 |
|       Provide logical data scheme internally(8)       | 3.00 +/- 3.00  | 4.50 +/- 3.00  |
|        External data model can be extended(19)        | 8.00 +/- 4.00  | 5.00 +/- 10.00 |
|       Svc layer w/ extracted biz logic in DB(12)      | 3.00 +/- 6.00  | 5.00 +/- 10.00 |
|          Svc layer w/ extracted biz logic(13)         | 5.00 +/- 10.00 | 3.00 +/- 6.00  |
|   External clients get exactly what they request(10)  | 8.00 +/- 4.00  | 3.00 +/- 6.00  |
| XXX coordinates and internal client does whatever(17) | 3.00 +/- 6.00  | 3.00 +/- 6.00  |
|                    Regression Test                    | 4.50 +/- 3.00  | 5.00 +/- 5.00  |
|       Define data model for all shared data(15)       | 3.00 +/- 6.00  | 7.50 +/- 0.00  |
|                     Documentation                     | 3.00 +/- 3.00  | 5.00 +/- 10.00 |
|                         2 Tier                        | 7.50 +/- 0.00  | 5.00 +/- 10.00 |
|           Define ext mandatory data std(18)           | 3.00 +/- 3.00  | 7.50 +/- 5.00  |
|                      Monitor(11)                      | 2.00 +/- 0.00  | 10.00 +/- 0.00 |
| XXX coordinates and external client does whatever(20) | 7.50 +/- 5.00  | 3.00 +/- 3.00  |
|        Build internal extensible data model(16)       | 2.00 +/- 4.00  | 3.00 +/- 6.00  |
|                    App Framework(6)                   | 5.00 +/- 5.00  | 5.00 +/- 10.00 |
|                         3 Tier                        | 5.00 +/- 5.00  | 10.00 +/- 5.00 |
+-------------------------------------------------------+----------------+----------------+
```

### Cluster 16
#### Measures
```
+---------------+--------+-----+
|    measure    | median | iqr |
+---------------+--------+-----+
|   softgoals   |   4    |  0  |
|     costs     |  52.0  | 2.0 |
|    benefits   |  89.0  | 5.0 |
| decisions_set |   18   |  1  |
+---------------+--------+-----+
```
#### Nodes
```
+-------------------------------------------------------+-----------------+-----------------+
|                          Node                         |       Cost      |     Benefit     |
+-------------------------------------------------------+-----------------+-----------------+
|                    Data Service(7)                    |  9.00 +/- 3.00  |  10.00 +/- 5.00 |
|                     Pnp Framework                     |  10.00 +/- 5.00 | 15.00 +/- 10.00 |
|                      New Database                     |  6.00 +/- 6.00  | 10.00 +/- 10.00 |
|       Provide logical data scheme internally(8)       |  6.00 +/- 6.00  |  6.00 +/- 3.00  |
|        External data model can be extended(19)        |  12.00 +/- 8.00 |  10.00 +/- 5.00 |
|       Svc layer w/ extracted biz logic in DB(12)      |  9.00 +/- 3.00  |  10.00 +/- 5.00 |
|          Svc layer w/ extracted biz logic(13)         |  15.00 +/- 5.00 |  9.00 +/- 3.00  |
|   External clients get exactly what they request(10)  |  8.00 +/- 4.00  |  6.00 +/- 6.00  |
| XXX coordinates and internal client does whatever(17) |  6.00 +/- 6.00  |  6.00 +/- 6.00  |
|                    Regression Test                    |  6.00 +/- 6.00  | 15.00 +/- 10.00 |
|       Define data model for all shared data(15)       |  6.00 +/- 6.00  |  6.00 +/- 6.00  |
|                     Documentation                     |  3.00 +/- 6.00  |  10.00 +/- 5.00 |
|                         2 Tier                        |  10.00 +/- 5.00 |  15.00 +/- 5.00 |
|           Define ext mandatory data std(18)           |  3.00 +/- 3.00  |  10.00 +/- 5.00 |
|                      Monitor(11)                      |  3.00 +/- 2.00  | 15.00 +/- 10.00 |
| XXX coordinates and external client does whatever(20) |  10.00 +/- 5.00 |  6.00 +/- 6.00  |
|        Build internal extensible data model(16)       |  2.00 +/- 2.00  |  6.00 +/- 3.00  |
|                    App Framework(6)                   |  5.00 +/- 5.00  |  15.00 +/- 5.00 |
|                         3 Tier                        | 15.00 +/- 10.00 |  10.00 +/- 5.00 |
+-------------------------------------------------------+-----------------+-----------------+
```

