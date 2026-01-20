# Todo CLI

一个轻量级命令行任务管理工具，用 Python 编写，数据自动保存在本地，无需依赖。

## 功能

- **添加新任务**  
  ```bash
  todo add "买牛奶"
  todo add "完成 Python 作业"
  ```

- **列出所有未完成任务**  
  ```bash
  todo list
  ```

- **完成并标记任务**  
  ```bash
  todo done 1
  todo done 3
  ```

> 💡  
> - 任务描述**必须用英文双引号 `"` 包裹**（支持空格和中文）  
> - `done` 后跟任务 ID（数字），**不要加引号**  
> - 完成任务后，该任务**不会出现在 todo list 的结果中**

## 安装与运行

确保已安装 Python 3.6+，然后在项目目录执行
```bash
python -m todo_list add "买牛奶"
python -m todo_list list
python -m todo_list done 1
```

## 使用说明

1. **添加任务**  
   所有任务内容需用双引号包围：
   ```bash
   $ todo add "整理书桌"
   $ todo add "给妈妈打电话"
   ```

2. **查看待办清单**  
   只显示未完成的任务（按 ID 排序）：
   ```bash
   $ todo list
   1     整理书桌
   2     给妈妈打电话
   ```

3. **标记任务为完成**  
   输入任务 ID 即可将其标记为已完成（不再显示在清单中）：
   ```bash
   $ todo done 1
   # ID 为 1 的任务“整理书桌”已标记为完成
   ```

## 数据存储

所有任务保存在：  
`~/.todolist/todos.json`  
（位于用户主目录，程序自动创建）
### 📁 自定义存档路径（高级用法）
你也可以通过代码指定自定义存档路径：

```python
from todo_list.engine import TodoList


my_todo = TodoList(data_dir="/path/to/my/tasks")```
---

> ✨ 特点：简单、快速、零依赖，适合日常轻量级任务管理。

---