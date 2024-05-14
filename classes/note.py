import json


class Note():

    def __init__(self, title, text):
        self.title = title
        self.text = text

    @classmethod
    def load(cls):
        with open("classes/note.json", "r")as f:
            data = json.load(f)
            result = []
        for key, value in data.items():
            result.append(Note(key, value["text"]))
        return result

    @classmethod
    def save(cls, list):
        result = {}

        for task in list:
            result[task.title] = {"text": task.text}

            with open("classes/note.json", "w")as f:
                json.dump(result, f, indent=4)

    def __str__(self) -> str:
        return f"{self.title}:{self.text}"
