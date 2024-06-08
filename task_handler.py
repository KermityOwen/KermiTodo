import sqlite3
from datetime import datetime
from db_handler import *

class Task:
    def __init__(self, name: str, description: str, date_created: datetime, date_deadline= datetime.now(), complete=False):
        if(self.validate(name, description)):
            pass 
        else:
            raise Exception("Invalid Task")
        
        self.name = name
        self.description = description
        self.date_created = date_created
        self.date_deadline = date_deadline
        self.complete = complete
        
        print("Task Created")
        
        
    def validate(self, name: str, description: str):
        validity = True
        validity = (len(name) <= 32) and (len(name) > 0) and validity 
        validity = (len(description) <= 512) and validity
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
    def __init__(self, db_path: str):
        self.id_counter = 0
        self.tasks: dict[int, Task] = {} # Index : Task Object

        self.conn = sqlite3.connect(db_path)
    
    
    def load_local_db(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        db_tasks = cursor.fetchall()
        highest_id = 0
        for row in db_tasks:
            start_time = datetime.strptime(row[3], "%d/%m/%Y")
            end_time = datetime.strptime(row[4], "%d/%m/%Y")
            curr_task = Task(row[1], row[2], start_time, end_time, row[5])
            self.tasks[row[0]] = curr_task
            if row[0] > highest_id:
                highest_id = row[0]
        self.id_counter = highest_id+1
        
            
    
    def add_task(self, task: Task):
        self.tasks[self.id_counter] = task
        add_task_local(self.conn, self.id_counter, task.name, task.description, task.date_created, task.date_deadline)
        self.id_counter += 1
        
        
    def complete_task(self, task_id: int):
        self.tasks[task_id].toggle_complete()
        toggle_complete_local(self.conn, task_id)


    def remove_task(self, task_id: int):
        self.tasks.pop(task_id)
        remove_task_local(self.conn, task_id)
        
        
    def update_task(self, task_id: int, new_name: str, new_desc: str, new_deadline_str: str):
        # NOT THE BEST (or even a good) WAY TO DO IT BUT IT WORKS FOR NOW
        # Easiest way to handle skip cases
        if new_name != "-":  
            self.tasks[task_id].name = new_name
            update_task_name_local(self.conn, task_id, new_name)
        if new_desc != "-":  
            self.tasks[task_id].description = new_desc
            update_task_desc_local(self.conn, task_id, new_desc)
        if new_deadline_str != "-":
            new_deadline = datetime.strptime(new_deadline_str, "%d/%m/%Y")
            self.tasks[task_id].date_deadline = new_deadline
            update_task_deadline_local(self.conn, task_id, new_deadline_str)

    
    def get_task(self, task_id: int) -> Task:
        return self.tasks[task_id]
    
    
    def get_tasks_ids(self):
        return list(self.tasks.keys())
    