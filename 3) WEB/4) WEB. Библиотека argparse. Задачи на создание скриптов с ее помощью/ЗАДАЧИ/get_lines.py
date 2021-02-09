import argparse


def count_lines(path_file):
    try:
        with open(path_file, mode='rt', encoding='UTF-8') as file:
            return len(file.readlines())
    except Exception:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_name', nargs='?', type=str)
    args = parser.parse_args()  # запустить функцию парсинга
    print(count_lines(args.file_name))
