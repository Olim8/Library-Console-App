import sqlite3
from book import Book

def cursor():
    return sqlite3.connect('books.db').cursor()

cur = cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS books 
            (book_id INTEGER PRIMARY KEY, 
             title VARCHAR(100) NOT NULL, 
             author VARCHAR(100) NOT NULL, 
             year INT NOT NULL, 
             status TEXT)''')
cur.connection.close()


def addBook(book):
    cur = cursor()
    with cur.connection:
        cur.executemany('INSERT INTO books(title, author, year, status) VALUES (?, ?, ?, ?)', (book))
    cur.connection.close()


def viewAll():
    cur = cursor()
    booksList = []
    with cur.connection:
        for book in cur.execute('SELECT * FROM books'):
            booksList.append(Book(book[0], book[1], book[2], book[3], book[4]))
    cur.connection.close()
    return booksList
    

def delete(id):
    cur = cursor()
    with cur.connection:
        cur.execute('SELECT * FROM books WHERE book_id = ?', (id,))
        row = cur.fetchone()
        if row:
            cur.execute('DELETE FROM books WHERE book_id = ?', (id,))
            print('Книга была удалена')
        else:
            print('Книги нет в списке')
    cur.connection.close()


def search(searchable):
    cur = cursor()
    with cur.connection:
        cur.execute('SELECT * FROM books WHERE title = ? OR author = ? OR year = ?', (searchable, searchable, searchable))
        data = cur.fetchone()  

        if not data:
            print('Книги нет в списке')
        else:
            print(data) 
    cur.connection.close()


def changeStatus(id):
    cur = cursor()
    with cur.connection:
        cur.execute('SELECT * FROM books WHERE book_id = ?', (id,))
        row = cur.fetchone()
        if row:
            cur.execute('UPDATE books SET status = "выдана" WHERE book_id = ?', (id,))
            print('Изменен статуса книги')
        else:
            print('Книги нет в списке')
    cur.connection.close()
