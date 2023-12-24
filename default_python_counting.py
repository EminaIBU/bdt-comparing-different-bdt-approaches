
import csv, time



ratings_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

with open('Hotel_reviews.csv', newline='', encoding='utf-8') as csvfile:
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

file_path = 'C:/Dev/BigData/timing/default_python_time_info.txt'
with open(file_path, 'w+') as file:
    file.write(f"Execution Time: {end_time - start_time} seconds")