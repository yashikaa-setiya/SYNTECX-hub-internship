import json

try:
    with open ("tasks.json","r") as f:
        tasks= json.load(f)
except :
    tasks=[]

def add_task():
    task_name = input("enter the task name that you wanna add: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks()  # persist the new task
    print(f"task {task_name} is added!")

def view_task():
    if not tasks:
        print("there are no tasks")
    else:
        for i , t in enumerate(tasks):
            status = "done" if t["done"] else "pending"
            print(f"{i+1}. {t['task']} - {status}")

def delete_task():
    if len(tasks) >= 1:
        view_task()
    else:
        print("no tasks available")
        return 
    deleted_task= int(input("enter the num of task you want to delete"))
    if 0 < deleted_task <= len(tasks):
        deleted_task -= 1
        removed_task = tasks.pop(deleted_task)
        save_tasks()  # update file after deletion
        print(f"task {removed_task['task']} is deleted!")
    else:
        print("invalid task number")

def mark_task_done():
    view_task()
    mark_task= int(input("enter the task num you want to mark done"))
    if 0 < mark_task <= len(tasks):
        mark_task -=1
        tasks[mark_task]["done"]=True
        save_tasks()
        print(f"task num {mark_task} is marked as done!")
    else:
        print("invalid number!")

def save_tasks():
    # fixed missing closing quote in filename
    with open("tasks.json","w") as f:
        json.dump(tasks, f)



def menu():
    while True:
        print("TO-DO MANAGER")
        print("1 = Add task")
        print("2 = Delete task")
        print("3 = Mark task as done")
        print("4 = View task")
        print("5 = Exit")
        try:
            chosen = int(input("what would want to do?"))
        except:
            print("invalid value")

        if chosen == 1:
            add_task()
        elif chosen == 2:
            delete_task()
        elif chosen == 3:
            mark_task_done()
        elif chosen == 4:
            view_task()
        elif chosen == 5:
            break
        else:
            print("write a valid num")

if __name__ == "__main__":
    menu()