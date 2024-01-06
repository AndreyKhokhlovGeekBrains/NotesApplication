
class NoteBuilder:
    @staticmethod
    def build(id, header, note_body, date_time):
        note = {
                "ID": id, 
                "Header": header, 
                "Body": note_body, 
                "Date": date_time
                }
            
        return note