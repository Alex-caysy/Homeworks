import sqlite3

connections = sqlite3.connect('Products.db')
cursor = connections.cursor()


def initiate_db():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
);
''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')
    connections.commit()


def get_all_products():
    all_db = cursor.execute('SELECT * FROM Products').fetchall()
    return all_db


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', '1000'))
    connections.commit()


def is_included(username):
    cursor.execute('SELECT EXISTS(SELECT id FROM Users WHERE username = ?)', (username,))
    return cursor.fetchone()[0]
