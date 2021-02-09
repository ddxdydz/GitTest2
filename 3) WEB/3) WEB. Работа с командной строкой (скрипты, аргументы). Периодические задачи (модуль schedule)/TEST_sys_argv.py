'''
Запустить интерпретатор Python и в качестве параметра передать ему имя вашего скрипта:
Для ОС Linux: python3 test.py 1 2 3 4
Для ОС Windows: python test.py 1 2 3 4
Добавить в начало файла заголовок #!/путь/до/интерпретатора, по которому shell (командная оболочка) поймет
Надо сделать файл с программой исполняемым через команду chmod+x <имя_файла>.(ОС семейства Linux)
python C:\Users\User\Desktop\TEST_CMD.py 1 2 3 4
'''

import sys

print("my name is {}".format(sys.argv[0]))  # python3 files/cmd2.py
if len(sys.argv) > 1:
    print("first arg is: '{}' and last arg is '{}'".format(
        sys.argv[1], sys.argv[-1]))
else:
    print("No arguments")
