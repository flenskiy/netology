def get_name(documents):
    number = input('Введите номер документа: ')

    for document in documents:
        if document['number'] == number:
            print(f'Имя: {document["name"]}')
            return

    print('Ошибка, нет документа с таким номером')


def get_shelf(directories):
    number = input('Введите номер документа: ')

    for shelf in directories:
        if number in directories[shelf]:
            print(f'Номер полки: {shelf}')
            return

    print('Ошибка, нет документа с таким номером')


def get_documents_list(documents):
    if len(documents) != 0:
        for document in documents:
            print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')

    else:
        print('Записей нет')


def add_document(documents, directories):
    number = input('Укажите номер документа: ')
    type = input('Укажите тип документа: ')
    name = input('Укажите имя владельца: ')
    shelf = input('Укажите номер полки: ')

    for document in documents:
        if number == document['number']:
            print('Ошибка, документ с таким номером уже существует')
            return

    if shelf in directories.keys():
        document_dict = {'type': type, 'number': number, 'name': name}
        documents.append(document_dict)
        directories[shelf].append(number)
        print('Записи успешно добавлены')

    else:
        print('Ошибка, нет полки с таким номером')


def del_document(documents, directories):
    number = input('Укажите номер документа: ')

    for document in documents:
        if document['number'] == number:
            documents.remove(document)
            for shelf in directories:
                if number in directories[shelf]:
                    directories[shelf].remove(number)
                    print('Записи успешно удалены')
                    return

    print('Ошибка, нет документа с таким номером')


def move_document(directories):
    number = input('Укажите номер документа: ')

    for shelf in directories:
        if number in directories[shelf]:
            new_shelf = input('Укажите номер полки: ')
            if new_shelf in directories.keys():
                directories[shelf].remove(number)
                directories[new_shelf].append(number)
                print('Запись успешно перемещена')
                return

            else:
                print('Ошибка, нет полки с таким номером')
                return

    else:
        print('Ошибка, нет документа с таким номером')


def add_shelf(directories):
    new_shelf = input('Укажите номер новой полки: ')

    if new_shelf not in directories.keys():
        directories[new_shelf] = []
        print('Полка успешно добавлена')

    else:
        print('Ошибка, полка с таким именем уже существует')


def close_program():
    raise SystemExit(0)
