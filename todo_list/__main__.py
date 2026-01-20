from .engine import TodoList
from sys import argv

todo = TodoList()

while True:
    print("通过add \"任务内容\"添加任务")
    print("通过list得到所有未完成任务列表")
    print("通过done <number>标记完成")
    print("通过save保存任务数据")
    print("通过exit退出")
    script, stuff = argv

    if "add" in stuff:
        todo.add("")

    elif "list" in stuff:
        todo.display()
    elif "done" in stuff:
        todo.finish("")

    elif "save" in stuff:
        todo.save()

    elif "exit" in stuff:
        exit(0)

    else:
        print("错误输入")

save_file.close()