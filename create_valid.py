input_file = "train_list.txt"  # Đường dẫn đến tệp văn bản đầu vào
output_file = "val_list.txt"  # Đường dẫn đến tệp văn bản đầu ra

# Open the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Create a dictionary to store the first two lines for each class
class_lines = {}

# Iterate over the lines in the input file
for line in lines:
    # Split the line by space
    parts = line.split()
    
    # Get the class value
    class_value = parts[1]
    
    # Check if the class value is already in the dictionary
    if class_value in class_lines:
        # If it is, append the line to the existing list
        class_lines[class_value].append(line)
    else:
        # If it is not, create a new list with the line
        class_lines[class_value] = [line]

# Open the output file
with open(output_file, 'w') as file:
    # Iterate over the dictionary items
    for class_value, lines in class_lines.items():
        # Write the first two lines for each class to the output file
        for l in lines[:2]:
            file.write(l)
        # Remove the first two lines for each class from the input file
        lines = lines[2:]
        # Update the dictionary with the modified lines
        class_lines[class_value] = lines

# Write the remaining lines to the input file
with open(input_file, 'w') as file:
    for lines in class_lines.values():
        file.writelines(lines)


