from textual.app import App
from textual.widgets import Footer, Header, Static, Button, Placeholder
from textual.containers import ScrollableContainer, Grid

class Actions(Static):
    def compose(self):
        with Grid(id="action-grid"):
            yield Button("Create", variant="success", id="create")
            yield Button("Delete", variant="error", id="delete")
            yield Button("Update", variant="primary", id="update")

class Task(Static):
    pass

class Todo_App(App): # Extends Textual App Class 
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggles Dark Mode"),
        ("q", "exit", "Exit Program")
    ]
    
    CSS_PATH = "./ui.tcss" 
    
    def compose(self):
        self.title = "To-Do App"
        yield Header(show_clock=True)
        yield Footer()
        yield Actions()
        with ScrollableContainer(id="tasks"):
            yield Task("text")
            yield Task("text")
            yield Task("text")
    
    def action_toggle_dark_mode(self):
        self.dark = not self.dark
    
    def action_exit(self):
        exit()


if __name__ == "__main__":
    app = Todo_App()
    app.run()