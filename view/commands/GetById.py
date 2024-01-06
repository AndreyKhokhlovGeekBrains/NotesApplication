from view.commands.Command import Command

class GetByID(Command):
    def __init__(self, view):
        super().__init__("Get note by id", view)
        
    def execute(self):
        self.get_view().get_by_id()