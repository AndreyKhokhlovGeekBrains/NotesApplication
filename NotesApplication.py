# Реализовать консольно еприложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок. Заметка должна содержать идентификатор, заголовок, телозаметкии дату/время создания или последнего изменения заметки. Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё,на усмотрение студента.

from datetime import datetime
import json
import pprint

def assign_id():
    try:
        with open("Notes.json", "r") as file:
            data = json.load(file)
            if data:
                existing_ids = [note["ID"] for note in data]
                new_id = max(existing_ids) + 1
            else:
                new_id = 1
    except FileNotFoundError:
        new_id = 1
    return new_id

def enter_header():
    return input("Введите название заметки: ").title()

def enter_note_body():
    return input("Введите тело заметки: ")

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_note():
    id = 1
    header = enter_header()
    body = enter_note_body()
    date_time = get_current_datetime()
    
    note = [
            {
                "ID": id, 
                "Header": header, 
                "Body": body, 
                "Date": date_time
            }
            ]
      
    with open("Notes.json", "w") as file:
        json.dump(note, file, indent=2)

def add_note():
    try:
        with open("Notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    id = assign_id()
    header = enter_header()
    body = enter_note_body()
    date_time = get_current_datetime()

    new_note = {
        "ID": id,
        "Header": header,
        "Body": body,
        "Date": date_time
    }

    notes.append(new_note)

    with open("Notes.json", "w") as file:
        json.dump(notes, file, indent=2)
        
def get_notes():
    try:
        with open("Notes.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Не найден файл.")
        return []

def print_notes():
    data = get_notes()
    pprint.pprint(data, indent=2, width=40)
    print("\n")
    
def save_changes(updated_note):
    data = get_notes()
    for note in data:
        if note["ID"] == updated_note["ID"]:
            note.update(updated_note)
                
    with open("Notes.json", "w") as file:
        data = json.dump(data, file, indent=2)
    
def get_by_id(note_id):
    data = get_notes()
    selected_note = next((note for note in data if note["ID"] == note_id), None)
    return selected_note

def change_name(note_id):
    note_to_change = get_by_id(note_id)
    if note_to_change:
        note_to_change["Header"] = input("Введите новое название:\n")
        note_to_change["Date"] = get_current_datetime()
        save_changes(note_to_change)
    
def change_body(note_id):
    note_to_change = get_by_id(note_id)
    if note_to_change:
        note_to_change["Body"] = input("Введите новую заметку:\n") 
        note_to_change["Date"] = get_current_datetime()
        save_changes(note_to_change)
        
def select_ID():
    data = get_notes()
    if data:
        existing_ids = [note["ID"] for note in data]
    
    selected_ID = None
    while selected_ID not in existing_ids:
        try:
            selected_ID = int(input("Введите ID нужной записи: "))
        except ValueError:
            print("Некорректный ввод. Введите число.")
            continue
        
        if selected_ID not in existing_ids:
            print("Некорректный ID. Пожалуйста, выберите существующий ID.")
    return selected_ID
    
def edit_note():
    cmd = 0
    selected_ID = select_ID()          
    
    while cmd not in ('1', '2'):
        print("Выбирите действие:\n"
            "1. Изменить название\n"
            "2. Изменить тело заметки\n")
        cmd = input("Введите действие: ")
        
        match cmd:
            case '1':
                change_name(selected_ID)
            case '2':
                change_body(selected_ID)

def search_note():
    selected_ID = select_ID()               
    return print(f'{get_by_id(selected_ID)} \n')

def delete_note():
    selected_ID = select_ID()
    data = get_notes()
    updated_data = [note for note in data if note["ID"] != selected_ID]
    try:
        with open("Notes.json", "w") as file:
            json.dump(updated_data, file, indent=2)
    except FileNotFoundError:
        print("Не найден файл.")
    
def user_interface():
    cmd = 0
    while cmd != '7':
        print("Выбирите дествие:\n"
              "1. Создать новую заметку\n"
              "2. Добавить заметку к уже существующим\n"
              "3. Редактировать заметку\n"
              "4. Вывести все заметки\n"
              "5. Поиск заметки\n"
              "6. Удалить заметку\n"
              "7. Выход\n")
        cmd = input("Введите действие: ")
        while cmd not in ('1', '2', '3', '4', '5', '6', '7'):
            print("Некорректный ввод")
            cmd = input("Введите действие: ")
        
        match cmd:
            case '1':
                create_note()
            case '2':
                add_note()
            case '3':
                edit_note()
            case '4':
                print_notes()
            case '5':
                search_note()
            case '6':
                delete_note()
            case '7':
                print("Всего доброго!\n")
                
user_interface()
