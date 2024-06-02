from task_handler import Tasks_handler
from ui import render_UI
from rich.console import Console
import os

SQLITE_PATH = "./tasks_db.sqlite"

if __name__ == "__main__":
    task_handler = Tasks_handler(SQLITE_PATH)
    console = Console()
    