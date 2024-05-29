from task_handler import Task_handler
from ui import render_UI
from rich.console import Console
import os

TASKS_PATH = "tasks.json"
FIREBASE_URL = "https://kermittodo-default-rtdb.firebaseio.com/"

if __name__ == "__main__":
    os.system('cls||clear')
    taskhandler = Task_handler(FIREBASE_URL, TASKS_PATH)
    # taskhandler.download_from_cloud(TASKS_PATH)
    taskhandler.load_file()
    console = Console()
    
    # os.system('cls||clear')
    # tasks = taskhandler.get_tasks()
    # render_UI(tasks, console)
    
    while (True):
        inp = input("0: Create Task, \n1: Delete Task, \n2: Get Tasks \nAny Other Key: Exit \nChoice: ")
        print("")
        if (inp == "0"):
            os.system('cls||clear')
            taskhandler.create_task(input("Name: "), input("Task: "))
            taskhandler.save_file()
            print("Task Created")
        elif (inp == "1"):
            os.system('cls||clear')
            taskhandler.delete_task(input("Name: "))
            taskhandler.save_file()
            print("Task Deleted")
        elif (inp == "2"):
            os.system('cls||clear')
            tasks = taskhandler.get_tasks()
            render_UI(tasks, console)
        else:
            taskhandler.save_file()
            # taskhandler.upload_to_cloud()
            print("File Saved")
            os.system('cls||clear')
            break
        print("")