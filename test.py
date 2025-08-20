print("Welcome to the task list app")
tasks = []


def mine():
    tas = '''1- add task 
2-make task complite 
3-view your to-do list
4-quit'''
    print(tas)
    while True:
        task = input("please choose one of this [1 / 2 / 3 / 4] : ")
        if task == "1":
            add_task()
        elif task == "2":
            compile_task()
        elif task == "3":
            viwe_task()
        elif task == "4":
            break
        else:
            print("wrong choose")


def add_task():
    user_task = input("enter your task : ")
    com_task = {"user_task": user_task, "complite": False}
    tasks.append(com_task)
    print("task had been add")


def compile_task():
    non_complite = [
        user_task for user_task in tasks if user_task["complite"] == False]
    if non_complite:
        for i, user_task in enumerate(non_complite):
            print(f"{i+1}- {user_task['uer_task']}")
            print('-'*30)
        user_com = int(input("which task you had complite : "))
        non_complite[user_com-1]["complite"] = True
    else:
        print("it's empty")


def viwe_task():
    if not tasks:
        print("no tasks")
        return
    for i, user_task in enumerate(tasks):
        set = "✔️" if user_task["complite"] == True else "❌"
        print(f"{i+1}. {user_task['user_task']}{set}")


mine()
