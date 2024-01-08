from mrjob.job import MRJob
from mrjob.step import MRStep
import csv, time, os, sys

class ReviewCounter(MRJob):

    def configure_args(self):
        super(ReviewCounter, self).configure_args()
        self.add_passthru_arg('main_directory', default=None, help='Directory from where the main.py script is started')

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

        #Define timing direcotry
        current_directory = main_directory
        folder_name = "timing"
        file_name = "map_reduce_time_info.txt"
        file_path = os.path.join(current_directory, folder_name, file_name)

        # Write time details to a file
        file_path = os.path.join(current_directory, folder_name, file_name)
        with open(file_path, 'a+') as file:
            file.write(f"Key: {key}, Execution Time: {end_time - start_time} seconds\n")

        # Emit reducers output in Key-Value pairs
        yield key, count

# Check for main and run script
if __name__ == '__main__':
    #Get 2nd argument and define main_directory from it
    main_directory = sys.argv[2]

    #Run MapReduce
    ReviewCounter.run()
