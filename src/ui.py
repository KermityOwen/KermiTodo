from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel

import os, sys, pathlib, json
from typing import Dict
from datetime import datetime

from task_handler import Task


START_RESPONSE = "Hello, Kermit. Use 'help' to get started ;)"
if getattr(sys, 'frozen', False):
    ABS_PATH = os.path.dirname(sys.executable)
else:
    ABS_PATH = pathlib.Path(__file__).parent.resolve()
COLOR_CONFIG_PATH = os.path.join(ABS_PATH, "color_config.json")
with open(COLOR_CONFIG_PATH) as json_file:
    COLOR_CONFIG = json.load(json_file)


def generate_header() -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="right")
    grid.add_row(
        f"[{COLOR_CONFIG['title']}]Kermit's [b]TO-DO[/b] App",
        f"[{COLOR_CONFIG['title_time']}]"+datetime.now().ctime(),
    )
    return Panel(grid, border_style=f"{COLOR_CONFIG['title_layout_border']}", style=f"{COLOR_CONFIG['title_layout_border']} on {COLOR_CONFIG['title_bg']}")


def generate_prompt(cmd_output: str) -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="left", ratio=1)
    grid.add_row(
        f"[{COLOR_CONFIG['prompt_text']}]{cmd_output}"
    )
    return Panel(grid, border_style=f"{COLOR_CONFIG['prompt_layout_border']}", style="default")


def generate_table(tasks: Dict[int, Task]):
    table = Table(expand=True, style=f"{COLOR_CONFIG['table_border']}", show_lines=True)
    
    table.add_column(f"[{COLOR_CONFIG['table_column_text']}]ID", ratio=2, justify="center")
    table.add_column(f"[{COLOR_CONFIG['table_column_text']}]Name", ratio=5, justify="center")
    table.add_column(f"[{COLOR_CONFIG['table_column_text']}]Description", ratio=25, justify="center")
    table.add_column(f"[{COLOR_CONFIG['table_column_text']}]Deadline", ratio=9, justify="center")
    table.add_column(f"[{COLOR_CONFIG['table_column_text']}]Days Left", ratio=4, justify="center")
    table.add_column(f"[{COLOR_CONFIG['table_column_text']}]Done", ratio=2, justify="center")
    
    for id, task in tasks.items():
        deadline = task.date_deadline
        time_left = (deadline - datetime.now()).days
        deadline_str = deadline.strftime("%d/%m/%Y")
        time_left_str = str(time_left)
        
        id_str = str(id)
        name_str = task.name
        desc_str = task.description       
        
        task_doneness = f"[b][{COLOR_CONFIG['normal']}]\[ ][/b]"
        if (task.complete == True):
            task_doneness = f"[b][{COLOR_CONFIG['complete']}]\[x][/b]"
            time_left_str = f"[{COLOR_CONFIG['complete']}]" + "Complete"
            deadline_str = f"[{COLOR_CONFIG['complete']}]" + deadline_str
            id_str = f"[{COLOR_CONFIG['complete']}]" + id_str
            name_str = f"[{COLOR_CONFIG['complete']}]" + name_str
            desc_str = f"[{COLOR_CONFIG['complete']}]" + desc_str
        elif (time_left <= 0):
            task_doneness = f"[b][{COLOR_CONFIG['overdue']}]\[ ][/b]"
            time_left_str = f"[{COLOR_CONFIG['overdue']}]" + time_left_str
            deadline_str = f"[{COLOR_CONFIG['overdue']}]" + deadline_str
            id_str = f"[{COLOR_CONFIG['overdue']}]" + id_str
            name_str = f"[{COLOR_CONFIG['overdue']}]" + name_str
            desc_str = f"[{COLOR_CONFIG['overdue']}]" + desc_str
        
        table.add_row(id_str, name_str, desc_str, deadline_str, time_left_str, task_doneness)
    return table


def render_UI(tasks: dict, console: Console, cmd_output=START_RESPONSE, debug=False):
    if (not debug):    
        os.system('cls||clear')
    table_panel = Panel.fit(generate_table(tasks), border_style=f"{COLOR_CONFIG['table_layout_border']}", title=f"[{COLOR_CONFIG['table_layout_border']}]Tasks")
    table_panel.expand = True
    
    layout = Layout()
    layout.split_column(
        Layout(name="header", minimum_size=3),
        Layout(name="table"),
        Layout(name="prompt", minimum_size=4)
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
        generate_prompt(cmd_output=cmd_output)
    )

    console.print(layout)
    