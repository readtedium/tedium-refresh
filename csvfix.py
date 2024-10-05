import csv

def replace_commas_in_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        # Create a writer with pipes as the delimiter and specify an escape character
        writer = csv.writer(outfile, delimiter='|', quoting=csv.QUOTE_NONE, escapechar='\\')

        for row in reader:
            # Create a modified row
            modified_row = []
            for item in row:
                # Check if the item is enclosed in quotes
                if item.startswith('"') and item.endswith('"'):
                    # Remove outer quotes
                    item = item[1:-1]
                modified_row.append(item)

            # Write the modified row with pipes as delimiters
            writer.writerow(modified_row)

if __name__ == '__main__':
    input_filename = 'input.csv'  # Change this to your input file name
    output_filename = 'output.csv'  # Change this to your desired output file name

    replace_commas_in_csv(input_filename, output_filename)
    print(f"Outer quotes removed and commas retained. Output written to {output_filename}")