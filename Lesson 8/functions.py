def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    print(data)
    data_to_find = input('Введите данные для поиска: ')
    results = search(data, data_to_find)
    if len(results) == 0:
        print('Совпадений не найдено')
    elif len(results) == 1:
        print(results[0])
    else:
        print('Найдено несколько совпадений:')
        for i, result in enumerate(results, start=1):
            print(f'{i}. {result}')
        choice = input('Введите номер выбранного совпадения: ')
        try:
            choice = int(choice)
            if 1 <= choice <= len(results):
                print(results[choice - 1])
            else:
                print('Недопустимый номер совпадения')
        except ValueError:
            print('Некорректный ввод')


def search(book: str, info: str) -> list:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    results = []
    for contact in book:
        if info in contact:
            results.append(contact)
    return results