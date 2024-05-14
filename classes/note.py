import json


class Note():
    notehash = dict()

    @classmethod
    def load(cls):
        with open("classes/note.json", "r")as f:
            Note.notehash = json.load(f)

    @classmethod
    def save(cls):

        with open("classes/note.json", "w")as f:
            json.dump(Note.notehash, f, indent=4)

    def __str__(self) -> str:
        return f"{self.title}:{self.text}"


Note.load()


