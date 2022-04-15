def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def write_file(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text)


def main():
    files = ['1.txt', '2.txt', '3.txt']

    text_dict = {}
    for file in files:
        file_name = f'{file}'
        file_text = f'{read_file(file)}'
        file_line_count = len(file_text.split('\n'))
        if file_line_count in text_dict.keys():
            text_dict[file_line_count] += [f'{file_name}\n{file_line_count}\n{file_text}\n']
        else:
            text_dict[file_line_count] = [f'{file_name}\n{file_line_count}\n{file_text}\n']

    final_file_text = ''
    for key in sorted(text_dict.keys()):
        for text in text_dict[key]:
            final_file_text += text

    write_file('final_file.txt', final_file_text)


if __name__ == '__main__':
    main()
