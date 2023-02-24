import os
import sqlite3
from datetime import datetime


# Функция очистки экрана для терминала, должна работать на Win и на MAC
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Функция паузы для терминала, должна работать на Win и на MAC
def pause():
    os.system('pause' if os.name == 'nt' else 'read -s -n 1 -p "Для продолжения нажмите любую клавишу..."')


# Запись строки str_data в файл
def note_add(title: str, data: str):
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute(
            f"INSERT INTO notebook (note_title, note_body, note_datetime) VALUES ('{title[:20:]}', '{data}', '{datetime.now()}');")


# Удаление строки с номером note_id из файла
def note_del(note_id: int):
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute(f"DELETE FROM notebook WHERE rowid = '{note_id}'")
        db.commit()


# Изменение строки с номером num из файла
def note_edit(note_id: int, title: str, note: str):
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute(f"UPDATE notebook SET note_title = '{title}', note_body = '{note}' WHERE rowid = '{note_id}'")


def note_search():
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute("")


# Определение количества строк в файле
def note_count():
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM notebook;")
        # items = cur.fetchall()
    return len(cur.fetchall())


# Формирование всех заметок в базе
def note_all():
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute("SELECT rowid, * FROM notebook;")
        return cur.fetchall()


def note_one_search(note_id: int):
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        # cur.execute("SELECT * FROM entry;")
        cur.execute(f"SELECT rowid, * FROM notebook WHERE rowid = '{note_id}'")
        return cur.fetchall()
