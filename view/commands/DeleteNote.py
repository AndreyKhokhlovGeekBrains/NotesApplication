from view.commands.Command import Command

class DeleteNote(Command):
    def __init__(self, view):
        super().__init__("Delete note", view)
        
    def execute(self):
        self.get_view().delete_note()