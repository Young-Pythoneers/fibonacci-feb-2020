import sqlite3


conn = sqlite3.connect('fibonacci.db')

cur = conn.cursor()

cur.execute('SELECT * FROM Fibonacci')

numbers = cur.fetchall()

for entry in numbers:
    print(f'{entry[0]} {entry[1]}')