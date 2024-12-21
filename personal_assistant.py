import csv
import pandas as pd
import time
import json
from notes import Note

print("Добро пожаловать в Персональный помощник! \nВыберите действие: \n1. Управление заметками \n2. Управление задачами \n3. Управление контактами \n4. Управление финансовыми записями \n5. Калькулятор \n6. Выход")

match(input()):
    case '1':
        print("Что вы хотите сделать? \n 1. Создать заметку \n 2. Просмотреть список всех заметок \n 3. Просмотр подробностей заметки \n 4. Редактирование заметки \n 5. Удаление заметки \n 6. Экспорт заметки в формате csv")
        match(input()):
            case '1':
                print("Укажите: \n 1. ID \n 2. Title \n 3. Content")
                id = int(input())
                title = str(input())
                content = str(input())
                note = Note(id, title, content, time.time())
                with open("notes.json", "w") as file:
                    notes = json.load(file)
                notes.append(note)
