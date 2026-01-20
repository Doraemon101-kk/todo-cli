from . import *
from pathlib import Path
import json

class InvalidTaskIDError(Exception):
    pass

class TodoList(object):
    def __init__(self, data_dir=None):  # ← 就改这一行！
        if data_dir is None:
            self.data_dir = Path.home() / ".todolist"
        else:
            self.data_dir = Path(data_dir)  # ← 支持传入路径
        
        self.data_dir.mkdir(exist_ok=True) 

        self.data_file = self.data_dir / "todos.json"
        if not self.data_file.exists():
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump([], f) 

        with open(self.data_file, "r", encoding="utf-8") as f:
            self.tasks = json.load(f)

    def save(self):
        with open (self.data_file, "w", encoding = "utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii = False, indent = 4)

    def add(self, stuff):
        new_id = max ((task["id"] for task in self.tasks), default = 0) + 1

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
                    raise InvalidTaskIDError("该id任务不存在")
            
            else:
                raise InvalidTaskIDError
        except ValueError:
            raise InvalidTaskIDError

    def display(self):
        if not self.tasks:
            print("任务列表空")
            return
        for task in self.tasks:
            if not task["done"]:
                print(f"{task['id']:<5}{task['task']}")