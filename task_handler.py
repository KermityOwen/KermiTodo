import json
import requests
import sqlite3
from datetime import datetime

class Task:
    def __init__(self, name: str, description: str, date_created: datetime, date_deadline: datetime):
        if(self.validate(name, description, date_created, date_deadline)):
            pass 
        else:
            raise Exception("Invalid Task")
        
        self.name = name
        self.description = description
        self.date_created = date_created
        self.date_deadline = date_deadline
        self.complete = False
        
        print("Task Created")
        
        
    def validate(self, name: str, description: str, date_created: datetime, date_deadline: datetime):
        validity = True
        validity = (len(name) <= 32) and (len(name) > 0) and validity 
        validity = (len(description) <= 512) and validity
        validity = (date_created < date_deadline) and validity
        return validity
    
    
    def toggle_complete(self):
        self.complete = not self.complete
        
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Date-Created: {self.date_created.strftime('%d/%m/%Y')}\n"
                f"Deadline: {self.date_deadline.strftime('%d/%m/%Y')}\n"
                f"Completed: {self.complete}")
    
    
class Tasks_handler:
    def __init__(self):
        self.id_counter = 0
        self.tasks: dict[int, Task] = {} # Index : Task Object
    
    def add_task(self, task:Task):
        self.tasks[self.id_counter] = task
        # TODO: Write to DB
        
    def complete_task(self, task_id: int):
        self.tasks[task_id].toggle_complete()
        # TODO: Update to DB

    def remove_task(self, task_id: int):
        self.tasks.pop(task_id)
        # TODO: Remove from DB
        
    def get_task(self, task_id: int):
        return self.tasks[task_id]
    
    def get_tasks_ids(self):
        return list(self.tasks.keys())


if __name__ == "__main__":
    task_handler = Tasks_handler()
    task1 = Task("name1", "ipsum loren yadda yadda yoo", datetime.now(), datetime(2024,6,10))
    task_handler.add_task(task1)
    
    print(task_handler.get_task(0))
    
    