from abc import ABC, abstractmethod

class InterfaceNoteItem(ABC):
    
    @abstractmethod
    def add_note(self, note):
       pass
    
    @abstractmethod   
    def assign_id(self):
        pass
    
    @abstractmethod
    def get_notes(self):
        pass
    
    @abstractmethod
    def set_notes(self, list_of_notes):
        pass