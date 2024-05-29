from task_handler import Task_handler
import os

TASKS_PATH = "tasks.json"
FIREBASE_URL = "https://kermittodo-default-rtdb.firebaseio.com/"

if __name__ == "__main__":
    os.system('cls||clear')
    taskhandler = Task_handler(FIREBASE_URL)
    # taskhandler.download_from_cloud(TASKS_PATH)
    taskhandler.load_file(TASKS_PATH)
    while (True):
        inp = input("0: Create Task, \n1: Delete Task, \n2: Get Tasks \nAny Other Key: Exit \nChoice: ")
        print("")
        if (inp == "0"):
            taskhandler.create_task(input("Name: "), input("Task: "))
            taskhandler.save_file(TASKS_PATH)
            print("Task Created")
        elif (inp == "1"):
            taskhandler.delete_task(input("Name: "))
            taskhandler.save_file(TASKS_PATH)
            print("Task Deleted")
        elif (inp == "2"):
            print(taskhandler.get_tasks())
        else:
            taskhandler.save_file(TASKS_PATH)
            taskhandler.upload_to_cloud(TASKS_PATH)
            print("File Saved")
            os.system('cls||clear')
            break
        print("")