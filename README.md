RU:
Консольное приложение для управления библиотекой книг написанный в python и подключен БД sqlite3.
Приложение позволяет добавлять, удалять, искать и отображать книги. Каждая книга содержит следующие поля:
 • id (уникальный идентификатор, генерируется автоматически)
 • title (название книги)
 • author (автор книги)
 • year (год издания)
 • status (статус книги: “в наличии”, “выдана”)
 
 Написал функции для каждой операции (добавление, удаление, поиск, отображение, изменение статуса).
 Применил объектно-ориентированный подход программирования

 Требования
 1. Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку
    с уникальным id и статусом “в наличии”.
 2. Удаление книги: Пользователь вводит id книги, которую нужно удалить.
 3. Поиск книги: Пользователь может искать книги по title, author или year.
 4. Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.
 5. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).


EN:
Console application for managing a library of books written in python and connected to sqlite3 database.
The application allows you to add, delete, search and display books. Each book contains the following fields:
• id (unique identifier, generated automatically)
• title (title of the book)
• author (author of the book)
• year (year of publication)
• status (book status: “in stock”, “issued”)

Wrote functions for each operation (add, delete, search, display, change status).
Applied object-oriented programming approach

Requirements
1. Adding a book: The user enters the title, author and year, after which the book is added to the library
with a unique id and the status “in stock”.
2. Deleting a book: The user enters the id of the book to be deleted.
3. Searching for a book: The user can search for books by title, author or year.
4. Displaying all books: The application displays a list of all books with their id, title, author, year and status.
5. Changing the status of a book: The user enters the id of the book and the new status (“in stock” or “issued”).
