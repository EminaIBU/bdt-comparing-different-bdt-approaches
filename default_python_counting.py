
import csv, time, os



ratings_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

with open('Hotel_Reviews.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    next(reader)
    
    start_time = time.time()
    for row in reader:
        rating = int(row['Rating'])
        ratings_count[rating] += 1

print("1: " + str(ratings_count.get(1)))
print("2: " + str(ratings_count.get(2)))
print("3: " + str(ratings_count.get(3)))
print("4: " + str(ratings_count.get(4)))
print("5: " + str(ratings_count.get(5)))
end_time = time.time() 

#Define timing direcotry
current_directory = os.getcwd()
folder_name = "timing"
file_name = "default_python_time_info.txt"

# Write time details to a file
file_path = os.path.join(current_directory, folder_name, file_name)
with open(file_path, 'w+') as file:
    file.write(f"Execution Time: {end_time - start_time} seconds")