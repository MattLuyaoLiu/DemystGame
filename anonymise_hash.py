"""
# This is a Hashing cryptographic solusion with hash function SHA-256, which is one-way operation.
# The anonymized data can not decrypt or reverse the hash back.
# But the process is much faster and allows you to securely transform data into an unreadable format.
# The selection of encription algorithms is significantly effecting the processing speed. 
# However it really depends on the purpose of the application and data usage. 

# to process big size data, uncoment line 22-23, comment 20-21
"""

import csv
import hashlib
import time

# Function to anonymize a given value using a hash function
def anonymize_value(value):
    return hashlib.sha256(value.encode()).hexdigest()[:10]  # Taking the first 10 characters for simplicity

# Read the input CSV file
input_file = 'output_csv.csv'
output_file = 'anonymized_hash.csv'
# input_file = 'output_csv_duplicated.csv'
# output_file = 'anonymized_hash_duplicated.csv'

start_time = time.time() # Record the start time

with open(input_file, mode='r', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile, delimiter='|')
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='|')

    # Write the header to the output file
    writer.writeheader()

    # Process each row and anonymize the specified columns
    for row in reader:
        row['first_name'] = anonymize_value(row['first_name'])
        row['last_name'] = anonymize_value(row['last_name'])
        row['address'] = anonymize_value(row['address'])
        writer.writerow(row)

print(f"Anonymized CSV file generated successfully: {output_file}")
end_time = time.time() # Record the end time
elapsed_time = end_time - start_time  # Calculate the elapsed time
print("Encription time:", elapsed_time)