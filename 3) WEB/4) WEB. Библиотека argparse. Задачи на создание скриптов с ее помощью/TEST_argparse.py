import sys
import argparse  # Парсер для параметров командной строки, аргументов и подкоманд

#  создать экземпляр объекта ArgumentParser
# description - Текст для отображения перед справкой по аргументу (по умолчанию: нет)
parser = argparse.ArgumentParser(description="convert integers to decimal system")

# sage: ex2.py [-h] [--base BASE] [--log LOG] integers [integers ...]
parser.add_argument('integers', metavar='integers', nargs='+', type=str, help='integers to be converted')
parser.add_argument('--base', default=2, type=int, help='default numeric system')
parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'), help='converted data should be written')
# positional arguments:
#   integers      integers to be converted
# optional arguments:
#   -h, --help   show this help message and exit
#   --base BASE  default numeric system
#   --log LOG    the file where converted data should be written

# usage: ex3.py [-h] arg1 arg2 N [N ...]
parser.add_argument("arg1")
parser.add_argument("arg2", help="echo this string")
parser.add_argument("int_args", metavar="N", type=int, nargs='+', help="echo some integers")
# positional arguments:
#   arg1            arg2   echo this string      N  echo some integers
# optional arguments:
#   -h, --help  show this help message and exit

# usage: ex4.py [-h] [--name NAME] [-up] --number {0,1,2} [--no-name]
parser.add_argument("--name")
parser.add_argument("-up", "--up_case", action="store_true", help="convert name to upper register")
parser.add_argument("--number", choices=[0, 1, 2], type=int, default=0, help="select number", required=True)
parser.add_argument("--no-name", action="store_const", const="no", dest="name")
# optional arguments:
#   -h, --help        show this help message and exit
#   --name NAME
#   -up, --up_case    convert name to upper register
#   --number {0,1,2}  select number
#   --no-name

args = parser.parse_args()  # запустить функцию парсинга

s = " ".join(map(lambda x: str(int(x, args.base)), args.integers))
# parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'), help='converted')
args.log.write(s + '\n')
args.log.close()

# python3 files/ex3.py 'one'    'two' 3 4   17
print(args.arg1)  # one
print(args.arg2)  # two
print(args.int_args)  # [3, 4, 17]
# args.number args.up_case args.name


'''
parser.add_argument('integers', metavar='integers', nargs='+', type=int, 
                    default=0, choices=[0, 1, 2], required=True,
                    action="store_const", const="no", dest="name",
                    help='integers to be converted')
                    
parser.add_argument('integers', nargs='?', type=int, 
                    default=0, choices=[0, 1, 2], required=True)
parser.add_argument('string', nargs='?', type=str)
parser.add_argument('true', action="store_const", const="no", dest="name")

ArgumentParser.add_argument(<name or flags> 
                [, help][, metavar][, type][,nargs][, default]
                [, action][, const][, choices][, required][, dest])

Фраза parser.add_argument("--no-name", action="store_const", const="no", dest="name") расшифровывается так:
Создать именованный параметр no-name
При его указании проинициализировать переменную с именем name (указано в параметре dest) значением no

name or flags - имя или список строк параметров, например foo или .-f, --foo
    >>> parser.add_argument('-f', '--foo')  # серией флагов, либо простым именем аргумента
    >>> parser.add_argument('bar')  # позиционный аргумент
action - основной тип действия, выполняемого, когда этот аргумент встречается в командной строке.
    action - простой флаг, принимающий значение true (store_true, store_false, store_const(в перем dest иди const)
    'store_const'- Здесь хранится значение, указанное аргументом ключевого слова const
    'store_true'и 'store_false'- они создают значения по умолчанию False и True
    'append'- Сохраняет список и добавляет в него значение каждого аргумента.
nargs - количество аргументов командной строки, которые следует использовать.
    '?'. Один аргумент
    '*'/'+'. Все имеющиеся аргументы командной строки собраны в список.
const - постоянное значение, необходимое для некоторых действий и выборок .
default - значение, создаваемое, если аргумент отсутствует в командной строке
type - Тип, в который должен быть преобразован аргумент командной строки.
choices - контейнер допустимых значений для аргумента.
required - Можно ли опустить параметр командной строки (аргумент является обязательным?). (True False)
help - краткое описание того, что делает аргумент.(вводится Текст подсказки)
metavar - имя аргумента в сообщениях об использовании. (отвечает за название параметра в подсказке (по умолч name)
dest - Имя атрибута, который будет добавлен к объекту, возвращаемому parse_args().
'''
