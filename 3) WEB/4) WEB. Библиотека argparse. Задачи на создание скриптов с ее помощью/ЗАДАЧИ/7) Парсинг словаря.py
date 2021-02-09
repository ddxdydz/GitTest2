import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--sort', action="store_true")
parser.add_argument('keys', nargs='+', type=str)

args = parser.parse_args()  # запустить функцию парсинга

data_dict = dict()
for elem in args.keys:
    key, value = elem.split('=')
    data_dict[key] = value

keys = [f'Key: {key}\tValue: {value}' for key, value in data_dict.items()]
keys = sorted(keys) if args.sort else keys
print(*keys, sep='\n')
