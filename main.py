from pyspark.sql import SparkSession
import time
from time import sleep
import psutil
import os


def get_memory_usage():
    return psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2


def start_session():
    spark = SparkSession.builder.appName("ExampleApp").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    return spark


def data_manip(df):
    df.show(5)
    df.describe()
    df.select("type", "nameDest").show(10)
    df.filter(df['amount'] < 5000).show(10)
    df.filter(df['amount'] >= 5000).count()
    df.withColumn('new_amount', df['amount']/10).show(10)
    df.groupBy('type').count().show()


if __name__ == "__main__":
    spark = start_session()
    df = spark.read.csv("hdfs://namenode:9001/Fraud.csv", header=True)
    df.cache()

    times = []
    ram = []
    for i in range(30):
        start = time.time()
        data_manip(df)
        end = time.time()
        times.append(end - start)
        ram.append(get_memory_usage())

    print(times)
    print(ram)
    spark.stop()