from domain.todo import ToDoItem

class ToDoService:
    def __init__(self, todo_repo):
        self.todo_repo = todo_repo

    def add_todo_item(self, description: str):
        new_id = len(self.todo_repo.get_all()) + 1
        new_todo = ToDoItem(id=new_id, description=description)
        self.todo_repo.save(new_todo)
        return new_todo

    def mark_todo_as_completed(self, id: int):
        todo = self.todo_repo.get_by_id(id)
        if todo:
            todo.mark_as_completed()
            self.todo_repo.save(todo)
            return todo
        else:
            raise ValueError("ToDo item not found.")
