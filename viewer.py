"""
Модуль вывода информации
"""


def note_view(note, full: bool):
    for el in note:
        if full:
            print(f"Заметка {el[0]}: {el[1]}\n"
                  f"Дата и время создания: {el[3][:19:]}\n"
                  f"{el[2]}\n")
        else:
            print(f"Заметка {el[0]}: {el[1]}\n"
                  f"Дата и время создания: {el[3][:16:]}\n")
