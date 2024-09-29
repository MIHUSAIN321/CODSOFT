def task():
    tasks=[] #empty list
    print("welcome the to do list")
        
    total_task = int(input("enter how many task you want to add"))
    for i in range (1,total_task+1):
        task_name = input(f"Enter task {i} =")
        tasks.append(task_name)

    print(f"Todays task are\n{tasks}") 

    while True:
        operation = int(input("Enter 1-add\n2-update\n3-view\n4-delete\n5-exit/stop/"))
        if operation == 1:
            add = input("Enter the task you want to add =")
            tasks.append(add)
            print(f"Task{add} has been successfully added")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter the new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"updated task {up}")

        elif operation == 3:
            print(f"total tasks = {tasks}")

        elif operation ==4:
            del_val = input("which task you want to delete =")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"task {del_val} has been deleted")

        elif operation ==5:
            print("closing the program")         
            break  
        
        else:
            print("invalid input")

task()            
            