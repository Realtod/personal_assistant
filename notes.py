import json

with open("notes.json", "r") as file:
    notes = json.load(file)

class Note:
    def __init__(self, id, title, content, timestamp):
        try:
            self.id = int(id)
            self.title = str(title)
            self.content = str(content)
            self.timestamp = str(timestamp)
        except:
            print("Invalid type")

    def add_note(self):
         notes["notes"].append(self.id, self.title, self.content, self.timestamp)

    def get_notes(self):
        return notes["notes"]

    def get_note(self, id):
        return notes["notes"][id]

    def edit_note(self, id, title, content, timestamp):
        notes["notes"][id] = title
        notes["notes"][id] = content
        notes["notes"][id] = timestamp

    def delete_note(self, id):
        del notes["notes"][id]
