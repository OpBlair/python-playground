tasks = []

def main():
    while True:
        print("\n--- Daily Task Scheduler ---")
        print("1. Add Task")
        print("2. Mark Tasks complete")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            # Add task logic
            task_name = input("Enter the task description: ").strip()
            if task_name:
                tasks.append({"title": task_name, "completed": False})
                print(f"Task '{task_name}' added successfully!")
            else:
                print("Task description cannot be empty.")
                
        elif choice == "2":
            # Mark tasks complete logic
            if not tasks:
                print("No tasks available to mark complete.")
                continue
            
            print("\nCurrent Tasks:")
            for index, task in enumerate(tasks, 1):
                status = "X" if task["completed"] else " "
                print(f"{index}. [{status}] {task['title']}")
            
            try:
                task_num = int(input("Enter the task number to mark complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print(f"Task '{tasks[task_num - 1]['title']}' marked as complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
