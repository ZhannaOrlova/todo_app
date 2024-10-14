class InMemoryToDoRepository:
    def __init__(self):
        self.todos = []

    def save(self, todo):
        # If the item already exists, update it
        for i, existing_todo in enumerate(self.todos):
            if existing_todo.id == todo.id:
                self.todos[i] = todo
                return
        # Otherwise, add it
        self.todos.append(todo)

    def get_all(self):
        return self.todos

    def get_by_id(self, id):
        for todo in self.todos:
            if todo.id == id:
                return todo
        return None
