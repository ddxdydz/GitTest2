import sys
import argparse


try:
    parser = argparse.ArgumentParser()

    parser.add_argument('--count', action="store_true")
    parser.add_argument('--num', action="store_true")
    parser.add_argument('--sort', action="store_true")
    parser.add_argument('file_name', nargs='?', type=str)

    args = parser.parse_args()  # запустить функцию парсинга

    with open(args.file_name, 'rt', encoding='UTF-8') as file:
        read_data = file.read().split('\n')

    if args.sort:  # для сортировки строк в алфавитном порядке перед выводом
        read_data.sort()
    if args.num:  # для вывода порядкового номера с пробелом в начале каждой строки
        read_data = list(map(lambda elem: f'{elem[0]} {elem[1]}', enumerate(read_data)))
    if args.count:  # для вывода кол-ва строк в конце сообщения
        read_data.append(f'rows count: {len(read_data)}')

    print('\n'.join(read_data))

except Exception:
    print('ERROR')
