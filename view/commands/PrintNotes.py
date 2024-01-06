from view.commands.Command import Command

class PrintNotes(Command):
    def __init__(self, view):
        super().__init__("Print notes", view)
        
    def execute(self):
        self.get_view().print_notes()