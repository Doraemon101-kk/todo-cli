import tempfile
from todo_list.engine import TodoList, InvalidTaskIDError


def test_basic_workflow():
    with tempfile.TemporaryDirectory() as tmpdir:
        todo = TodoList(data_dir=tmpdir)
        todo.add("买牛奶")
        todo.add("写代码")
        
        assert len(todo.tasks) == 2
        assert todo.tasks[0]["id"] == 1
        assert todo.tasks[0]["task"] == "买牛奶"
        assert todo.tasks[1]["id"] == 2
        assert todo.tasks[1]["task"] == "写代码"
        
        todo.finish("1")
        
        assert len(todo.tasks) == 1
        assert todo.tasks[0]["id"] == 2
        assert todo.tasks[0]["task"] == "写代码"


def test_empty_list():
    with tempfile.TemporaryDirectory() as tmpdir:
        todo = TodoList(data_dir=tmpdir)
        assert len(todo.tasks) == 0
        
        todo.add("第一个任务")
        assert todo.tasks[0]["id"] == 1


def test_invalid_id():
    with tempfile.TemporaryDirectory() as tmpdir:
        todo = TodoList(data_dir=tmpdir)
        todo.add("有效任务")
        
        # 非数字
        try:
            todo.finish("abc")
            assert False
        except InvalidTaskIDError:
            pass
        
        # 负数
        try:
            todo.finish("-1")
            assert False
        except InvalidTaskIDError:
            pass
        
        # 不存在的 ID
        try:
            todo.finish("999")
            assert False
        except InvalidTaskIDError:
            pass


def test_persistence():
    with tempfile.TemporaryDirectory() as tmpdir:
        todo1 = TodoList(data_dir=tmpdir)
        todo1.add("持久化测试")
        task_id = todo1.tasks[0]["id"]
        
        todo2 = TodoList(data_dir=tmpdir)
        assert len(todo2.tasks) == 1
        assert todo2.tasks[0]["id"] == task_id
        assert todo2.tasks[0]["task"] == "持久化测试"
        
        todo2.finish(str(task_id))
        
        todo3 = TodoList(data_dir=tmpdir)
        assert len(todo3.tasks) == 0