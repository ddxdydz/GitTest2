import argparse


def format_text_block(frame_height, frame_width, file_name):  # возвращает отформатированный текст
    try:
        with open(file_name, mode='rt', encoding='UTF-8') as file:
            read_data, output_data = file.readlines(), []

        def add_str(cur_s):
            nonlocal output_data
            if len(output_data) != frame_height:
                if len(cur_s) <= frame_width:
                    output_data.append(cur_s)
                else:
                    output_data.append(cur_s[:frame_width])
                    add_str(cur_s[frame_width:])

        for s in read_data:
            add_str(s.strip())
            if len(output_data) == frame_height:
                return '\n'.join(output_data)

    except Exception as e:
        return e


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', nargs='?', type=int, required=True, dest='height')
    parser.add_argument('--frame-width', nargs='?', type=int, required=True, dest='width')
    parser.add_argument('file_name', nargs='?', type=str)
    args = parser.parse_args()  # запустить функцию парсинга
    print(format_text_block(args.height, args.width, args.file_name))
