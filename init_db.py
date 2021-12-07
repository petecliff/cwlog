import sqlite3

conn = sqlite3.connect('cwlog.db')

with open('schema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("INSERT INTO items (item) VALUES (?)", ['Item 1'])
cur.execute("INSERT INTO items (item) VALUES (?)", ['Item 2'])

conn.commit()
conn.close()
