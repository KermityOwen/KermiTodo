from task_handler import Task, Tasks_handler
from datetime import datetime
import os

HELP_HELP = """Syntax: help <command>. To get instructions on how to use <command>."""
HELP_ADD = """Syntax: add <task_name> <task_description> <task_deadline>. To add a task to the to-do list, date is in the format of dd/mm/YYYY"""
HELP_REMOVE = """Syntax: remove <task_id>. Removes task from to-do list."""
HELP_EXIT = """Syntax: exit. Exits the program"""
HELP_COMPLETE = """Syntax: complete <task_id>. Toggles task's completeness"""
HELP_UPDATE = """Syntax: update <task_id> <task_name> <task_description> <task_deadline>. Updates task's details. Enter '-' to skip updating that element."""

class Command_handler:
    def __init__(self, task_handler: Tasks_handler):
        self.COMMANDS_MAP = {"add": self.add_task_command,
                             "remove": self.remove_task_command,
                             "complete": self.complete_task_command,
                             "update": self.update_task_command,
                             "exit": self.exit_command,
                             "help": self.help_command}
        
        self.task_handler = task_handler
    
    
    def help_command(self, args_arr: list, help=False):
        if help:
            return HELP_HELP
        
        if len(args_arr) == 0:
            # Dynamically updates along with dictionary
            return f"Command List: {HELP_HELP}. {str(list(self.COMMANDS_MAP.keys()))}."
        else:
            try:
                return self.COMMANDS_MAP.get(args_arr[0])([], help=True) # Kinda shitty code but its compact and efficient
            except: 
                return f"Help: '{args_arr[0]}', Command Not Found"
    
    
    def add_task_command(self, args_arr, help=False):
        if help:
            return HELP_ADD
        
        try:
            task = Task(args_arr[0], args_arr[1], datetime.now(), datetime.strptime(args_arr[2],"%d/%m/%Y")) # Exception checking here
            self.task_handler.add_task(task)
            return "Task added successfully"
        except IndexError:
            return "Add: Arguments Missing. Use 'help add' for more details."
        except Exception as e: # Custom Exceptions raised and handled in task_handler.py
            return e
            
        
    def remove_task_command(self, args_arr, help=False):
        if help:
            return HELP_REMOVE
        
        try:
            self.task_handler.remove_task(int(args_arr[0])) # Exception checking here
            return "Task removed successfully"
        except IndexError:
            return "Remove: Arguments Missing. Use 'help remove' for more details."
        except Exception as e: # Custom Exceptions raised and handled in task_handler.py
            return e
        
        
    def complete_task_command(self, args_arr, help=False):
        if help:
            return HELP_COMPLETE
        
        try:
            self.task_handler.complete_task(int(args_arr[0])) # Exception checking here
            return "Task completed successfully."
        except IndexError:
            return "Complete: Arguments Missing. Use 'help complete' for more details."
        except Exception as e:
            return e
    
    
    def update_task_command(self, args_arr, help=False):
        if help:
            return HELP_UPDATE
        try:
            self.task_handler.update_task(int(args_arr[0]), args_arr[1], args_arr[2], args_arr[3])
            return "Task updated successfully"
        except IndexError:
            return "Update: Arguments Missing. Use 'help update' for more details."
        except Exception as e:
            return e
    

    def exit_command(self, args_arr, help=False): # Need to pass in args but doesn't need to use them
        if help:
            return HELP_EXIT
        os.system("cls||clear")
        exit()


    def read_commands(self, command_str: str) -> str:
        parsed_args = command_str.split(" ")
        func = parsed_args[0].lower()
        parsed_args.pop(0)
        try:
            cmd_out = self.COMMANDS_MAP.get(func)(parsed_args)
            return cmd_out
        except Exception as e:
            return e