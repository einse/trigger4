# To the extent possible under law,
# Sergey Arsentev (http://github.com/einse)
# has waived all copyright
# and related or neighboring rights to Trigger.
# This work is published from: Russian Federation.
# More on this: see README and/or
# http://creativecommons.org/publicdomain/zero/1.0/

import sys, os, time

script_path = os.path.dirname(os.path.abspath(__file__))
path_to_start = script_path
tags = []
shifted_argv = sys.argv[1:]
for i, arg in enumerate(shifted_argv):
    if os.path.sep in arg:
        path_to_start = arg
    else:
        tags.append(arg)
if len(tags) == 0:
    print('No tags provided.\n')
    sys.exit();

count_of_hits = 0
dirs_with_hits = {}
dir_no = 0

now = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
path_for_indices = os.path.join(script_path, 'trigger-index')
if not os.path.exists(path_for_indices):
    print('''Output folder ("trigger-index") doesn't exist.\n''')
    sys.exit();
path_template_for_index = os.path.join(path_for_indices, now + '_')
index_of_folders = path_template_for_index + 'folders-index.txt'
index_of_files   = path_template_for_index + 'files-index.txt'

def generate_dir_id(dirname, filename, number):
    file_path = os.path.join(dirname, filename)
    timestamp = time.gmtime(os.stat(file_path).st_mtime)
    return time.strftime('%Y-%m-%d', timestamp) + '-f' + str(number)

def make_row(*any_args):
    str_args = []
    for any_arg in any_args:
        str_args.append(str(any_arg))
    return '\t'.join(str_args)

with open(index_of_files, 'a') as f:
    for a_dir, _, files in os.walk(path_to_start):
        count_of_hits = 0
        dir_no += 1
        for a_file in files:
            for a_tag in tags:
                if a_tag in a_file:
                    count_of_hits += 1
                    if count_of_hits == 1:
                        dir_id = generate_dir_id(a_dir, a_file, dir_no)
                    hit_id = dir_id + '-ff' + str(count_of_hits)
                    row = make_row(dir_id, hit_id, a_file)
                    f.write(row + '\n')
                    break #matching_tags
                else:
                    continue #matching_tags
            continue #searching_files
        if count_of_hits > 0:
            dirs_with_hits[dir_id] = [len(files), count_of_hits, a_dir]

with open(index_of_folders, 'a') as f:
    for i, dir_id in enumerate(dirs_with_hits):
        row = make_row(
            dirs_with_hits[dir_id][0],
            dirs_with_hits[dir_id][1],
            dir_id,
            dirs_with_hits[dir_id][2],
        )
        f.write(row + '\n')
