from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel


def generate_table(tasks: dict):
    table = Table(expand=True)
    
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Description")
    
    i = 0
    for x, y in tasks.items():
        table.add_row(str(i), str(x), str(y))
        i = i+1
    
    return table


def render_UI(tasks: dict, console: Console):
    panel_table = Panel.fit(generate_table(tasks))
    panel_table.expand = True
    
    layout = Layout()
    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )
    
    layout["upper"].ratio = 7
    layout["upper"].update(
        panel_table
    )
    
    layout["lower"].ratio = 1

    console.print(layout)