from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel
import os

from typing import Dict
from datetime import datetime

from task_handler import Task, Tasks_handler

# TODO color config

def generate_header() -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="right")
    grid.add_row(
        "[rgb(230,255,250)]Kermit's [b]TO-DO[/b] App",
        "[rgb(230,255,250)]"+datetime.now().ctime(),
    )
    return Panel(grid, border_style="rgb(230,255,250)", style="white on rgb(80,200,70)")

def generate_prompt() -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="right")
    grid.add_row(
        "[green]Commands: Add, Remove, Update, Sync, Help[/green]"
    )
    return Panel(grid, border_style="rgb(50,125,100)", style="default")

def generate_table(tasks: Dict[int, Task]):
    table = Table(expand=True, style="rgb(50,125,100)")
    
    table.add_column("[rgb(122,255,235)]ID", ratio=2, justify="center")
    table.add_column("[rgb(122,255,235)]Name", ratio=5, justify="center")
    table.add_column("[rgb(122,255,235)]Description", ratio=25, justify="center")
    table.add_column("[rgb(122,255,235)]Deadline", ratio=9, justify="center")
    table.add_column("[rgb(122,255,235)]Days Left", ratio=4, justify="center")
    table.add_column("[rgb(122,255,235)]Done", ratio=2, justify="center")
    
    for id, task in tasks.items():
        deadline = task.date_deadline
        time_left = (deadline - datetime.now()).days
        deadline_str = deadline.strftime("%d/%m/%Y")
        time_left_str = str(time_left)
        
        id_str = str(id)
        name_str = task.name
        desc_str = task.description       
        
        task_doneness = "[b][white]\[ ][/b]"
        if (task.complete == True):
            task_doneness = "[b][green]\[x][/b]"
            time_left_str = "[green]" + time_left_str
            deadline_str = "[green]" + deadline_str
            id_str = "[green]" + id_str
            name_str = "[green]" + name_str
            desc_str = "[green]" + desc_str
        elif (time_left <= 0):
            task_doneness = "[b][red]\[ ][/b]"
            time_left_str = "[red]" + time_left_str
            deadline_str = "[red]" + deadline_str
            id_str = "[red]" + id_str
            name_str = "[red]" + name_str
            desc_str = "[red]" + desc_str
        
        table.add_row(id_str, name_str, desc_str, deadline_str, time_left_str, task_doneness)
    return table


def render_UI(tasks: dict, console: Console, command_stream: str = ""):
    # os.system('cls||clear')
    table_panel = Panel.fit(generate_table(tasks), border_style="green", title="[rgb(80,200,70)]Tasks")
    table_panel.expand = True
    
    layout = Layout()
    layout.split_column(
        Layout(name="header", minimum_size=3),
        Layout(name="table"),
        Layout(name="prompt", minimum_size=3)
    )
    
    layout["header"].ratio = 1
    layout["header"].update(
        generate_header(),
    )
    
    layout["table"].ratio = 15
    layout["table"].update(
        table_panel,
    )
    
    layout["prompt"].ratio = 1
    layout["prompt"].update(
        generate_prompt()
    )

    console.print(layout)
    