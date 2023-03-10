"""
Модуль вывода информации
"""


# Вывод информации из базы на экран:
# полностью     full=True
# или кратко    full=False
def note_view(note, full: bool):
    for el in note:
        if full:
            # выводим идентификатор, заголовок и заметку
            print(f"Заметка {el[0]}: {el[1]}\n"
                  f"Дата и время создания: {el[3][:19:]}\n"
                  f"{el[2]}\n")
        else:
            # выводим идентификатор и заголовок
            print(f"Заметка {el[0]}: {el[1]}\n"
                  f"Дата и время создания: {el[3][:16:]}\n")
