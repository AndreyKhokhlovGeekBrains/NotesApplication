from abc import ABC, abstractmethod
from view.View import View

class Command(ABC):
    def __init__(self, description, view):
        self._description = description
        self._view = view
    
    def get_description(self):
        return self._description
    
    def get_view(self):
        return self._view
    
    @abstractmethod
    def execute(self):
        pass
