# все функции

# def open_file()

# def save_file()

def find_file():
    with open ('phonebook.txt', 'r') as data:
        contact = input('Пожалуйста, задайте фамилию адресата для поиска: ')
        lines = data.readlines()

        found = False
        for line in lines:
            if contact in line:
                print("Вот контакт, который Вы искали: ", end=' ')
                print(line)
                found = True
                break
        if found == False:
            print("Контакта с такой фамилией нет")
    pass

def change_file():
    fin = open('phonebook.txt', 'r')
    data = fin.read()
    print("Вот все записи справочника: ", end=' ')
    print(data)
    text_1 = str(input("Введите запись, которую Вы хотете заменить: ", end=' '))
    text_2 = str(input("На что вы хотите заменить: ", end=' '))
    data = data.replace(text_1, text_2)
    fin.close()
    fin = open('phonebook.txt', 'w')
    fin.write(data)
    fin.close
    pass

def delete_file():
    f = open('phonebook.txt', 'r')
    lines = f.readlines()
    f.close()
    f = open('phonebook.txt', 'w')
    line_del = int(input("Введите номер строки для удаления: "))
    for line in lines:
        if line != line_del:
            f.write(line)
    f.close()
    pass

def finish_file():
    quit()
