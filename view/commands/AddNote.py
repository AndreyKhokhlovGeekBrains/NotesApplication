from view.commands.Command import Command

class AddNote(Command):
    def __init__(self, view):
        super().__init__("Add/create note", view)
        
    def execute(self):
        self.get_view().add_note()