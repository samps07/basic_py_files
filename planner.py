# Task planner dictionary
d1 = {
    't1': 'watering plants',
    't2': 'sun bath'
}

print("Welcome to the Planner!\n")

for _ in range(1, 100):
    print("\nWhat do you want to do?")
    print("1. Know about a task")
    print("2. Add a task")
    print("3. Mark task as completed")
    print("4. Update a task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        task_id = input("Enter task ID to check (e.g., t1, t2): ").strip()
        if task_id in d1:
            print(f"Your task {task_id} is: {d1[task_id]}")
        else:
            ask = input(f"No task '{task_id}' found. Do you want to see available tasks? (yes/no): ").strip().lower()
            if ask == 'yes':
                print("\nAvailable tasks in your planner:")
                for k in d1:
                    print(f"{k}: {d1[k]}")

    elif choice == '2':
        new_task = input("Enter the new task description: ").strip()
        new_id = f"t{len(d1) + 1}"
        d1[new_id] = new_task
        print(f"\nTask added as {new_id}: {new_task}")
        print("All tasks:")
        for k, v in d1.items():
            print(f"{k}: {v}")

    elif choice == '3':
        task_id = input("Enter task ID to mark as completed: ").strip()
        if task_id in d1:
            print(f"Task '{d1[task_id]}' marked as completed and removed.")
            del d1[task_id]
        else:
            print("Invalid task ID.")

    elif choice == '4':
        task_id = input("Enter task ID to update: ").strip()
        if task_id in d1:
            new_task = input("Enter updated task description: ").strip()
            d1[task_id] = new_task
            print(f"Task {task_id} updated to: {new_task}")
        else:
            print("Invalid task ID.")

    elif choice == '5':
        print("Exiting planner. Have a nice day!")
        break

    else:
        print("Invalid option! Please choose from 1 to 5.")

