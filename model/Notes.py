from model.NoteItemInterface import InterfaceNoteItem
from model.FileHandler import FileHandler

class Notes(InterfaceNoteItem):
    def __init__(self):
        self._list_of_notes = FileHandler().read()
        
    def add_note(self, note):
       self._list_of_notes.append(note)
       
    def assign_id(self):
        if self._list_of_notes:
            existing_ids = [note["ID"] for note in self._list_of_notes]
            new_id = max(existing_ids) + 1
        else:
            new_id = 1
        return new_id
    
    def get_notes(self):
        return self._list_of_notes
    
    def set_notes(self, list_of_notes):
        self._list_of_notes = list_of_notes

    