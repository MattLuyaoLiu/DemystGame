# Question1
- Run
```python generate_fwf.py```.
- It will generate a fixed-width file using the provided spec file and sample data, named 'formatted_fwf.txt'.

- Then run 
```python parse_fwf_to_csv.py```.
- It will generate a CSV file with the delimiter '|', named 'output_csv.csv'.
- No extra library needs to be installed but Python 3.
- More detailed comments are labelled inside the scripts.


# Question2
## Step1 anonymisation:
- It might need to install cryptography package (If you feel like).
```pip install cryptography```.
- More detailed comments are labelled inside the scripts.
- For different purposes of the data usage and the requirement of process speed, I wrote two encryption methods below.

### Hash
- Run
```python anonymise_hash.py```.
- It will output an one-way encrypted csv result, named 'anonymised_hash.csv'.

### Fernet
- Run 
```python anonymise_fernet.py```
- It will output two files:<br>
-- encrypted csv result, named 'anonymised_fernet_encrypted.csv'.<br>
-- decrypted csv result, named 'anonymised_fernet_decrypted.csv'.<br>
- The decrypted csv result is retrieved from the encrypted csv result with the same secret key.

## Step2 big data processing
### Generate 2G csv file:
- Run ```python duplicated_data.py```, the script will duplicate output_csv.csv into a 2.016G csv file, named 'output_csv_duplicated.csv'
- Roughly it takes 40 seconds.

### Switch the input file sources:
#### Inside anonymise_hash.py:
- uncomment lines 22-23, comment lines 20-21.
- output file named: 'anonymized_hash_duplicated.csv'
- roughly it takes 6 minutes  (347 seconds). Similar size with input file, around 2.1G.

#### Inside anonymise_fernet.py:
- uncomment lines 33-35, comment lines 31-33.
- encryption output file named: 'anonymized_fernet_encrypted_duplicated.csv'.
- decryption output file named: 'anonymized_fernet_decrypted_duplicated.csv'.


