"""
# This is the script to genverate 2G csv data based on csv output.
"""

import csv
import time

# Function to duplicate the data
def duplicate_data(input_file, output_file, num_duplicates):
    with open(input_file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        header = next(reader)  # Read the header
        data = list(reader)  # Read the rest of the data

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter='|')
        writer.writerow(header)  # Write the header

        for _ in range(num_duplicates):
            for row in data:
                writer.writerow(row)

    print(f"CSV file with duplicated data generated successfully: {output_file}")

# Define the input and output file names
input_file = 'output_csv.csv'
output_file = 'output_csv_duplicated.csv'

# Define the number of times to duplicate the data
num_duplicates = 16000000  # Adjust this number as needed

# Duplicate the data, calculate the processing time
start_time = time.time() # Record the start time
duplicate_data(input_file, output_file, num_duplicates)
end_time = time.time() # Record the end time
elapsed_time = end_time - start_time  # Calculate the elapsed time
print("Encription time:", elapsed_time)