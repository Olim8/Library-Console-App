import booksSDK

booksList = []
def print_menu():
    print()
    print()
    print('*** Управление библиотекой ***')
    print('Выберите целое число для продолжения')
    print('1. Добавление книги')
    print('2. Удаление книги')
    print('3. Поиск книги')
    print('4. Отображение всех книг')
    print('5. Изменение статуса книги')
    print('6-*. Выход из программы')


while True:
    print_menu()
    try:
        r = int(input())
        if r == 1:
            try:
                title = input('Введите название книги: ')
                author = input('Введите автор книги: ')
                year = int(input('Введите год издания: '))
                status = 'в наличии'
                book = [(title, author, year, status)]
                booksSDK.addBook(book)
                print('Книга была добавлена!')
            except:
                print('Неправильные данные, повторите попытку')
        elif r == 2:
            try:
                id = int(input('Введите id книги для удаления: '))
                booksSDK.delete(id)
            except:
                print('Неправильные данные, повторите попытку')
        elif r == 3:
            try:
                searchable = input('Введите название или год выпуска или автора книги чтобы найти: ')
                booksSDK.search(searchable)
            except:
                print('Неправильные данные, повторите попытку')
        elif r == 4:
            for book in booksSDK.viewAll():
                print(book)
        elif r == 5:
            try:
                id = int(input('Введите id книги для изменения статуса: '))
                booksSDK.changeStatus(id)
            except:
                print('Неправильные данные, повторите попытку')
        else:
            print('Выход из программы')
            break
    except:
        print('Вы не ввели целое число')
    
