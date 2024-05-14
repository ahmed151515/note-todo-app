import json


class Todo():
    todohash = dict()
    todolist = list()

    @classmethod
    def load(cls):
        with open("classes/todo.json", "r")as f:
            Todo.todohash = json.load(f)

    @classmethod
    def save(cls):

        with open("classes/todo.json", "w")as f:
            json.dump(Todo.todohash, f, indent=4)

    @classmethod
    def convert_dict_to_list(cls):
        for t, d in Todo.todohash.items():
            todo = Todo()
            todo.title = t
            todo.describ = d
            Todo.todolist.append(todo)

    def _str_(self) -> str:
        return f"{self.title}:{self.describ}"


Todo.load()