import os
import sqlite3


# Функция очистки экрана для терминала, должна работать на Win и на MAC
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Функция паузы для терминала, должна работать на Win и на MAC
def pause():
    os.system('pause' if os.name == 'nt' else 'read -s -n 1 -p "Для продолжения нажмите любую клавишу..."')


def note_add():
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute()


def note_del():
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute()


def note_edit():
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute()


def note_search():
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute("")


def note_count():
    with sqlite3.connect('database.lite') as db:
        cur = db.cursor()
        cur.execute("")
