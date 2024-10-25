# To-Do List Application
def display_menu():
    print("--------------------------")
    print("1). View To-Do List")
    print("2). Add In To-Do List")
    print("3). Remove From To-Do List")
    print("4). Exit")
    
def view_tasks(tasks):
    if not tasks:
        print('Your To-Do List Is Empty')
    else:
        print('Your To-Do List')
        for idx, task in enumerate(tasks,1):
            print(f'{idx}. {task}')

def add_tasks(tasks):
    task = input("Enter A New Task: ")
    tasks.append(task)
    print(f'{task} has been added to your To-Do List')
    
def remove_tasks(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num -1)
            print(f"{removed_task} has been removed from your To-Do List")
        else:
            print('Invalid task number')
    except ValueError:
        print('Please enter a valid number')


def todo_list_app():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1\2\3\4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_tasks(tasks)
        elif choice == '3':
            remove_tasks(tasks)
        elif choice == '4':
            print('GoodBye')
            break
        else:
            print('Invalid Choice')

todo_list_app()