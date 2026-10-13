tasks = []

def main():
    while True:
        print("\n--- Daily Task Scheduler ---")
        print("1. Add Task")
        print("2. Mark Tasks complete")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            # TODO: Write your add task logic here
            print("You chose to add a task.")
        elif choice == "2":
            # TODO: Write your mark complete logic here
            print("You chose to mark a task complete.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()