tasks = [ {
    "Task": "Priority"
}]


def view_menu():
    for task in tasks:
        print (task)
index = 1
def delete_task():
    for c, task in enumerate(tasks, 1):
        view_menu()
        delete_input = del tasks[int(input("Which one do you want to delete?"))]
    return delete_input


def show_menu():
    print("Press 1 to add a new task: ")
    print("Press 2 to delete task: ")
    print("Press 3 to view all task: ")
    print("Press q to quit: ")

def add_new_task():
    task_name = str(input("Enter name of task:"))
    task_priority = str(input("Enter priority: "))
    tasks.append(task_name)
    tasks.append(task_priority)

user_input = ""

while user_input != "q":
    show_menu()
    user_input = input("Enter your choice:")
    if user_input == "3":
        view_menu()
    elif user_input == "1":
        add_new_task()
    elif user_input == "2":
        delete_task()
