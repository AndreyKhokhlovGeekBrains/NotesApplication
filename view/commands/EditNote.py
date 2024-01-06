from view.commands.Command import Command

class EditNote(Command):
    def __init__(self, view):
        super().__init__("Edit note", view)
        
    def execute(self):
        self.get_view().edit_note()