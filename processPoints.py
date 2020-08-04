

def depart_file(dir, index, born_dir):
    file_dir = dir + "\\" + str(index) + ".normals.txt"
    born_file_dir = born_dir + "\\" + str(index) + ".normals.txt"
    inter_list = list()
    with open(file_dir, 'r') as source_file, open(born_file_dir, 'w') as destination_file:
        for line in source_file.readlines():
            inter_list.append(line.split())
        for element in inter_list:
            if element[0] =='nan':
                destination_file.write('1' + '\n')
                destination_file.write('1' + '\n')
                destination_file.write('1' + '\n')
            else:
                destination_file.write(element[0] + '\n')
                destination_file.write(element[1] + '\n')
                destination_file.write(element[2] + '\n')


def aggregation_file(dir, index, born_dir):
    file_dir = dir + "\\" + str(index) + ".points.txt"
    born_file_dir = born_dir + "\\" + str(index) + ".points.txt"
    inter_list = ["1", "2", "3"]
    count = 0
    with open(file_dir, 'r') as source_file, open(born_file_dir, 'w') as destination_file:
        for line in source_file.readlines():
            if count == 0:
                inter_list[0] = line.strip()
                count += 1
            elif count == 1:
                inter_list[1] = line.strip()
                count += 1
            elif count == 2:
                inter_list[2] = line.strip()
                count = 0
                destination_file.write(" ".join(inter_list[0:3]) + "\n")


dir_name_c = "D:\\surf_\\surf"
dir_born_1 = "D:\\pcl-data\\normals"
dir_born_2 = "D:\\pcl-data"
for i in range(1, 976):
    #aggregation_file(dir_name_c, i, dir_born_1)
    depart_file(dir_born_1, i, dir_born_2)
    print("please wait -------{}%".format(i/5))
