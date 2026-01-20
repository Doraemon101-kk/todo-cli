from . import *
from pathlib import Path
import json

class InvalidTaskIDError(Exception):
    pass

class TodoList(object):
    def __init__(self):
        self.data_dir = Path.home() / ".todolist"
        self.data_dir.mkdir(exist_ok=True) 

        self.data_file = self.data_dir / "todos.json"
        if not self.data_file.exists():
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump([], f) 

        with open(self.data_file, "r", encoding="utf-8") as f:
            self.tasks = json.load(f)

    def save(self):
        with open (self.data_file, "a") as f:
            json.dump(self.tasks, f, ensure_ascii = False, indent = 4)

    def add(self, stuff):
        if self.tasks:
            new_id = max (tasks["id"] for tasks in self.tasks) + 1
        else:
            new_id = 1

        new_task = {
            "id":new_id,
            "task":stuff,
            "done":False,
        }
        self.tasks.append(new_task)

        self.save()

    def finish(self, stuff):
        stuff = stuff.strip()

        try :
            task_ID = int(stuff)

            if task_ID > 0:
                found = False
                for task in self.tasks:
                    if task["id"] == task_ID:
                        self.tasks.remove(task)
                        self.save()
                        found = True
                        break
                if not found:
                    print("该id任务不存在")
                
        except ValueError:
            raise InvalidTaskIDError

    def display(self):
        pass