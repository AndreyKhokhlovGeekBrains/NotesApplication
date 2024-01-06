from view.commands.PrintNotes import PrintNotes
from view.commands.AddNote import AddNote
from view.commands.Save import Save
from view.commands.Exit import Exit
from view.commands.GetById import GetByID
from view.commands.EditNote import EditNote
from view.commands.DeleteNote import DeleteNote

class MainMenu:
    def __init__(self, view):
        super().__init__()
        self.command_list = [
                PrintNotes(view),
                AddNote(view),
                EditNote(view),
                GetByID(view),
                DeleteNote(view),
                Save(view),
                Exit(view)  
            ]
    
    def print_menu(self):
        for index, command in enumerate(self.command_list, start=1):
            print(f"{index}. {command.get_description()}")
        
    def execute(self, cmd):
        self.command_list[cmd - 1].execute()
        
    def last_command_num(self):
       command_num = len(self.command_list)
       return command_num