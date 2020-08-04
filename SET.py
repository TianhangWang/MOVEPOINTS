import os


def get_files_list(file_dir):
    files_list = os.listdir(file_dir)
    files_path_list = [(file_dir + "\\" + file) for file in files_list]
    return files_path_list


def get_result(file_list_one, file_list_tow, file_list_three, write_location):
    list_points = list()
    list_feature = list()
    lumo=['-0.462','1.0064','0.8704','0.2448','-0.408','-0.4624','1.0064','0.8704','0.2448','-0.408','-0.4624','1.0064','0.8704','0.2448','-0.408','-0.4624','1.0064','0.8704','0.2448','-0.408','-0.4624','1.0064','0.8704','0.2448','-0.408']

    count = 1
    for file_three in file_list_three:
        for file_one in file_list_one:
            for file_tow in file_list_tow:

                list_points = list()
                list_feature = list()

                with open(file_one, 'r') as file_list_five, open(file_tow, 'r') as file_list_six, open(file_three, 'r') as file_list_cat:
                    for line_five in file_list_five.readlines():
                        five_list = line_five.split()
                        new_five_list = five_list[0:3]
                        temp_list = five_list[3:]
                        temp_list.append("0")
                        list_points.append("\n".join(new_five_list))
                        list_feature.append('\n'.join(temp_list))
                    for line_six in file_list_six.readlines():
                        six_list = line_six.split()
                        new_six_list = six_list[0:3]
                        temp_list = six_list[3:]
                        if count%25 == 0:
                            temp_list.append('-0.408')
                        else:
                            temp_list.append(lumo[count%25 - 1])

                        #temp_list.append("0")
                        #temp_list.append("0")
                        list_points.append("\n".join(new_six_list))
                        list_feature.append("\n".join(temp_list))
                    for line_cat in file_list_cat.readlines():
                        cat_list = line_cat.split()
                        new_cat_list = cat_list[0:3]
                        temp_list = cat_list[3:]
                        temp_list.append('0')
                        #temp_list.append("0")
                        #temp_list.append("0")
                        list_points.append("\n".join(new_cat_list))
                        list_feature.append("\n".join(temp_list))
                with open(write_location + "\\" + str(count) + ".points.txt", "w") as point_file:
                    for point in list_points:
                        point_file.write(point)
                        point_file.write('\n')
                with open(write_location + "\\" + str(count) + ".features.txt", "w") as feature_file:
                    for feature in list_feature:
                        feature_file.write(feature)
                        feature_file.write('\n')
                count = count + 1
                print('the process has done: {} file '.format(count))


dir_one_name = r"E:\STUDY-PROGRESS\HUAXUE\PCL_975_reaction\0.001\25"
dir_tow_name = r"E:\STUDY-PROGRESS\HUAXUE\PCL_975_reaction\0.001\26"
dir_three_name = r"E:\STUDY-PROGRESS\HUAXUE\PCL_975_reaction\0.001\cat"

file_list_one = get_files_list(dir_one_name)
file_list_tow = get_files_list(dir_tow_name)
file_list_three = get_files_list(dir_three_name)

get_result(file_list_one, file_list_tow, file_list_three, r"E:\STUDY-PROGRESS\HUAXUE\PCL_975_reaction")






