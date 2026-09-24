tasks = []

try:
     with open("tasks.txt", "r") as file:
        for line in file:
            task, status = line.strip().split("|")
            tasks.append([task, status == "True"])
except FileNotFoundError:
    pass

def save_tasks():
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(f"{task[0]}|{task[1]}\n")


while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append([task,False])
        save_tasks()
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks,start=1):
            status = "✅" if task[1] else " "
            print(f"{i}. [{status}] {task[0]}")

    elif choice == "3":
        num = int(input("Enter task number to delete: "))

        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks()
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")    
        


    elif choice == "4":
        num = int(input("Enter task number to mark as completed:"))

        if 1 <= num <= len(tasks):
            tasks[num - 1][1] = True
            save_tasks()
            print("Task marked as complete!")

        else:
            print("Invalid task number!")


    elif choice == "5":
        print("Goodbye!")
        break    

   
        
        
        