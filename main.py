from task_handler import Tasks_handler
from command_handler import Command_handler
from ui import render_UI
from rich.console import Console

SQLITE_PATH = "./tasks_db.sqlite"

if __name__ == "__main__":
    console = Console()
    console.height = console.height - 1
    
    console_prompt = Console()
    console_prompt.height = 1
    
    task_handler = Tasks_handler(SQLITE_PATH)
    cmd_handler = Command_handler(task_handler)
    
    task_handler.load_local_db()
    task_handler.complete_task(0)
    
    render_UI(task_handler.tasks, console)
    
    while True:
        input = console_prompt.input("[green] >: ")
        cmd_handler.read_command(input)
        render_UI(task_handler.tasks, console)