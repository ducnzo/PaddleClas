input_file = 'test_list.txt'
output_file = 'test_list.txt'

with open(input_file, 'r') as file:
    lines = file.readlines()

updated_lines = []
for line in lines:
    columns = line.split()
    updated_line = ' '.join(columns[:2]) + '\n'
    updated_lines.append(updated_line)

with open(output_file, 'w') as file:
    file.writelines(updated_lines)