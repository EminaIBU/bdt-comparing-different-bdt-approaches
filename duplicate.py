# Define the number of times you want to duplicate the file
num_duplicates = 100

# Read the contents of the original CSV file
with open('Hotel_reviews.csv', 'r', newline='', encoding='utf-8') as original_file:
    lines = original_file.readlines()
    header = lines[0]  # Extracting the header
    data = lines[1:]    # Extracting the rest of the data

# Write the contents including the header multiple times into a new file
with open('duplicated_file.csv', 'w', newline='', encoding='utf-8') as duplicated_file:
    duplicated_file.write(header)  # Writing the header once
    for _ in range(num_duplicates):
        duplicated_file.writelines(data)
