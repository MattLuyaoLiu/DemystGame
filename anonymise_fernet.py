"""
# Fernet is a symmetric encryption algorithm used for secure messaging in Python applications.
# Fernet is efficient for encrypting large amounts of data quickly and securely, making it suitable for various cryptographic applications
# By using this symmetric encryption, the original data could be later retrieved, by provided the encryption key.

"""

from cryptography.fernet import Fernet
import csv
import time

# Generate and save a key (this should be done once and the key should be kept safe)
key = Fernet.generate_key()
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Load the key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# encription way
def encrypt_value(value):
    return cipher_suite.encrypt(value.encode()).decode()
# decription way
def decrypt_value(value):
    return cipher_suite.decrypt(value.encode()).decode()

# Read the input CSV file
input_csv_file = 'output_csv.csv'
output_file_encrypt = 'anonymized_fernet_encrypted.csv'
output_file_decrypt = 'anonymized_fernet_decrypted.csv'
# input_csv_file = 'output_csv_duplicated.csv'
# output_file_encrypt = 'anonymized_fernet_encrypted_duplicated.csv'
# output_file_decrypt = 'anonymized_fernet_decrypted_duplicated.csv'
### Encryption process
start_time_en = time.time() # Record the encription start time
with open(input_csv_file, mode='r') as infile, open(output_file_encrypt, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='|')
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='|')

    # Write the header to the output file
    writer.writeheader()

    # Process each row and encrypt the specified columns
    for row in reader:
        row['first_name'] = encrypt_value(row['first_name'])
        row['last_name'] = encrypt_value(row['last_name'])
        row['address'] = encrypt_value(row['address'])
        writer.writerow(row)

print(f"Encrypted CSV file generated successfully: {output_file_encrypt}")
end_time_en = time.time() # Record the encription end time
elapsed_time_en = end_time_en - start_time_en  # Calculate the elapsed encription time
print("Encription time:", elapsed_time_en)

### Decryption process
start_time_de = time.time() # Record the decription start time
with open(output_file_encrypt, mode='r') as infile, open(output_file_decrypt, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='|')
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='|')

    # Write the header to the output file
    writer.writeheader()

    # Process each row and decrypt the specified columns
    for row in reader:
        row['first_name'] = decrypt_value(row['first_name'])
        row['last_name'] = decrypt_value(row['last_name'])
        row['address'] = decrypt_value(row['address'])
        writer.writerow(row)

print(f"Decrypted CSV file generated successfully: {output_file_decrypt}")
end_time_de = time.time() # Record the decription end time
elapsed_time_de = end_time_de - start_time_de  # Calculate the elapsed decription time
print("Decription time:", elapsed_time_de)