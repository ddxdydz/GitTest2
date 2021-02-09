import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--no-name", action="store_const", const="no", dest="name")
args = parser.parse_args()  # запустить функцию парсинга

print(args.name)
