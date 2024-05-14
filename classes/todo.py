import json


class Todo():
    def __init__(self, title, descraibe):
        self.title = title
        self.descraibe = descraibe

    @classmethod
    def load(cls):
        with open("classes/todo.json", "r")as f:
            data = json.load(f)
            result = []
        for key, value in data.items():
            result.append(Todo(key, value["descraibe"]))
        return result

    @classmethod
    def save(cls, list):
        result = {}

        for task in list:
            result[task.title] = {"descraibe": task.descraibe}

            with open("classes/todo.json", "w")as f:
                json.dump(result, f, indent=4)

    def __str__(self) -> str:
        return f"{self.title}:{self.descraibe}"


