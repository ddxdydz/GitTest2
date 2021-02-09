import os


inp_file_name = input()


def human_read_format(size):  # size — размер файла в байтах.
    prf = ['Б', 'КБ', 'МБ', 'ГБ']
    cur_prf = 0
    while size >= 1024:
        size /= 1024
        cur_prf += 1
    return f'{round(size)}{prf[cur_prf]}'


files_sizes_dict = dict()
for cur_dir, dirs, files in os.walk(inp_file_name):
    for file in files:
        file_path = f'{cur_dir}\\{file}'

        if os.path.isfile(file_path):
            if cur_dir not in files_sizes_dict.keys():
                files_sizes_dict[cur_dir] = 0
            files_sizes_dict[cur_dir] += os.path.getsize(file_path)

            if file_path not in files_sizes_dict.keys():
                files_sizes_dict[file_path] = 0
            files_sizes_dict[file_path] += os.path.getsize(file_path)

files_sizes_list = sorted(
    files_sizes_dict.items(),
    key=lambda elem: elem[1], reverse=True)

files_sizes_list = files_sizes_list[:min(len(files_sizes_list), 10)]

print('\n'.join([f'{name} {human_read_format(size)}'
                 for name, size in files_sizes_list]))
