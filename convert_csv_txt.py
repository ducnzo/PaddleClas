import csv

def convert_csv_to_txt(csv_file, txt_file):
    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        with open(txt_file, 'w') as txt_file:
            for row in reader:
                txt_file.write(' '.join(row) + '\n')

# Define the path to your CSV file
csv_file_path = "test_kaggletest.csv"

# Define the path for the text file
txt_file_path = "test_list.txt"

# Convert CSV to TXT
convert_csv_to_txt(csv_file_path, txt_file_path)
