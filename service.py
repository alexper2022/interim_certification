import os
import sqlite3
from datetime import datetime

from viewer import note_view


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
            f"INSERT INTO notebook (note_title, note_body, note_datetime) "
            f"VALUES ('{title[:20:]}', '{data}', '{datetime.now()}');")


# Удаление строки с номером note_id из файла
def note_del(note_id: int):
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute(f"DELETE FROM notebook WHERE rowid = '{note_id}'")
        db.commit()


# Изменение строки c идентификатором note_id
# изменяем в заметке: заголовок на title и заметку note
def note_edit(note_id: int, title: str, note: str):
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute(f"UPDATE notebook SET note_title = '{title}', note_body = '{note}' WHERE rowid = '{note_id}'")


# Вывод на экран строки
def note_search(date: str):
    # получаем все записи в базе
    items = note_all()
    # Перебираем записи
    for el in items:
        # и если дата совпала,
        if el[3][:10:] == date:
            # выводим на экран
            note_view([el], True)


# Определение количества строк в файле
def note_count():
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        # Получаем все записи в базе
        cur.execute("SELECT * FROM notebook;")
    # возвращаем количество записей
    return len(cur.fetchall())


# Получаем все заметки в базе
def note_all():
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        # Получаем из базы все строки
        cur.execute("SELECT rowid, * FROM notebook;")
        # и возвращаем их
        return cur.fetchall()


# Ищем заметку с идентификатором note_id
def note_one_search(note_id: int):
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        # Получаем из базы строку с идентификатором note_id
        cur.execute(f"SELECT rowid, * FROM notebook WHERE rowid = '{note_id}'")
        # и возвращаем её
        return cur.fetchall()
