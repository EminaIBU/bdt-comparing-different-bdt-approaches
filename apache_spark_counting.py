from pyspark.sql import SparkSession
import time, os

spark = SparkSession.builder.appName("RatingCounter").getOrCreate()

# Load CSV file into Spark DataFrame
df = spark.read.csv("Hotel_Reviews.csv", header=True)

# Perform grouping and count
start_time = time.time()
result = df.groupBy("Rating").count().orderBy("Rating")
end_time = time.time()

result.show()


#Define timing direcotry
current_directory = os.getcwd()
folder_name = "timing"
file_name = "apache_spark_time_info.txt"

# Write time details to a file
file_path = os.path.join(current_directory, folder_name, file_name)
with open(file_path, 'w+') as file:
    file.write(f"Execution Time: {end_time - start_time} seconds")