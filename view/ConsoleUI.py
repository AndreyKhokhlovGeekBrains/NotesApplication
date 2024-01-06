from datetime import datetime
from view.View import View
from view.MainMenu import MainMenu
from presenter.Presenter import Presenter

class ConsoleUI(View):
    def __init__(self):
        super().__init__()
        self.check = True
        self.main_menu = MainMenu(self)
        self.presenter = Presenter()
        
    def prin_menu(self):
        self.main_menu.print_menu()
        
    def scan_menu(self):
        try:
            cmd = int(input("Enter command number: "))
            if cmd > 0 and cmd <= self.main_menu.last_command_num():
                print()
                self.main_menu.execute(cmd)
            else: 
                print("Invalid input. Please enter a valid integer.")
                print()
            
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            print()
            
    def start(self):
        print("Hello!")
        while self.check:
            self.prin_menu()
            print()
            self.scan_menu()
            
    def enter_header(self):
        return input("Enter note name: ").title()

    def enter_note_body(self):
        return input("Enter note body: ")

    def get_current_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    def add_note(self):
        note_header = self.enter_header()
        note_body = self.enter_note_body()
        note_date = self.get_current_datetime()
        self.presenter.add_note(note_header, note_body, note_date)

    def delete_note(self):
        self.presenter.delete_note()

    def exit(self):
        print("Bye-bye")
        print()
        self.check = False

    def print_notes(self):
        self.presenter.print_notes()

    def save(self):
        self.presenter.save()
        
    def get_by_id(self):
        note = self.presenter.get_by_id()
        print(f'{note}\n')
        
    def edit_note(self):
        self.presenter.edit_note()