import dask.dataframe as dd
import time, os

# Load CSV file into Dask
dataframe = dd.read_csv('Hotel_Reviews.csv')

# Perform counting
start_time = time.time()
count_result = dataframe['Rating'].value_counts().compute()
end_time = time.time()
print(count_result)

#Define timing direcotry
current_directory = os.getcwd()
folder_name = "timing"
file_name = "dask_time_info.txt"

# Write time details to a file
file_path = os.path.join(current_directory, folder_name, file_name)
with open(file_path, 'w+') as file:
    file.write(f"Execution Time: {end_time - start_time} seconds")