
from datetime import datetime
from model.Notes import Notes
from model.FileHandler import FileHandler
from model.NoteBuilder import NoteBuilder

class Service:
    
    def __init__(self):
        self.my_notes = Notes()
    
    def add_note(self, header, body, date):
        note_id = self.my_notes.assign_id()
        note = NoteBuilder.build(note_id, header, body, date)
        self.my_notes.add_note(note)
        print(note)
        
    def save(self):
        all_notes = self.my_notes.get_notes()
        FileHandler.save(all_notes)
    
    def print_notes(self):
        all_notes = self.my_notes.get_notes()
        print(f'Total number of notes: {len(all_notes)}')
        for note in all_notes:
            print(f'ID: {note["ID"]}, Header: {note["Header"]}, Body: {note["Body"]}, Date: {note["Date"]}')
        print()
        
    def select_ID(self):
        data = self.my_notes.get_notes()
        if data:
            existing_ids = [note["ID"] for note in data]
        
        selected_ID = None
        self.print_notes()
        while selected_ID not in existing_ids:
            try:
                selected_ID = int(input("Enter the ID for the note: "))
                print()
            except ValueError:
                print("Incorrect input. Enter a number")
                continue
            
            if selected_ID not in existing_ids:
                print("Incorrect ID. Please enter an existing ID.")
        return selected_ID
        
    def get_by_id(self, id=None):
        if id == None:
            selected_id = self.select_ID()
        else:
            selected_id = id
            
        data = self.my_notes.get_notes()
        selected_note = next((note for note in data if note["ID"] == selected_id), None)
        return selected_note
    
    def edit_note(self):
        cmd = 0
        selected_ID = self.select_ID()          
        
        while cmd not in ('1', '2'):
            print("Select command:\n"
                "1. Change name\n"
                "2. Change note body\n")
            cmd = input("Enter command: ")
            
            match cmd:
                case '1':
                    self.change_name(selected_ID)
                case '2':
                    self.change_body(selected_ID)
                    
    def change_name(self, note_id):
        note_to_change = self.get_by_id(note_id)
        if note_to_change:
            note_to_change["Header"] = input("Enter new header:\n")
            note_to_change["Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_changes(note_to_change)
    
    def save_changes(self, updated_note):
        data = self.my_notes.get_notes()
        for note in data:
            if note["ID"] == updated_note["ID"]:
                note.update(updated_note)
                
    def change_body(self, id):
        note_to_change = self.get_by_id(id)
        if note_to_change:
            note_to_change["Body"] = input("Enter new note body:\n") 
            note_to_change["Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_changes(note_to_change)
            
    def delete_note(self):
        selected_ID = self.select_ID()
        data = self.my_notes.get_notes()
        updated_data = [note for note in data if note["ID"] != selected_ID]
        self.my_notes.set_notes(updated_data)
        self.print_notes()
                  