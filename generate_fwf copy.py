
"""
# Sample data should have the same field list in spec file. Otherwise it will throw keyerror exception.
# Manually created some testing data in standard JSON format.
# Loading specs process is robust for some unexpected error input.
# The [:width] ensures that the text does not exceed the specified width, truncating any excess characters.
# Adding defualt value for the missing data field.
# Pandas package has read_fwf and to_fwf methods, but avoid using it here to follow the criteria.
# Only using standard libraies to do the processing, do not need to install anything but python 3.
# Typically fwf files do not include headers. if need, uncomment those lines 118-121.

"""

import json

# load sample data
def load_sample_data(data_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    print("Sample data loaded successfully:", data_path)
    return data

# load specs
def load_specs(specs_path):
    with open(specs_path, 'r', encoding='utf-8') as f:
        # spec_header = f.readline() # skip spec header. "field, width, alignment"
        for line in f:
            """# simple loading without valid check
            # field, width, alignment = line.strip().split(',')
            # specs[field] = int(width)
            # justify[field] = alignment
            """
            # valid check if there is empty row in specs file
            if len(line.strip()) == 0:
                print("Empty row in specs, skip")
                continue
            else:
                pass
            # try reading parameters
            try:
                temp = line.strip().split(',')
                if len(temp) == 3:
                    temp[0] = temp[0].strip()
                    # valid check for 'field length'
                    if temp[1].strip().isdigit() and int(temp[1]) < 50:
                        specs[temp[0]] = int(temp[1])
                    else:
                        print(f"Invalid field length parameter for '{temp[0]}'. Default value '0' is assigned.")
                        specs[temp[0]] = 0 # given a default value 0
                    # valid check for 'alignment'
                    if temp[2].strip() in ('L', 'R', 'C'):
                        justify[temp[0]] = temp[2]
                    else:
                        print(f"Invalid alingment parameter for '{temp[0]}'. Default value 'L' is assigned.")
                        justify[temp[0]] = 'L' # given a default value L
                else:
                    print("Invalid parameter numbers in line:", temp)
            except:
                raise Exception(f"Loading spec '{temp[0]}' error...")
    print("Specs loaded successfully:", specs_path)

# row processing
def format_row(row, specs, defaults):
    formatted_row = ''
    for col_name, width in specs.items():
        if(justify[col_name] == 'R'):
            # temprow = str(row[col_name]).rjust(width)[:width] 
            temprow = str(row.get(col_name, defaults.get(col_name, ''))).rjust(width)[:width]
        elif(justify[col_name] == 'C'):
            # temprow = str(row[col_name]).center(width)[:width]
            temprow = str(row.get(col_name, defaults.get(col_name, ''))).center(width)[:width]
        else:
            # temprow = str(row[col_name]).ljust(width)[:width]
            temprow = str(row.get(col_name, defaults.get(col_name, ''))).ljust(width)[:width]
        formatted_row += temprow
    return formatted_row

# output fixed width file
def output_fwf(output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in fixed_width_data:
            f.write(line + '\n')
    print("Fixed width file generated successfully:", output_path)


### Initialization
data=[]
specs = {} # length of each field
justify = {} # alignment of each field
fixed_width_data = []
sample_data_filename = "sample_data.json"
specs_filename = "specs.txt"
output_fwf_filename = "formatted_fwf.txt"

defaults = {
    "first_name": "N/A",      # Default value for first_name
    "last_name": "N/A",       # Default value for last_name
    "address": "N/A",         # Default value for address
    "date_of_birth": "0000-00-00"  # Default value for date_of_birth
}


if __name__ == '__main__':

    ### Load sample data
    data = load_sample_data(sample_data_filename)
    # load specs
    load_specs(specs_filename)

    # print(data)
    # print(specs)
    # print(justify)

    ### Processing rows
    fixed_width_data = [format_row(row, specs, defaults) for row in data]
    # print(fixed_width_data)

    # # Generate the header row
    # header_row = format_row({col: col for col in specs.keys()}, specs, {})
    # # print(header_row)
    # fixed_width_data = [header_row] + fixed_width_data

    ### Output fixed width file
    output_fwf(output_fwf_filename)
