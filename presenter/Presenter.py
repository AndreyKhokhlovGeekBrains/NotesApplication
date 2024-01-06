from model.Service import Service

class Presenter:
    def __init__(self):
        self.service = Service()
    
    def add_note(self, header, body, date):
        self.service.add_note(header, body, date)
        
    def save(self):
        self.service.save()
    
    def print_notes(self):
        self.service.print_notes()
        
    def get_by_id(self):
        return self.service.get_by_id()
        
    def edit_note(self):
        self.service.edit_note()
        
    def delete_note(self):
        return self.service.delete_note()
