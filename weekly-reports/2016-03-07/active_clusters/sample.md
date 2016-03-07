### Cluster 1
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |  4.0   |  0   |
|     costs     | 34.84  | 2.2  |
|    benefits   | 55.26  | 2.05 |
| decisions_set |  18.0  |  1   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 3.69 +/- 0.82 | 6.43 +/- 1.05 |
|                     Pnp Framework                     | 6.62 +/- 1.02 | 6.90 +/- 1.91 |
|                      New Database                     | 7.50 +/- 2.12 | 7.61 +/- 1.12 |
|       Provide logical data scheme internally(8)       | 3.93 +/- 0.89 | 3.75 +/- 1.15 |
|        External data model can be extended(19)        | 4.53 +/- 1.85 | 5.95 +/- 3.54 |
|       Svc layer w/ extracted biz logic in DB(12)      | 3.62 +/- 0.90 | 7.24 +/- 0.71 |
|          Svc layer w/ extracted biz logic(13)         | 7.01 +/- 1.68 | 4.46 +/- 0.64 |
|   External clients get exactly what they request(10)  | 4.82 +/- 1.23 | 4.23 +/- 0.79 |
| XXX coordinates and internal client does whatever(17) | 4.36 +/- 1.15 | 4.12 +/- 0.63 |
|                    Regression Test                    | 3.71 +/- 1.55 | 6.52 +/- 1.26 |
|       Define data model for all shared data(15)       | 3.90 +/- 1.08 | 4.01 +/- 1.08 |
|                     Documentation                     | 4.54 +/- 0.67 | 6.83 +/- 1.40 |
|                         2 Tier                        | 6.57 +/- 1.73 | 6.16 +/- 3.28 |
|           Define ext mandatory data std(18)           | 3.95 +/- 1.04 | 7.40 +/- 0.92 |
|                      Monitor(11)                      | 1.33 +/- 0.42 | 7.26 +/- 1.04 |
| XXX coordinates and external client does whatever(20) | 7.02 +/- 1.07 | 3.79 +/- 1.42 |
|        Build internal extensible data model(16)       | 2.69 +/- 0.51 | 3.29 +/- 1.78 |
|                    App Framework(6)                   | 6.88 +/- 0.53 | 6.77 +/- 1.07 |
|                         3 Tier                        | 7.16 +/- 1.54 | 6.64 +/- 1.41 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 2
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |   4    |  0   |
|     costs     | 35.04  | 2.24 |
|    benefits   | 57.67  | 1.88 |
| decisions_set |   17   |  1   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.56 +/- 0.43 | 7.71 +/- 1.14 |
|                     Pnp Framework                     | 7.87 +/- 1.80 | 7.74 +/- 1.25 |
|                      New Database                     | 8.93 +/- 3.71 | 7.14 +/- 1.82 |
|       Provide logical data scheme internally(8)       | 4.49 +/- 0.75 | 4.63 +/- 1.15 |
|        External data model can be extended(19)        | 5.94 +/- 1.21 | 6.94 +/- 0.92 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.64 +/- 0.51 | 7.34 +/- 1.22 |
|          Svc layer w/ extracted biz logic(13)         | 7.47 +/- 1.91 | 4.09 +/- 1.19 |
|   External clients get exactly what they request(10)  | 6.15 +/- 0.58 | 4.10 +/- 1.19 |
| XXX coordinates and internal client does whatever(17) | 4.30 +/- 1.64 | 4.17 +/- 1.17 |
|                    Regression Test                    | 4.19 +/- 1.00 | 7.42 +/- 1.39 |
|       Define data model for all shared data(15)       | 4.65 +/- 0.85 | 4.88 +/- 1.03 |
|                     Documentation                     | 4.60 +/- 0.64 | 8.24 +/- 0.83 |
|                         2 Tier                        | 7.28 +/- 1.39 | 7.73 +/- 1.52 |
|           Define ext mandatory data std(18)           | 5.12 +/- 0.33 | 7.75 +/- 0.80 |
|                      Monitor(11)                      | 1.49 +/- 0.16 | 8.57 +/- 0.75 |
| XXX coordinates and external client does whatever(20) | 7.73 +/- 1.75 | 4.14 +/- 1.07 |
|        Build internal extensible data model(16)       | 2.70 +/- 0.33 | 4.89 +/- 1.49 |
|                    App Framework(6)                   | 6.56 +/- 0.55 | 7.52 +/- 2.17 |
|                         3 Tier                        | 8.53 +/- 1.96 | 7.05 +/- 2.27 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 3
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |  4.0   |  0   |
|     costs     | 37.49  | 1.59 |
|    benefits   | 54.41  | 5.93 |
| decisions_set |  16.0  |  1   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.09 +/- 0.52 | 6.12 +/- 1.71 |
|                     Pnp Framework                     | 6.96 +/- 1.87 | 6.97 +/- 0.74 |
|                      New Database                     | 8.66 +/- 0.77 | 7.16 +/- 1.64 |
|       Provide logical data scheme internally(8)       | 3.99 +/- 0.69 | 3.61 +/- 0.96 |
|        External data model can be extended(19)        | 5.65 +/- 1.19 | 6.33 +/- 2.20 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.08 +/- 0.66 | 7.64 +/- 1.34 |
|          Svc layer w/ extracted biz logic(13)         | 7.19 +/- 1.02 | 3.32 +/- 1.59 |
|   External clients get exactly what they request(10)  | 4.79 +/- 1.41 | 4.49 +/- 0.86 |
| XXX coordinates and internal client does whatever(17) | 4.17 +/- 0.78 | 4.07 +/- 0.81 |
|                    Regression Test                    | 4.22 +/- 0.78 | 7.44 +/- 0.32 |
|       Define data model for all shared data(15)       | 3.92 +/- 0.71 | 3.97 +/- 0.90 |
|                     Documentation                     | 3.69 +/- 1.43 | 6.48 +/- 1.37 |
|                         2 Tier                        | 6.47 +/- 0.62 | 7.12 +/- 0.60 |
|           Define ext mandatory data std(18)           | 4.16 +/- 1.27 | 7.18 +/- 1.62 |
|                      Monitor(11)                      | 1.46 +/- 0.24 | 7.08 +/- 0.63 |
| XXX coordinates and external client does whatever(20) | 7.85 +/- 0.39 | 4.17 +/- 1.05 |
|        Build internal extensible data model(16)       | 2.87 +/- 0.75 | 4.33 +/- 1.03 |
|                    App Framework(6)                   | 6.58 +/- 2.24 | 7.36 +/- 0.50 |
|                         3 Tier                        | 6.07 +/- 1.51 | 6.95 +/- 1.48 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 4
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |   4    |  0   |
|     costs     | 39.93  | 2.13 |
|    benefits   | 58.96  | 4.65 |
| decisions_set |   15   |  1   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 5.54 +/- 1.40 | 7.40 +/- 0.43 |
|                     Pnp Framework                     | 8.17 +/- 0.61 | 7.49 +/- 1.92 |
|                      New Database                     | 8.96 +/- 0.38 | 7.58 +/- 2.34 |
|       Provide logical data scheme internally(8)       | 4.93 +/- 1.08 | 4.79 +/- 1.54 |
|        External data model can be extended(19)        | 6.00 +/- 0.68 | 7.73 +/- 1.99 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.16 +/- 1.26 | 8.19 +/- 0.89 |
|          Svc layer w/ extracted biz logic(13)         | 7.81 +/- 2.06 | 4.25 +/- 0.40 |
|   External clients get exactly what they request(10)  | 6.29 +/- 0.97 | 4.75 +/- 0.65 |
| XXX coordinates and internal client does whatever(17) | 4.46 +/- 0.34 | 4.09 +/- 0.11 |
|                    Regression Test                    | 4.30 +/- 1.40 | 7.32 +/- 2.13 |
|       Define data model for all shared data(15)       | 4.47 +/- 0.78 | 4.06 +/- 0.87 |
|                     Documentation                     | 4.53 +/- 0.80 | 7.70 +/- 1.52 |
|                         2 Tier                        | 7.52 +/- 1.50 | 7.59 +/- 0.76 |
|           Define ext mandatory data std(18)           | 4.62 +/- 0.39 | 7.08 +/- 1.14 |
|                      Monitor(11)                      | 1.69 +/- 0.38 | 6.89 +/- 1.07 |
| XXX coordinates and external client does whatever(20) | 7.28 +/- 3.07 | 4.84 +/- 0.97 |
|        Build internal extensible data model(16)       | 3.10 +/- 0.56 | 4.30 +/- 1.02 |
|                    App Framework(6)                   | 7.10 +/- 1.17 | 7.06 +/- 2.24 |
|                         3 Tier                        | 6.51 +/- 1.74 | 7.55 +/- 2.36 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 5
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |  0.0   |  0   |
|     costs     |  5.88  | 0.53 |
|    benefits   |  7.78  | 1.28 |
| decisions_set |  2.0   |  0   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.37 +/- 0.66 | 6.82 +/- 0.72 |
|                     Pnp Framework                     | 5.88 +/- 0.53 | 7.78 +/- 1.28 |
|                      New Database                     | 8.30 +/- 2.62 | 6.21 +/- 1.55 |
|       Provide logical data scheme internally(8)       | 4.38 +/- 0.84 | 3.65 +/- 1.11 |
|        External data model can be extended(19)        | 5.85 +/- 0.62 | 7.04 +/- 0.59 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.02 +/- 0.77 | 7.20 +/- 0.48 |
|          Svc layer w/ extracted biz logic(13)         | 6.36 +/- 1.92 | 4.08 +/- 0.35 |
|   External clients get exactly what they request(10)  | 5.16 +/- 0.88 | 3.95 +/- 0.67 |
| XXX coordinates and internal client does whatever(17) | 4.55 +/- 0.37 | 3.78 +/- 0.66 |
|                    Regression Test                    | 4.17 +/- 0.39 | 6.53 +/- 0.37 |
|       Define data model for all shared data(15)       | 4.12 +/- 0.85 | 3.83 +/- 1.48 |
|                     Documentation                     | 4.34 +/- 0.54 | 7.32 +/- 1.16 |
|                         2 Tier                        | 6.05 +/- 2.22 | 6.64 +/- 1.29 |
|           Define ext mandatory data std(18)           | 3.91 +/- 1.85 | 7.07 +/- 0.89 |
|                      Monitor(11)                      | 1.22 +/- 0.50 | 7.27 +/- 0.49 |
| XXX coordinates and external client does whatever(20) | 7.10 +/- 2.27 | 3.58 +/- 0.64 |
|        Build internal extensible data model(16)       | 2.35 +/- 0.51 | 4.46 +/- 0.52 |
|                    App Framework(6)                   | 7.37 +/- 1.20 | 6.36 +/- 2.86 |
|                         3 Tier                        | 6.23 +/- 1.88 | 6.64 +/- 1.18 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 6
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |   0    |  0   |
|     costs     |  7.1   | 1.06 |
|    benefits   |  6.82  | 0.84 |
| decisions_set |   2    |  0   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.52 +/- 0.91 | 7.06 +/- 1.47 |
|                     Pnp Framework                     | 7.10 +/- 1.06 | 6.82 +/- 0.84 |
|                      New Database                     | 8.85 +/- 2.68 | 6.21 +/- 0.77 |
|       Provide logical data scheme internally(8)       | 4.79 +/- 0.49 | 4.38 +/- 0.40 |
|        External data model can be extended(19)        | 5.77 +/- 0.77 | 7.58 +/- 1.60 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.43 +/- 1.35 | 6.95 +/- 0.82 |
|          Svc layer w/ extracted biz logic(13)         | 7.99 +/- 1.90 | 4.82 +/- 0.75 |
|   External clients get exactly what they request(10)  | 6.71 +/- 1.02 | 4.68 +/- 0.87 |
| XXX coordinates and internal client does whatever(17) | 4.97 +/- 0.43 | 4.12 +/- 1.17 |
|                    Regression Test                    | 4.17 +/- 0.55 | 8.04 +/- 0.81 |
|       Define data model for all shared data(15)       | 4.54 +/- 0.38 | 4.75 +/- 0.47 |
|                     Documentation                     | 5.00 +/- 0.22 | 8.11 +/- 0.91 |
|                         2 Tier                        | 6.67 +/- 1.15 | 8.17 +/- 1.14 |
|           Define ext mandatory data std(18)           | 4.01 +/- 0.66 | 7.96 +/- 0.91 |
|                      Monitor(11)                      | 1.50 +/- 0.23 | 7.42 +/- 2.73 |
| XXX coordinates and external client does whatever(20) | 7.58 +/- 0.39 | 4.12 +/- 1.01 |
|        Build internal extensible data model(16)       | 3.20 +/- 0.50 | 4.37 +/- 0.58 |
|                    App Framework(6)                   | 8.23 +/- 1.29 | 6.92 +/- 1.77 |
|                         3 Tier                        | 7.43 +/- 1.29 | 6.71 +/- 1.84 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 7
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |  0.0   |  0   |
|     costs     | 6.915  | 0.91 |
|    benefits   | 8.315  | 0.78 |
| decisions_set |  2.0   |  0   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.19 +/- 0.29 | 7.54 +/- 1.70 |
|                     Pnp Framework                     | 7.01 +/- 0.71 | 7.84 +/- 1.26 |
|                      New Database                     | 7.30 +/- 1.93 | 7.05 +/- 0.66 |
|       Provide logical data scheme internally(8)       | 4.27 +/- 0.68 | 4.10 +/- 0.65 |
|        External data model can be extended(19)        | 5.68 +/- 1.73 | 6.91 +/- 1.69 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.36 +/- 0.34 | 7.30 +/- 1.84 |
|          Svc layer w/ extracted biz logic(13)         | 7.15 +/- 0.77 | 4.47 +/- 0.37 |
|   External clients get exactly what they request(10)  | 5.31 +/- 1.94 | 4.23 +/- 0.84 |
| XXX coordinates and internal client does whatever(17) | 3.74 +/- 0.71 | 4.32 +/- 1.03 |
|                    Regression Test                    | 3.87 +/- 0.86 | 7.16 +/- 0.79 |
|       Define data model for all shared data(15)       | 4.30 +/- 0.84 | 3.29 +/- 2.08 |
|                     Documentation                     | 4.00 +/- 1.02 | 6.11 +/- 1.76 |
|                         2 Tier                        | 6.60 +/- 0.99 | 6.23 +/- 1.36 |
|           Define ext mandatory data std(18)           | 3.91 +/- 1.02 | 7.49 +/- 1.45 |
|                      Monitor(11)                      | 1.55 +/- 0.26 | 5.66 +/- 2.15 |
| XXX coordinates and external client does whatever(20) | 7.07 +/- 0.56 | 3.87 +/- 0.54 |
|        Build internal extensible data model(16)       | 2.47 +/- 0.48 | 4.46 +/- 0.54 |
|                    App Framework(6)                   | 7.03 +/- 1.75 | 7.06 +/- 1.56 |
|                         3 Tier                        | 6.43 +/- 0.87 | 6.85 +/- 1.34 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 8
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |   0    |  0   |
|     costs     |  8.71  | 1.64 |
|    benefits   |  8.72  | 0.91 |
| decisions_set |   2    |  0   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.57 +/- 0.76 | 7.77 +/- 1.39 |
|                     Pnp Framework                     | 8.24 +/- 1.01 | 8.60 +/- 0.70 |
|                      New Database                     | 9.12 +/- 1.88 | 6.81 +/- 1.46 |
|       Provide logical data scheme internally(8)       | 5.04 +/- 0.73 | 4.33 +/- 0.61 |
|        External data model can be extended(19)        | 5.50 +/- 1.61 | 6.33 +/- 1.00 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.34 +/- 0.53 | 7.38 +/- 1.00 |
|          Svc layer w/ extracted biz logic(13)         | 7.28 +/- 1.35 | 5.03 +/- 0.19 |
|   External clients get exactly what they request(10)  | 6.08 +/- 1.29 | 4.54 +/- 0.81 |
| XXX coordinates and internal client does whatever(17) | 4.47 +/- 0.19 | 4.25 +/- 0.72 |
|                    Regression Test                    | 4.50 +/- 0.87 | 7.78 +/- 1.81 |
|       Define data model for all shared data(15)       | 4.14 +/- 0.49 | 4.42 +/- 0.66 |
|                     Documentation                     | 4.00 +/- 1.52 | 6.62 +/- 1.02 |
|                         2 Tier                        | 8.04 +/- 1.20 | 7.62 +/- 2.09 |
|           Define ext mandatory data std(18)           | 4.34 +/- 0.83 | 8.03 +/- 2.74 |
|                      Monitor(11)                      | 1.42 +/- 0.18 | 8.16 +/- 1.51 |
| XXX coordinates and external client does whatever(20) | 7.61 +/- 1.41 | 4.15 +/- 0.96 |
|        Build internal extensible data model(16)       | 2.83 +/- 0.57 | 4.40 +/- 0.97 |
|                    App Framework(6)                   | 8.13 +/- 1.62 | 7.11 +/- 1.24 |
|                         3 Tier                        | 6.39 +/- 1.17 | 7.47 +/- 1.65 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 9
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |  4.0   |  0   |
|     costs     | 34.62  | 1.31 |
|    benefits   | 54.67  | 5.7  |
| decisions_set |  20.0  |  1   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 3.71 +/- 0.60 | 6.24 +/- 1.24 |
|                     Pnp Framework                     | 7.67 +/- 0.90 | 6.72 +/- 1.00 |
|                      New Database                     | 7.23 +/- 1.73 | 6.74 +/- 2.26 |
|       Provide logical data scheme internally(8)       | 3.78 +/- 1.46 | 3.49 +/- 1.11 |
|        External data model can be extended(19)        | 5.49 +/- 0.40 | 6.44 +/- 1.12 |
|       Svc layer w/ extracted biz logic in DB(12)      | 3.94 +/- 1.00 | 8.04 +/- 1.43 |
|          Svc layer w/ extracted biz logic(13)         | 7.13 +/- 1.49 | 3.93 +/- 0.82 |
|   External clients get exactly what they request(10)  | 6.00 +/- 0.75 | 4.54 +/- 1.06 |
| XXX coordinates and internal client does whatever(17) | 3.99 +/- 0.64 | 4.30 +/- 0.65 |
|                    Regression Test                    | 3.75 +/- 1.42 | 6.93 +/- 1.18 |
|       Define data model for all shared data(15)       | 4.21 +/- 0.92 | 3.64 +/- 1.02 |
|                     Documentation                     | 4.22 +/- 0.76 | 6.46 +/- 2.18 |
|                         2 Tier                        | 6.30 +/- 0.26 | 6.95 +/- 1.92 |
|           Define ext mandatory data std(18)           | 4.94 +/- 0.51 | 7.36 +/- 1.10 |
|                      Monitor(11)                      | 1.45 +/- 0.40 | 6.23 +/- 1.87 |
| XXX coordinates and external client does whatever(20) | 6.85 +/- 1.51 | 4.40 +/- 0.33 |
|        Build internal extensible data model(16)       | 2.42 +/- 0.33 | 4.17 +/- 1.05 |
|                    App Framework(6)                   | 6.99 +/- 0.93 | 6.33 +/- 1.72 |
|                         3 Tier                        | 6.51 +/- 1.23 | 6.45 +/- 1.53 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 10
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |   4    |  0   |
|     costs     | 37.26  | 0.52 |
|    benefits   | 59.59  | 4.0  |
| decisions_set |   18   |  1   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.27 +/- 0.96 | 7.43 +/- 2.08 |
|                     Pnp Framework                     | 7.47 +/- 0.56 | 7.15 +/- 1.08 |
|                      New Database                     | 8.37 +/- 1.26 | 7.68 +/- 0.95 |
|       Provide logical data scheme internally(8)       | 4.23 +/- 0.63 | 4.67 +/- 0.42 |
|        External data model can be extended(19)        | 5.51 +/- 2.17 | 7.38 +/- 2.46 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.56 +/- 0.40 | 7.03 +/- 2.75 |
|          Svc layer w/ extracted biz logic(13)         | 7.11 +/- 2.25 | 4.21 +/- 1.10 |
|   External clients get exactly what they request(10)  | 5.69 +/- 0.76 | 4.43 +/- 1.22 |
| XXX coordinates and internal client does whatever(17) | 4.53 +/- 1.10 | 4.55 +/- 0.55 |
|                    Regression Test                    | 4.97 +/- 1.03 | 8.32 +/- 1.04 |
|       Define data model for all shared data(15)       | 4.94 +/- 0.48 | 4.35 +/- 1.09 |
|                     Documentation                     | 4.67 +/- 0.41 | 7.75 +/- 0.78 |
|                         2 Tier                        | 6.86 +/- 1.65 | 8.08 +/- 1.14 |
|           Define ext mandatory data std(18)           | 4.49 +/- 0.64 | 6.92 +/- 0.73 |
|                      Monitor(11)                      | 1.30 +/- 0.21 | 7.21 +/- 1.65 |
| XXX coordinates and external client does whatever(20) | 7.73 +/- 0.72 | 4.69 +/- 0.54 |
|        Build internal extensible data model(16)       | 3.02 +/- 0.08 | 4.56 +/- 0.81 |
|                    App Framework(6)                   | 7.50 +/- 1.13 | 7.49 +/- 0.70 |
|                         3 Tier                        | 7.14 +/- 1.11 | 6.73 +/- 1.75 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 11
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |  4.0   |  0   |
|     costs     | 39.32  | 2.08 |
|    benefits   | 59.31  | 4.58 |
| decisions_set |  21.0  |  0   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.57 +/- 0.59 | 7.25 +/- 0.95 |
|                     Pnp Framework                     | 6.74 +/- 0.76 | 6.52 +/- 0.64 |
|                      New Database                     | 7.88 +/- 1.83 | 7.26 +/- 0.28 |
|       Provide logical data scheme internally(8)       | 3.61 +/- 1.03 | 4.14 +/- 0.65 |
|        External data model can be extended(19)        | 4.82 +/- 2.21 | 6.08 +/- 1.92 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.43 +/- 0.51 | 7.09 +/- 0.50 |
|          Svc layer w/ extracted biz logic(13)         | 6.09 +/- 1.41 | 3.86 +/- 0.66 |
|   External clients get exactly what they request(10)  | 5.84 +/- 0.93 | 4.35 +/- 0.64 |
| XXX coordinates and internal client does whatever(17) | 4.12 +/- 1.27 | 4.09 +/- 1.23 |
|                    Regression Test                    | 3.86 +/- 0.80 | 5.91 +/- 1.62 |
|       Define data model for all shared data(15)       | 3.83 +/- 1.16 | 3.64 +/- 0.78 |
|                     Documentation                     | 4.61 +/- 0.76 | 6.84 +/- 0.98 |
|                         2 Tier                        | 7.70 +/- 1.12 | 7.48 +/- 0.90 |
|           Define ext mandatory data std(18)           | 4.10 +/- 0.61 | 7.61 +/- 1.18 |
|                      Monitor(11)                      | 1.46 +/- 0.29 | 6.93 +/- 0.74 |
| XXX coordinates and external client does whatever(20) | 6.92 +/- 1.19 | 4.41 +/- 0.72 |
|        Build internal extensible data model(16)       | 2.97 +/- 0.45 | 4.06 +/- 0.64 |
|                    App Framework(6)                   | 7.43 +/- 1.09 | 6.72 +/- 1.52 |
|                         3 Tier                        | 8.06 +/- 0.18 | 7.56 +/- 0.96 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 12
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |   4    |  0   |
|     costs     |  39.8  | 1.45 |
|    benefits   | 59.75  | 2.29 |
| decisions_set |   19   |  0   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.56 +/- 1.32 | 7.70 +/- 2.38 |
|                     Pnp Framework                     | 7.89 +/- 2.36 | 7.70 +/- 1.45 |
|                      New Database                     | 8.90 +/- 1.72 | 7.81 +/- 1.53 |
|       Provide logical data scheme internally(8)       | 4.23 +/- 0.91 | 4.22 +/- 1.72 |
|        External data model can be extended(19)        | 5.68 +/- 1.18 | 7.91 +/- 2.05 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.66 +/- 1.39 | 7.60 +/- 2.07 |
|          Svc layer w/ extracted biz logic(13)         | 8.10 +/- 1.64 | 4.35 +/- 0.31 |
|   External clients get exactly what they request(10)  | 6.25 +/- 1.30 | 4.24 +/- 0.79 |
| XXX coordinates and internal client does whatever(17) | 4.23 +/- 1.02 | 4.54 +/- 0.51 |
|                    Regression Test                    | 4.99 +/- 0.85 | 7.81 +/- 1.61 |
|       Define data model for all shared data(15)       | 4.73 +/- 0.60 | 3.93 +/- 1.23 |
|                     Documentation                     | 4.84 +/- 0.41 | 7.57 +/- 0.93 |
|                         2 Tier                        | 7.49 +/- 1.80 | 8.06 +/- 0.70 |
|           Define ext mandatory data std(18)           | 4.52 +/- 0.29 | 6.96 +/- 0.94 |
|                      Monitor(11)                      | 1.57 +/- 0.14 | 7.63 +/- 0.59 |
| XXX coordinates and external client does whatever(20) | 6.72 +/- 1.36 | 4.66 +/- 0.97 |
|        Build internal extensible data model(16)       | 2.59 +/- 0.68 | 4.60 +/- 0.62 |
|                    App Framework(6)                   | 8.10 +/- 0.73 | 6.95 +/- 0.77 |
|                         3 Tier                        | 6.34 +/- 2.46 | 8.10 +/- 0.89 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 13
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |  4.0   |  0   |
|     costs     | 38.085 | 2.96 |
|    benefits   | 60.84  | 0.56 |
| decisions_set |  18.0  |  1   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 3.55 +/- 0.94 | 6.84 +/- 1.52 |
|                     Pnp Framework                     | 7.23 +/- 0.64 | 7.38 +/- 1.09 |
|                      New Database                     | 8.36 +/- 1.49 | 7.04 +/- 1.06 |
|       Provide logical data scheme internally(8)       | 4.43 +/- 0.86 | 4.02 +/- 0.70 |
|        External data model can be extended(19)        | 5.69 +/- 1.93 | 7.27 +/- 0.53 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.05 +/- 1.13 | 6.82 +/- 1.06 |
|          Svc layer w/ extracted biz logic(13)         | 7.21 +/- 1.31 | 4.43 +/- 0.80 |
|   External clients get exactly what they request(10)  | 5.51 +/- 1.43 | 4.05 +/- 0.56 |
| XXX coordinates and internal client does whatever(17) | 4.24 +/- 0.88 | 4.54 +/- 0.74 |
|                    Regression Test                    | 3.78 +/- 1.07 | 7.50 +/- 0.98 |
|       Define data model for all shared data(15)       | 4.02 +/- 0.21 | 4.25 +/- 0.44 |
|                     Documentation                     | 3.95 +/- 0.59 | 7.08 +/- 0.78 |
|                         2 Tier                        | 5.78 +/- 2.64 | 6.48 +/- 1.47 |
|           Define ext mandatory data std(18)           | 3.88 +/- 0.83 | 7.00 +/- 1.58 |
|                      Monitor(11)                      | 1.31 +/- 0.21 | 6.16 +/- 1.75 |
| XXX coordinates and external client does whatever(20) | 6.09 +/- 1.18 | 3.74 +/- 1.23 |
|        Build internal extensible data model(16)       | 2.60 +/- 0.69 | 3.92 +/- 0.61 |
|                    App Framework(6)                   | 6.46 +/- 1.10 | 7.37 +/- 0.73 |
|                         3 Tier                        | 7.55 +/- 0.95 | 6.65 +/- 0.81 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 14
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |   4    |  0   |
|     costs     | 42.37  | 1.54 |
|    benefits   | 63.75  | 5.13 |
| decisions_set |   19   |  1   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.31 +/- 0.59 | 7.43 +/- 0.75 |
|                     Pnp Framework                     | 7.67 +/- 1.81 | 7.15 +/- 0.55 |
|                      New Database                     | 9.82 +/- 1.28 | 7.66 +/- 0.99 |
|       Provide logical data scheme internally(8)       | 4.27 +/- 1.43 | 4.91 +/- 0.98 |
|        External data model can be extended(19)        | 6.20 +/- 1.52 | 7.78 +/- 1.97 |
|       Svc layer w/ extracted biz logic in DB(12)      | 5.12 +/- 0.67 | 8.19 +/- 2.14 |
|          Svc layer w/ extracted biz logic(13)         | 7.97 +/- 2.10 | 4.09 +/- 0.28 |
|   External clients get exactly what they request(10)  | 5.61 +/- 1.01 | 4.34 +/- 0.51 |
| XXX coordinates and internal client does whatever(17) | 4.56 +/- 0.65 | 4.94 +/- 0.47 |
|                    Regression Test                    | 4.52 +/- 1.09 | 8.05 +/- 1.18 |
|       Define data model for all shared data(15)       | 3.88 +/- 0.69 | 4.13 +/- 0.60 |
|                     Documentation                     | 4.34 +/- 0.60 | 7.20 +/- 0.72 |
|                         2 Tier                        | 7.54 +/- 1.39 | 8.16 +/- 0.78 |
|           Define ext mandatory data std(18)           | 4.61 +/- 0.33 | 7.49 +/- 1.48 |
|                      Monitor(11)                      | 1.41 +/- 0.42 | 8.19 +/- 1.38 |
| XXX coordinates and external client does whatever(20) | 7.25 +/- 2.30 | 4.11 +/- 1.07 |
|        Build internal extensible data model(16)       | 2.84 +/- 0.23 | 4.75 +/- 0.83 |
|                    App Framework(6)                   | 7.82 +/- 1.22 | 8.14 +/- 0.36 |
|                         3 Tier                        | 7.70 +/- 0.21 | 6.41 +/- 2.47 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 15
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |  4.0   |  0   |
|     costs     | 42.04  | 0.38 |
|    benefits   | 60.55  | 3.86 |
| decisions_set |  15.0  |  2   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.28 +/- 1.05 | 6.65 +/- 1.15 |
|                     Pnp Framework                     | 7.18 +/- 1.49 | 6.65 +/- 1.13 |
|                      New Database                     | 7.34 +/- 1.93 | 6.91 +/- 1.36 |
|       Provide logical data scheme internally(8)       | 4.83 +/- 0.35 | 4.54 +/- 0.67 |
|        External data model can be extended(19)        | 6.53 +/- 0.40 | 6.70 +/- 1.77 |
|       Svc layer w/ extracted biz logic in DB(12)      | 3.85 +/- 0.93 | 6.38 +/- 1.39 |
|          Svc layer w/ extracted biz logic(13)         | 7.11 +/- 2.76 | 3.98 +/- 0.93 |
|   External clients get exactly what they request(10)  | 6.06 +/- 0.45 | 4.02 +/- 0.52 |
| XXX coordinates and internal client does whatever(17) | 4.14 +/- 0.43 | 4.26 +/- 1.43 |
|                    Regression Test                    | 4.00 +/- 0.60 | 5.85 +/- 2.65 |
|       Define data model for all shared data(15)       | 3.85 +/- 0.92 | 4.59 +/- 0.96 |
|                     Documentation                     | 4.03 +/- 0.40 | 6.19 +/- 1.19 |
|                         2 Tier                        | 6.77 +/- 1.33 | 7.95 +/- 0.49 |
|           Define ext mandatory data std(18)           | 4.09 +/- 0.76 | 7.02 +/- 1.06 |
|                      Monitor(11)                      | 1.15 +/- 0.37 | 6.23 +/- 1.68 |
| XXX coordinates and external client does whatever(20) | 6.41 +/- 0.96 | 4.15 +/- 0.86 |
|        Build internal extensible data model(16)       | 2.85 +/- 0.55 | 3.98 +/- 1.22 |
|                    App Framework(6)                   | 6.92 +/- 1.78 | 7.03 +/- 0.55 |
|                         3 Tier                        | 6.42 +/- 1.03 | 7.63 +/- 1.05 |
+-------------------------------------------------------+---------------+---------------+
```

### Cluster 16
#### Measures
```
+---------------+--------+------+
|    measure    | median | iqr  |
+---------------+--------+------+
|   softgoals   |   4    |  0   |
|     costs     | 39.15  | 0.72 |
|    benefits   | 63.22  | 2.61 |
| decisions_set |   17   |  0   |
+---------------+--------+------+
```
#### Nodes
```
+-------------------------------------------------------+---------------+---------------+
|                          Node                         |      Cost     |    Benefit    |
+-------------------------------------------------------+---------------+---------------+
|                    Data Service(7)                    | 4.39 +/- 0.71 | 7.78 +/- 2.10 |
|                     Pnp Framework                     | 7.00 +/- 1.47 | 7.54 +/- 1.04 |
|                      New Database                     | 9.30 +/- 0.43 | 7.01 +/- 1.65 |
|       Provide logical data scheme internally(8)       | 4.11 +/- 0.75 | 4.19 +/- 1.52 |
|        External data model can be extended(19)        | 6.33 +/- 0.84 | 7.64 +/- 1.30 |
|       Svc layer w/ extracted biz logic in DB(12)      | 4.18 +/- 0.59 | 7.20 +/- 1.97 |
|          Svc layer w/ extracted biz logic(13)         | 7.61 +/- 2.21 | 4.96 +/- 1.39 |
|   External clients get exactly what they request(10)  | 6.35 +/- 1.26 | 3.97 +/- 0.72 |
| XXX coordinates and internal client does whatever(17) | 4.79 +/- 0.70 | 4.96 +/- 1.44 |
|                    Regression Test                    | 4.32 +/- 0.22 | 7.77 +/- 0.79 |
|       Define data model for all shared data(15)       | 4.74 +/- 1.43 | 4.43 +/- 0.39 |
|                     Documentation                     | 4.35 +/- 0.71 | 8.20 +/- 0.92 |
|                         2 Tier                        | 7.67 +/- 1.64 | 7.53 +/- 2.06 |
|           Define ext mandatory data std(18)           | 4.49 +/- 0.33 | 7.91 +/- 1.15 |
|                      Monitor(11)                      | 1.61 +/- 0.11 | 7.96 +/- 0.41 |
| XXX coordinates and external client does whatever(20) | 7.94 +/- 0.70 | 4.00 +/- 0.85 |
|        Build internal extensible data model(16)       | 2.62 +/- 0.25 | 4.42 +/- 0.45 |
|                    App Framework(6)                   | 7.16 +/- 0.86 | 8.05 +/- 1.79 |
|                         3 Tier                        | 6.65 +/- 1.83 | 7.84 +/- 1.88 |
+-------------------------------------------------------+---------------+---------------+
```

