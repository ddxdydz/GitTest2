import os


print(os.name)  # тип операционной системы

print(os.getcwd())  # узнать имя текущего каталога
os.chdir('ЗАДАЧИ/files')  # Для смены текущего каталога / C:\Program files.
os.chdir('')  # из текущего каталога в родительский

# Получение списка файлов и вложенных каталогов (можно передать адрес)
print(os.listdir())  # ['1', '2', '3', '1.txt', 'Icon\r']

# os.walk() возвращает кортеж из трех элементов:
for currentdir, dirs, files in os.walk('ЗАДАЧИ/files'):
    print(currentdir, dirs, files)  # текущий каталог, список вложенных каталогов, список файлов текущей директории.

# Флаги W_OK, R_OK, F_OK отвечают за возможность записи, чтения, факт существования файла.
os.access("1.txt", os.F_OK)

os.path.exists('ЗАДАЧИ/files/3')  # существует ли файл
os.path.isfile('ЗАДАЧИ/files/3')
os.path.isdir('files/2')

os.path.abspath('1.txt')  # вернет абсолютный путь по относительному
os.path.dirname('1.txt')  # полное имя каталога, в котором находится файл

os.path.getsize('obj_name')  # размер


import shutil

shutil.copy('ЗАДАЧИ/files/3/Описание.txt', 'ЗАДАЧИ/files/Копия.txt')  # скопировать файл(источник, приёмник)
shutil.rmtree('Путь до папки')  # Удаление папки
shutil.move('старое_место', 'новое_место')  # Перенос папки (со всем ее содержимым) в новое место
shutil.get_archive_formats()  # вывод поддерживпаемых форматов
# мы создали архив с именем archive типа zip, положив него все содержимое каталога files.
shutil.make_archive('archive', 'zip', root_dir='ЗАДАЧИ/files')


from zipfile import ZipFile
# работать с архивом, как с обычной папкой, содержащей файлы и другие каталоги.

# выведет на экран содержание архива
with ZipFile('archive.zip') as myzip:  # можно укачать mode='r'
    myzip.printdir()

# можно получать информацию о файлах в архиве в виде списка:
with ZipFile('archive.zip') as myzip:
    info = myzip.infolist()
print(info[0].orig_filename)

# Имена файлов в архиве в виде списка:
with ZipFile('archive.zip') as myzip:
    print(myzip.namelist())

#  «вытащим» теперь и конкретный файл:
with ZipFile('archive.zip') as myzip:
    with myzip.open('1.txt', 'r') as file:
        print(file.read())
with ZipFile('archive.zip') as myzip:
    with myzip.open('1.txt', 'r') as file:
        print(file.read().decode('utf-8'))
with ZipFile('archive.zip', 'w') as myzip:
    myzip.write('test.txt')  # запись
    print(myzip.namelist())
with ZipFile('archive.zip', 'a') as myzip:
    myzip.write('test.txt')
    print(myzip.namelist())

# вытаскивает из архива все содержимое в указанную папку.
ZipFile.extractall(path=None, members=None, pwd=None)


from pickle import loads, dumps
s = {'Иван': 24, 'Сергей': 11}
d = dumps(s)
print(d)
loads(d)

import json
data = '''
{ 
  "scoring": [ 
    { 
      "required_pretests": [], 
      "required_tests": [1], 
      "outcome": 1, 
      "points": 0 
    }, 
    { 
      "required_pretests": [], 
      "required_tests": [2, 3, 4], 
      "outcome": 1, 
      "points": 30 
    }, 
    { 
      "required_pretests": [], 
      "required_tests": [5, 6, 7, 8], 
      "outcome": 1, 
      "points": 40 
    }, 
    { 
      "required_pretests": [], 
      "required_tests": [9, 10], 
      "outcome": 1, 
      "points": 20 
    }, 
    { 
      "required_pretests": [], 
      "required_tests": [11], 
      "outcome": 1, 
      "points": 10 
    } 
  ] 
}'''
resp = json.loads(data)
print(resp['scoring'])

s = {'Первый параметр': 24,
     'Второй параметр': 11,
     "Параметр со словарем": {"Ключ1": "Знач1", "Ключ 2": "Знач2"}}
print(json.dumps(s, ensure_ascii=False, indent=4))
'''
любая работа с JSON в Python происходит по алгоритму:

1 Получение словаря с данными
2 Преобразание словаря в JSON-объект
3 Передача данных

Или в обратную сторону:

1 Получение файла или строки с JSON-содержимым
2 Преобразование данных в словарь Python
3 Работа с данными
'''
