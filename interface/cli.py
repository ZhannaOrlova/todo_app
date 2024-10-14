from application.todo_service import ToDoService
from infrastructure.memory_todo_repo import InMemoryToDoRepository

def main():
    repo = InMemoryToDoRepository()
    todo_service = ToDoService(repo)
    
    while True:
        print("\n1. Add To-Do")
        print("2. List To-Do Items")
        print("3. Mark To-Do as Completed")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter the to-do description: ")
            todo = todo_service.add_todo_item(description)
            print(f"Added: {todo}")
        elif choice == '2':
            todos = repo.get_all()
            for todo in todos:
                print(todo)
        elif choice == '3':
            todo_id = int(input("Enter the to-do ID to mark as completed: "))
            try:
                todo = todo_service.mark_todo_as_completed(todo_id)
                print(f"Updated: {todo}")
            except ValueError as e:
                print(e)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
