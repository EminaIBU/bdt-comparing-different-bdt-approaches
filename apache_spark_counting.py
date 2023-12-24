from pyspark.sql import SparkSession
import time

spark = SparkSession.builder.appName("RatingCounter").getOrCreate()

# Load CSV file into Spark DataFrame
df = spark.read.csv("Hotel_Reviews.csv", header=True)

# Perform grouping and count
start_time = time.time()
result = df.groupBy("Rating").count().orderBy("Rating")
end_time = time.time()

result.show()


file_path = 'C:/Dev/BigData/timing/apache_spark_time_info.txt'
with open(file_path, 'w+') as file:
    file.write(f"Execution Time: {end_time - start_time} seconds")