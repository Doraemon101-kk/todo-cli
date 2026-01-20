from .engine import TodoList
from .engine import InvalidTaskIDError
from sys import argv

def help():
    print("添加任务：输入 add \"task\"")
    print("完成任务：输入 done <number>")
    print("展示任务清单：输入list")

todo = TodoList()
if len(argv) == 2:
    script, cmd = argv
    if cmd == "list":
        todo.display()
    else:
        print("错误的输入")
    

elif len(argv) == 3:
    script, cmd, stuff = argv

    if cmd == "add":
        todo.add(stuff)

    elif cmd == "done":
        try:
            todo.finish(stuff)
        except InvalidTaskIDError:
            print("序号必须为正整数")

    else:
        print("错误的输入")
    
elif len(argv) == 1:
    help()


else:
    print("错误的输入")