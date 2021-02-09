import argparse

# python3 file_copy.py --upper --lines 10 source.txt destination.txt
parser = argparse.ArgumentParser()
parser.add_argument('--upper', action="store_true")
parser.add_argument('--lines', nargs='?', type=int)
parser.add_argument('source', nargs='?', type=str)
parser.add_argument('destination', nargs='?', type=str)
args = parser.parse_args()  # запустить функцию парсинга

with open(args.source, mode='rt', encoding='UTF-8') as s_file:
    with open(args.destination, mode='wt', encoding='UTF-8') as d_file:
        read_data = s_file.readlines()
        n = args.lines if args.lines in range(0, len(read_data)) else len(read_data)
        read_data = ''.join(read_data[0: n])
        d_file.write(read_data.upper() if args.upper else read_data)
