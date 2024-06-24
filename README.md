# SparkLab

## Dataset
[Fraudulent Transactions Prediction](https://www.kaggle.com/datasets/vardhansiramdasu/fraudulent-transactions-prediction). 6362620 rows, 10 features (types: string, float, int)

## Put data on HDFS
``` bash
docker cp data/Fraud.csv namenode:/
docker exec -it namenode bash
hdfs dfs -put Fraud.csv /
```

## Results
Using optimization is [dataframe.cache()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.cache.html)

### Time (sec.):
|        | 1 Datanode, not opt | 1 Datanode, opt | 3 Datanode, not opt | 3 Datanode, opt |
|--------|---------------------|-----------------|---------------------|-----------------|
| Max    | 6.33                | 11.12           | 6.64                | 11.71           |
| Min    | 3.1                 | 0.46            | 2.94                | 0.48            |
| Mean   | 3.36                | 0.94            | 3.2                 | 0.94            |
| Median | 3.21                | 0.51            | 3.04                | 0.52            |

### Memory usage (MiB)
|        | 1 Datanode, not opt | 1 Datanode, opt | 3 Datanode, not opt | 3 Datanode, opt |
|--------|---------------------|-----------------|---------------------|-----------------|
| Max    | 38.22                | 38.1           | 37.96                | 37.92           |
| Min    | 38.22                 | 38.1            | 37.59                | 37.92            |
| Mean   | 38.22                | 38.1            | 37.67                 | 37.92            |
| Median | 38.22                | 38.1            | 37.61                | 37.92            |


![image](https://github.com/kasyanikita/spark_lab/assets/71206801/e899372f-0b0d-4011-867f-9fbfa9998662)
![image](https://github.com/kasyanikita/spark_lab/assets/71206801/e9dd5ebd-389a-4510-804d-e64ec43041df)
![image](https://github.com/kasyanikita/spark_lab/assets/71206801/068ffd65-aaae-45c0-abbe-ad7717218d1a)
![image](https://github.com/kasyanikita/spark_lab/assets/71206801/57af6b0b-afdb-4b50-a89f-c3d269e05996)
![image](https://github.com/kasyanikita/spark_lab/assets/71206801/a9053ee8-0fa7-43ad-ac34-b782c0d7e315)
![image](https://github.com/kasyanikita/spark_lab/assets/71206801/5e2bd9f3-62eb-43f6-8b0e-fc4de7347373)
![image](https://github.com/kasyanikita/spark_lab/assets/71206801/81626be1-bdcd-4ee9-971b-ca3ba13b9dff)
![image](https://github.com/kasyanikita/spark_lab/assets/71206801/2eca76ef-87c1-4dc5-a8bb-9e71f7f36bb0)


