import os


def get_file_line_nums(file_directory, index):
    file_directory = file_directory + "\\" + str(index) + ".points.txt"
    count = 0
    with open(file_directory, 'r') as points_open:
        for line in points_open.readlines():
            count = count+1
    return count


def generate_features_file(file_directory, count, index):
    directory = file_directory + "\\" + str(index) + ".features.txt"
    with open(directory, 'w') as features_file:
        for i in range(count):
            if i % 3 == 0:
                features_file.write(str(1) + "\n")
            else:
                features_file.write(str(1) + "\n")


def generate_normals_file(file_directory, count, index):
    directory = file_directory + "\\" + str(index) + ".normals.txt"
    with open(directory, 'w') as normals_file:
        for i in range(count):
            normals_file.write(str(1) + '\n')


def get_sum_file(born_directory, type, one_father_directory, other_father_directory, index):
    one_father_file = one_father_directory + "\\" + str(index) + "." + type
    other_father_file = other_father_directory + "\\" + str(index) + "." + type
    born_file = born_directory + "\\" + str(index) + "." + type
    with open(one_father_file, 'r') as one_father, open(other_father_file, 'r') as other_father, open(born_file, 'w') as son:
        for line in one_father.readlines():
            son.write(line)
        for line in other_father.readlines():
            son.write(line)


dir_name_c = "D:\\surf_0.001\\c-obj"
dir_name_e = "D:\\surf_0.001\\e-0.001"
dir_name_son = "D:\\surf_0.001"

for i in range(1, 501):
    count_c = get_file_line_nums(dir_name_c, i)
    count_e = get_file_line_nums(dir_name_e, i)
    #generate_features_file(dir_name_c, count_c, i)
    #generate_normals_file(dir_name_e, count_e, i)
    get_sum_file(dir_name_son, "points.txt", dir_name_c, dir_name_e, i)
    get_sum_file(dir_name_son, "normals.txt", dir_name_c, dir_name_e, i)
    get_sum_file(dir_name_son, "features.txt", dir_name_c, dir_name_e, i)
    print("please wait!!!!    now have done {0}%".format(i/5))

