import sqlite3

db = sqlite3.connect('database.lite')
cur = db.cursor()

# Создание таблицы
cur.execute("""CREATE TABLE notebook (
            note_title text ,
            note_body text,
            note_datetime text NOT NULL
            )""")
