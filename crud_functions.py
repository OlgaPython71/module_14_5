import sqlite3


def initiate_db():
    connection = sqlite3.connect('product_base.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')
    connection.commit()
    #cursor.execute('CREATE INDEX IF NOT EXISTS idx_title ON Products (title)')
    #for i in range(1, 5):
    #    cursor.execute('INSERT INTO Products (title, description, price) VALUES(?,?,?)',
    #                   (f'Продукт{i}', f'Описание{i}', i * 100))
        #cursor.execute('DELETE FROM Products')

    #connection.commit()
    #connection.close()

def add_user(username, email, age):
    connection = sqlite3.connect('product_base.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) "
                   "VALUES (?, ?, ?, ?)", (username, email, age, "1000"))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('product_base.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?;', (username,))
    user = cursor.fetchone()
    connection.commit()
    connection.close()
    return bool(user)


def get_all_products():
    connection = sqlite3.connect('product_base.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    connection.commit()
    connection.close()
    return products


initiate_db()
