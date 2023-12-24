import subprocess
import os
import shutil
from tabulate import tabulate

print("Starting all scripts, please wait until everything is executed")

# Remove logs and timing
directories = ["logs", "timing"]
current_directory = os.getcwd()

for directory in directories:
    directory_path = os.path.join(current_directory, directory)
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        try:
            # Remove the directory and its contents
            shutil.rmtree(directory_path)
        except OSError:
            pass

# Create empty logs and timing folders
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to execute script and redirect output to log file
def execute_script(script_name, output_file):
    with open(output_file, 'w+') as log_file:
        if (script_name == "map_reduce_counting.py"):
            subprocess.run(["python", script_name, "duplicated_file.csv"], stdout=log_file, stderr=subprocess.STDOUT)
        else:
            subprocess.run(["python", script_name], stdout=log_file, stderr=subprocess.STDOUT)

# Execute map_reduce_counting.py with parameter
execute_script("map_reduce_counting.py", "logs/map_reduce_log.txt")

# Execute default_python_counting.py
execute_script("default_python_counting.py", "logs/default_python_log.txt")

# Execute apache_spark_counting.py
execute_script("apache_spark_counting.py", "logs/apache_spark_log.txt")

# Scripts finished execution
print("\nAll scripts have finished execution\nLogs are saved into Logs folder\n\n")


# Variables to store execution times for the first two files
apache_spark_time = None
default_python_time = None
# Variables to store execution times for the map reduce file
map_reduce_times = []

# Loop through all files in the timing to get execution times for every method
for filename in os.listdir(directory):
    if filename.endswith(".txt"):  # Check if the file is a txt file
        filepath = os.path.join("timing", filename)  # Create the full file path
      
        # Open the file and read its contents line by line
        with open(filepath, 'r') as file:
            lines = file.readlines()
            if filename == "apache_spark_time_info.txt":
                apache_spark_time = float(lines[0].split(":")[1].strip().split()[0])
            elif filename == "default_python_time_info.txt":
                default_python_time = float(lines[0].split(":")[1].strip().split()[0])
            elif filename == "map_reduce_time_info.txt":
                # Extract execution times from lines
                times = [float(line.split(":")[2].strip().split()[0]) for line in lines]
                map_reduce_times.extend(times)

# Get Hotel Review count from default_python_log.txt
# This could be read from any log file, but it was the simplest to use this one
for filename in os.listdir("logs"):
    if filename == "default_python_log.txt":  # Check if the file is a txt file
        filepath = os.path.join("logs", "default_python_log.txt")  # Create the full file path

        # Open the file and read its contents line by line
        ratings = []
        with open(filepath, 'r') as file:
            file_lines = file.readlines()
            for single_line in file_lines:
                single_line = "".join(single_line.split())
                split_list = single_line.split(':')
                ratings.append([split_list[0], split_list[1]])

# Print table format for Hotel Reivews
print("Hotel Ratings we counted")
print(tabulate(ratings, headers=['Rating (stars)', 'Count'], tablefmt="outline"))

# Print table format for Methods and their execution times
print("\nRequired time to count all ratings for every method")
formattedResultList = [["Apache Spark", "{:.2f}".format(apache_spark_time)], ["Map Reduce", "{:.2f}".format(max(map_reduce_times))], ["Default python counting", "{:.2f}".format(default_python_time)]]
print(tabulate(formattedResultList, headers=['Method', 'Time required to finish (sec)'], tablefmt="outline"))