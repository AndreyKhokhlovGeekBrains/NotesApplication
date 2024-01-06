from view.commands.Command import Command

class Save(Command):
    def __init__(self, view):
        super().__init__("Save", view)
        
    def execute(self):
        self.get_view().save()