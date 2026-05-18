def add_task(name):
    task ={
        "name":name
    }
    tasks.append(task)

def save_tasks(tasks):
    with open("task.txt","w",encoding="utf-8") as f:
        for t in tasks:
            f.write(t["name"]+"\n")

def load_task():
    task=[]
    try:
        with open("task.txt","r",encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    task.append({"name":line.strip()})
    except FileNotFoundError:
        pass
    return task

tasks=load_task()

while True:
    control= input(("press a to add task\n" 
    "press d to delete task\n" 
    "press s to show task\n" 
    "enter save to save tasks\n"
    "press e and enter to exit\n"
    "enter control : "))
    
    if control == "e":
        save = input("save before exit?(y/n)")
        if save == "y":
            save_tasks(tasks)
            print("Tasks saved")
        break
    elif control =="a":
        name= input("Enter task name to add : ")
        add_task(name)
        print("Task added")
    elif control == "d":
        name = input("Enter task name to delete")
        found= False
        for t in tasks[:]:
            if t["name"]==name:
                tasks.remove(t)
                print("task deleted")
                found= True
                break
        if not found:
            print("task not found")
    elif control =="s":
        if len(tasks)==0:
            print("No task found")
            continue
        print("Tasks : ")
        for i,t in enumerate(tasks):
            print(i,":",t["name"],"\n")
    elif control == "save":
        save_tasks(tasks)
        print("Tasks saved")
        