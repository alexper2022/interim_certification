"""
Пользовательский интерфейс
"""
from service import cls, pause, note_all, note_count, note_one_search
from viewer import note_view


# основное меню
def menu():
    cls()
    print('МЕНЮ:')
    print('1. Просмотреть все заметки (только заголовки).')
    print('2. Просмотреть все заметки (полностью).')

    print('4. Добавить заметку.')
    print('5. Редактировать заметку.')
    print('6. Найти заметку.')
    print('7. Удалить заметку(по дате).')
    print('0. Выход из программы.')
    try:
        # Запрашиваем у пользователя пункт меню
        menu_number = int(input('Введите номер: '))
        match menu_number:
            # 0. Выход из программы(заголовки).
            case 0:
                cls()
                print('Спасибо, что пользуетесь нашей программой!')
                pause()
            # 1. Просмотреть все заметки (только заголовки).
            case 1:
                cls()
                # Выводим все заметки
                note_view(note_all(), False)
                print(f"Всего заметок в базе: {note_count()}")
                pause()
                cls()
                menu()
            # 2. Просмотреть все заметки (полностью).
            case 2:
                cls()
                # Выводим все заметки
                note_view(note_all(), True)
                print(f"Всего заметок в базе: {note_count()}")
                pause()
                cls()
                menu()
            # 3. Просмотреть заметку полностью.
            case 3:
                cls()
                note_id = int(input('Введите идентификатор заметки: '))
                cls()
                note_view(note_one_search(note_id), True)
                pause()
                cls()
                menu()
            case 4:
                pass
            case 5:
                pass
            case _:
                cls()
                menu()
    except Exception as e:
        print(e)
        cls()
        menu()
