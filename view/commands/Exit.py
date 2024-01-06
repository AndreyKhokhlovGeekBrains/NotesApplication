
from view.commands.Command import Command


class Exit(Command):
    def __init__(self, view):
        super().__init__("Exit", view)
        
    def execute(self):
        self.get_view().exit()