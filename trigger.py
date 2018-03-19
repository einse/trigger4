import os
import time

start_path = '/'
tags = ['-мкрк', '-диз', 'мкрк-', 'диз-']
count_of_target_files_in_folder = 0
folders_collection = {}
current_folder_number = 0

current_time__unix = time.localtime()
current_time__human_cn\
    = time.strftime('%Y-%m-%d_%H-%M-%S', current_time__unix)
index_root = 'trigger-index'
folders_index_path\
    = './' + index_root + '/'\
    + current_time__human_cn + '_folders-index.txt'
files_index_path\
    = './' + index_root + '/'\
    + current_time__human_cn + '_files-index.txt'

for current_folder, folders, files in os.walk(start_path):    
    count_of_target_files_in_folder = 0
    current_folder_number = current_folder_number + 1
    for current_file in files:
        for current_tag in tags:
            if current_tag in current_file:
                count_of_target_files_in_folder\
                    = count_of_target_files_in_folder + 1
                if count_of_target_files_in_folder == 1:
                    current_path_of_file\
                        = current_folder + '/' + current_file
                    date_of_the_first_target_file_in_folder__unix\
                        = time.gmtime(os.stat(current_path_of_file).st_mtime)
                    date_of_the_first_target_file_in_folder__human_cn\
                        = time.strftime('%Y-%m-%d'\
                        , date_of_the_first_target_file_in_folder__unix)
                    target_folder_id\
                        = date_of_the_first_target_file_in_folder__human_cn\
                        + '-f'\
                        + str(current_folder_number)
                with open(files_index_path, 'a') as f:
                    target_file_id = target_folder_id + '-ff'\
                        + str(count_of_target_files_in_folder)
                    files_index_string = '{}\t{}\t{}'\
                        .format\
                        ( target_folder_id\
                        , target_file_id\
                        , current_file\
                        )
                    f.write(files_index_string)
                    f.write('\n')
                break
        continue # searching files
    if count_of_target_files_in_folder > 0:
        folders_collection[target_folder_id]\
            = [len(files)\
            , count_of_target_files_in_folder\
            , current_folder]
with open(folders_index_path, 'a') as f:
    for i, id_ in enumerate(folders_collection):
        folders_index_string = '{}\t{}\t{}\t{}'\
            .format\
            ( folders_collection[id_][0]\
            , folders_collection[id_][1]\
            , id_\
            , folders_collection[id_][2]\
            )
        f.write(folders_index_string)
        f.write('\n')
