# интефейс взаимодействия с пользователем

# открытть файл
# сохранить файл
# показать контакт
# создать контакты
# изменить контакты
# найти контакты
# удалить контакты
# выход

# def show_contacts(data: list):
#     print('Фамилия:  ')


# изменить контакт


# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n')

# print(56)

path = 'file.txt'
data = open('file.txt', 'r')  #запись и чтение
for line in data:
    print(line)
data.close()