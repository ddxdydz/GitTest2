import os


def human_read_format(size):  # size — размер файла в байтах.
    prf = ['Б', 'КБ', 'МБ', 'ГБ']
    cur_prf = 0
    while size >= 1024:
        size /= 1024
        cur_prf += 1
    return f'{round(size)}{prf[cur_prf]}'


def get_files_sizes():
    files_sizes = []
    for obj_name in os.listdir():
        if os.path.isfile(obj_name):
            size = human_read_format(
                int(os.path.getsize(obj_name)))
            files_sizes.append(f'{obj_name} {size}')
    return '\n'.join(files_sizes)


# get_files_sizes()
