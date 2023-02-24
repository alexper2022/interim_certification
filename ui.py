"""
Пользовательский интерфейс
"""
import time

from service import cls, pause, note_all, note_count, note_one_search, note_add, note_edit, note_del, note_search
from viewer import note_view


# основное меню
def menu():
    cls()
    print('МЕНЮ:')
    print('1. Просмотреть все заметки (только заголовки).')
    print('2. Просмотреть все заметки (полностью).')
    print('3. Просмотреть заметку по идентификатору.')
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
                # запрашиваем идентификатор заметки
                note_id = int(input('Введите идентификатор заметки: '))
                cls()
                # Выводим заметку полностью на экран
                note_view(note_one_search(note_id), True)
                del note_id
                pause()
                cls()
                menu()
            # 4. Добавить заметку.
            case 4:
                cls()
                # Запрашиваем текст новой заметки
                title = input('Введите краткое наименование (до 20 знаков):\n')
                note = input('Введите заметку:\n')
                # И записываем её в файл
                note_add(title, note)
                print("Заметка успешно добавлена\n")
                del title, note
                pause()
                cls()
                menu()
            # 5. Редактировать заметку.
            case 5:
                cls()
                # Запрашиваем номер строки для редактирования
                note_id = int(input('Введите идентификатор заметки для редактирования: '))
                cls()
                # для наглядности выводим заметку на экран
                note_view(note_one_search(note_id), True)
                # запрашиваем новый заголовок
                title = input("Введите заголовок:\n")
                # запрашиваем новый текст заметки
                note = input("Введите новый текст заметки:\n")
                # Запрашиваем подтверждение на удаление
                yes_no = input(f"\nВы действительно хотите удалить заметку {note_id}?\n"
                               f"Удаление не возможно отменить!\n"
                               f"Если согласны введите Д,д,Y,y и нажмите Enter: ")
                # если пользователь согласен с удалением
                if yes_no in ["Y", "y", "Д", "д"]:
                    # сохраняем измененную заметку
                    note_edit(note_id, title, note)
                    print("Отредактированная заметка успешно сохранена!")
                del note_id, title, note, yes_no
                pause()
                cls()
                menu()
            # 6. Найти заметку.
            case 6:
                cls()
                # Запрашиваем номер строки
                print('Пожалуйста введите данные:\n')
                yyyy = input('Введите год 4 цифры (2023): ')
                mm = input('Введите месяц 2 цифры (02): ')
                dd = input('Введите день 2 цифры (21): ')
                date = f'{yyyy}-{mm}-{dd}'
                try:
                    # проверяем верно ли введена дата
                    time.strptime(date, '%Y-%m-%d')
                    cls()
                    print(f"Ищем заметки по дате: {date}\n")
                    note_search(f'{yyyy}-{mm}-{dd}')
                except ValueError:
                    print('Вы ввели неправильную дату!')
                del yyyy, mm, dd, date
                pause()
                cls()
                menu()
            # 7. Удалить заметку.
            case 7:
                cls()
                # Запрашиваем номер строки для удаления
                note_id = int(input('Введите идентификатор заметки для удаления: '))
                # выводим заметку на экран
                note_view(note_one_search(note_id), True)
                # Запрашиваем подтверждение на удаление
                yes_no = input(f"\nВы действительно хотите удалить заметку {note_id}?\n"
                               f"Удаление не возможно отменить!\n"
                               f"Если согласны введите Д,д,Y,y и нажмите Enter: ")
                # если пользователь согласен с удалением
                if yes_no in ["Y", "y", "Д", "д"]:
                    # Удаляем запись
                    note_del(note_id)
                    cls()
                    print("Заметка успешно удалена!\n")
                    pause()
                del note_id, yes_no
                cls()
                menu()
            case _:
                cls()
                menu()
    except Exception as e:
        print(e)
        cls()
        menu()
