"""
# Parse the formatted fixed width file to csv with the help of spec.
# Keep it simple.

"""

import csv
import os

def main():
    delimiter = '|'
    specs_filename = "specs.txt"
    input_fwf_filename = "formatted_fwf.txt"
    output_csv_filename = "output_csv.csv"

    # load specs
    specs = []
    with open(specs_filename, 'r', encoding='utf-8') as f:
        for line in f:
            field, width, alignment = line.strip().split(',')
            specs.append((field, int(width)))
    # print(specs)

    # parsing fwf data.
    fixed_width_data = []
    if os.path.exists(input_fwf_filename):
        pass
    else: 
        print("There is no fixed width file:", input_fwf_filename)
        exit()
    with open(input_fwf_filename, 'r', encoding='utf-8') as f:
        for line in f:
            parsed_line = {}
            start = 0
            for field, width in specs:
                parsed_line[field] = line[start:start + width].strip()
                start += width
            fixed_width_data.append(parsed_line)
    # print(fixed_width_data)

    # output csv
    with open(output_csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[col[0] for col in specs], delimiter=delimiter)
        writer.writeheader()
        for row in fixed_width_data:
            writer.writerow(row)
    print(f"CSV file '{output_csv_filename}' generated successfully.")


if __name__ == '__main__':
    main()