# Задача 38: Дополнить телефонный справочник возможностью изменения и 
# удаления данных. Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных
contacts = 'hmw-8/contacts.txt'

def show_data() -> str:
    with open(contacts, 'r', encoding='utf-8') as file:
        book = file.read()
    return book

def new_data() -> None:
    with open(contacts, 'a', encoding='utf-8') as file:
        file.write(input('Введите ФИО | номер телефона: ') + '\n')

def search() -> str:
    with open(contacts, 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        info = input('Поиск -> (ФИО либо номер телефона): ')
        for i in book:
            if info in i:
                print(i)

def replace() -> str:
    book = show_data().split('\n')
    for i in enumerate(book):
        print(i)
    res = int(input('Введите порядковый номер контакта которого хотели изменить: '))
    change = input('Введите изменение в выбранном контакте ли пустую строку, чтобы удалить этот контакт: ')
    book[res] = change
    print(book)
    with open(contacts, 'w', encoding='utf-8') as file:
        for i in book:
            file.write(str(i) + '\n')

while True:
    mode =  input('Выберите режим работы справочника (1-читение, 2-запись, 3-поиск, 4-изменить, 0-выход): ')
    if mode == '1':
        print(show_data())
    elif mode == '2':
        new_data()
    elif mode == '3':
        search()
    elif mode == '4':
        replace()
    elif mode == '0':
        break