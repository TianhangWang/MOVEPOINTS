import os


def process_file_add(file_directory, value):
    result = list()
    with open(file_directory, 'r') as processedFile:
        for line in processedFile.readlines():
            input_one_list = line.split()
            input_one_list[0] = str(float(input_one_list[0]) + value)
            out_str = " ".join(input_one_list)
            result.append(out_str)
    with open(file_directory, 'w') as processedFile:
        for line in result:
            processedFile.write(line)
            processedFile.write('\n')


dir_name = "D:\\975_reaction\\0.001\\cat"
files = os.listdir(dir_name)
files_path_list = [(dir_name + "\\" + file) for file in files]

for file_path in files_path_list:
    process_file_add(file_path, 40)



