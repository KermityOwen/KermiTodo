from task_handler import Task, Tasks_handler
from datetime import datetime
import os

class Command_handler:
    def __init__(self, task_handler: Tasks_handler):
        self.COMMANDS_MAP = {"add": self.add_task_command,
                             "remove": self.remove_task_command,
                             "update": self.update_task_command,
                             "exit": self.exit_command}
        
        self.task_handler = task_handler
    
    def add_task_command(self, args_arr):
        task = Task(args_arr[0], args_arr[1], datetime.now(), datetime.strptime(args_arr[2],"%d/%m/%Y"))
        self.task_handler.add_task(task)
        
    def remove_task_command(self, args_arr):
        self.task_handler.remove_task(int(args_arr[0]))
        
    def update_task_command(self, args_arr):
        print("update")

    def exit_command(self, args_arr):
        os.system("cls||clear")
        exit()

    def read_command(self, command_str: str):
        parsed_args = command_str.split(" ")
        func = parsed_args[0].lower()
        parsed_args.pop(0)
        try:
            self.COMMANDS_MAP.get(func)(parsed_args)
        except Exception as e:
            print(e)