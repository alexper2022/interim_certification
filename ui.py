"""
Пользовательский интерфейс
"""
from service import cls, pause


# основное меню
def menu():
    cls()
    print('МЕНЮ:')
    print('1. Просмотреть все заметки.')
    print('2. Добавить заметку.')
    print('3. Редактировать заметку.')
    print('4. Найти заметку.')
    print('5. Удалить заметку.')
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
            # 1. Просмотреть все заметки.
            case 0:
                cls()
                print('Спасибо, что пользуетесь нашей программой!')
                pause()
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
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
