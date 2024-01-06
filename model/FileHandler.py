import json

class FileHandler:
    @staticmethod
    def save(data):
         with open(".\\model\\Notes.json", "w") as file:
            json.dump(data, file, indent=2)
    
    @staticmethod
    def read():
        try:
            with open(".\\model\\Notes.json", "r") as file:
                data = file.read()
                if data:
                    notes = json.loads(data)
                else:
                    notes = []
        except FileNotFoundError:
            notes = []
        return notes