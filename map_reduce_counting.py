from mrjob.job import MRJob
from mrjob.step import MRStep
import csv, time

class ReviewCounter(MRJob):

    # Define Mapper and Reducer Steps
    def steps(self):
        return[
            MRStep(
                mapper=self.reviews_mapper,
                reducer=self.reviews_reducer
                )
            ]

    # Define function which will be used as mapper for our CSV file
    def reviews_mapper(self, _, line):
        csv_row = next(csv.reader([line])) 
        
        # Ignore header row
        if csv_row[0] != 'Review':
            rating = int(csv_row[1])
            
            # Emit rating with count 1
            yield rating, 1  

    # Define function which will be used as reducer
    def reviews_reducer(self, key, values):
        # Calculate time required to count ratings
        start_time = time.time()
        count = sum(values)
        end_time = time.time()

        # Write time details to a file
        file_path = 'C:/Dev/BigData/timing/map_reduce_time_info.txt'
        with open(file_path, 'a+') as file:
            file.write(f"Key: {key}, Execution Time: {end_time - start_time} seconds\n")

        # Emit reducers output in Key-Value pairs
        yield key, count

# Check for main and run script
if __name__ == '__main__':
    ReviewCounter.run()
