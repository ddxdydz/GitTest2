from zipfile import ZipFile


zip_name = 'crowd_archive.zip'

# Имена файлов в архиве в виде списка:
with ZipFile(zip_name) as myzip:
    indent_step = '  '
    indent = 0
    for obj_name in myzip.namelist():
        obj_path_list = [elem for elem in obj_name.split('/') if elem]
        print(indent_step * (len(obj_path_list) - 1) + obj_path_list[-1])
