# все функции
from copy import deepcopy
import variable

phone_book = []
new_phone_book = []
path = 'phone_db.txt'


def open_file():
    global phone_book
    global new_phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            new = contact.strip().split(';')
            new_contact = {}
            new_contact['name'] = new[0]
            new_contact['phone'] = new[1]
            new_contact['comment'] = new[2]
            phone_book.append(new_contact)
    new_phone_book = deepcopy(phone_book)


def save_file():
    pass

def get_contacts():
    pass

def new_contact():
    pass

def change_contact():
    pass

def find_contact(msg) -> dict:
    path
    pass

def delete_contact():
    pass

def finish():
    pass