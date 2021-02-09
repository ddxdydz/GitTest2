import sys


try:
    args = sys.argv[1:]
    file_name = [elem for elem in args if '.' in elem][0]
    keys = [elem for elem in args if '--' in elem]

    with open(file_name, 'rt', encoding='UTF-8') as file:
        read_data = file.read().split('\n')

    if '--sort' in keys:  # для сортировки строк в алфавитном порядке перед выводом
        read_data.sort()
    if '--num' in keys:  # для вывода порядкового номера с пробелом в начале каждой строки
        read_data = list(map(lambda elem: f'{elem[0]} {elem[1]}', enumerate(read_data)))
    if '--count' in keys:  # для вывода кол-ва строк в конце сообщения
        read_data.append(f'rows count: {len(read_data)}')

    print('\n'.join(read_data))

except Exception:
    print('ERROR')
