import cmd
from data import documents, directories


def command_handler(command):
    if command == 'q':
        cmd.close_program()

    elif command == 'p':
        cmd.get_name(documents)

    elif command == 's':
        cmd.get_shelf(directories)

    elif command == 'l':
        cmd.get_documents_list(documents)

    elif command == 'a':
        cmd.add_document(documents, directories)

    elif command == 'd':
        cmd.del_document(documents, directories)

    elif command == 'm':
        cmd.move_document(directories)

    elif command == 'as':
        cmd.add_shelf(directories)

    else:
        print('Ошибка, такой команды нет')


def main():
    print(
      'Система учета документов.',
      'Команды для управления: p, s, l, a, d, m, as, q',
      sep='\n'
    )
    while True:
        command = input('Введите команду: ')
        command_handler(command)


if __name__ == '__main__':
    main()