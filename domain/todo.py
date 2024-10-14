class ToDoItem:
    def __init__(self, id: int, description: str, completed: bool = False):
        self.id = id
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

    def __repr__(self):
        return f"{self.id}: {self.description} - {'Completed' if self.completed else 'Pending'}"
