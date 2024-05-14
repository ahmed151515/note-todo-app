import json


class Todo():
    todohash = dict()

    @classmethod
    def load(cls):
        with open("classes/todo.json", "r")as f:
            Todo.todohash = json.load(f)

    @classmethod
    def save(cls):

        with open("classes/todo.json", "w")as f:
            json.dump(Todo.todohash, f, indent=4)


Todo.load()

