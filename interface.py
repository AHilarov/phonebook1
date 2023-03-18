from tabulate import tabulate
import variable

def menu():
    print('''\nMain menu:
    1. Отрыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Создать контакт
    5. Изменить контакт
    6. Найти контакт
    7. Delete contact
    8. Exit
    \n{variable.menu_selection}''', end='')
    while True:
        try:
            user_input = int(input())
            if 0 < user_input < 9:
                return user_input
            else:
                print(variable.error)
        except:
            print(variable.error)


def show_contacts(data: list):
    print(tabulate(data, headers=variable.first_line))