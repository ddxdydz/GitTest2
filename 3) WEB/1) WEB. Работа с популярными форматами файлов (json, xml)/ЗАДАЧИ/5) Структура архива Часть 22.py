from zipfile import ZipFile


def human_read_format(size):  # size — размер файла в байтах.
    prf = ['Б', 'КБ', 'МБ', 'ГБ']
    cur_prf = 0
    while size >= 1024:
        size /= 1024
        cur_prf += 1
    return f'{round(size)}{prf[cur_prf]}'


indent_step = '  '
zip_name = 'input.zip'
with ZipFile(zip_name) as myzip:
    for obj_name in myzip.namelist():
        obj_path_list = [elem for elem in obj_name.split('/') if elem]
        indent = indent_step * (len(obj_path_list[:-1]))
        file = myzip.getinfo(obj_name)
        size = human_read_format(file.file_size) if obj_name[-1] != '/' else ''
        print(indent + obj_path_list[-1] + ' ' + size)
