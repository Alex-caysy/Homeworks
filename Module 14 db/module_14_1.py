import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# Заполняю таблицу значениями.
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))

# Первый способ(доступ по id когда известно количество). Меняю значения в каждой 2-ой строке.
for _id in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, _id))

list_id = cursor.execute('SELECT id FROM Users').fetchall()
# Второй способ.
for i in range(1, len(list_id) + 1, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

result = cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60').fetchall()
# Третий способ (Через список элементов).
for user, email, age, balance in result:
    print(f'Имя: {user} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

connection.commit()
connection.close()
