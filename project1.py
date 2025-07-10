def print_menu():
    print("----------TO DO LIST MENU----------")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")

def add_task(tasks):
    task_name = input("Enter task name: ")
    tasks.append({"description":task_name, "finished":False})

def view_all_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks added")
    else:
        print("----------------------------------")
        for i, task in enumerate(tasks):
            if task["finished"]==True:
                print(i+1, ".", task["description"], "✓")
            else:
                print(i+1,".", task["description"])

def mark_task(tasks):
    if len(tasks) == 0:
        print("No tasks added")
    else:
        task_num = int(input("Enter task number: "))
        if task_num-1 > len(tasks):
            print("Invalid task number")
            task_num = int(input("Enter another task number: "))
            tasks[task_num-1]["finished"] = True

def delete_task(tasks):
    task_num = int(input("Enter task number: "))
    del tasks[task_num-1]

def main():
    tasks = []
    while True:
        print_menu()
        option = input("Enter your choice: ")
        if option == "1":
            add_task(tasks)
        if option == "2":
            view_all_tasks(tasks)
        if option == "3":
            mark_task(tasks)
        if option == "4":
            delete_task(tasks)
        if option == "5":
            break

if __name__ == "__main__":
    main()


