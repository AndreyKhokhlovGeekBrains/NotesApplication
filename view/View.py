from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def add_note(self):
        pass
    
    @abstractmethod
    def print_notes(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def delete_note(self):
        pass
    
    @abstractmethod
    def exit(self):
        pass