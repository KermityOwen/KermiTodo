import sqlite3
from datetime import datetime
from db_handler import *

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
        # validity = (date_created < date_deadline) and validity
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
        for row in db_tasks:
            start_time = datetime.strptime(row[3], "%d/%m/%Y")
            end_time = datetime.strptime(row[4], "%d/%m/%Y")
            curr_task = Task(row[1], row[2], start_time, end_time)
            self.tasks[row[0]] = curr_task
            
    
    def add_task(self, task:Task):
        self.tasks[self.id_counter] = task
        add_task_local(self.conn, self.id_counter, task.name, task.description, task.date_created, task.date_deadline)
        self.id_counter += 1
        
        
    def complete_task(self, task_id: int):
        self.tasks[task_id].toggle_complete()


    def remove_task(self, task_id: int):
        self.tasks.pop(task_id)
        remove_task_local(self.conn, task_id)
        
        
    def get_task(self, task_id: int):
        return self.tasks[task_id]
    
    
    def get_tasks_ids(self):
        return list(self.tasks.keys())


if __name__ == "__main__":
    task_handler = Tasks_handler("tasks_db.sqlite")
    
    task1 = Task("name1", "ipsum loren yadda yadda yoo", datetime.now(), datetime(2024,6,10))
    task2 = Task("name2", "ipsum loren yadda yadda yoo2", datetime.now(), datetime(2024,6,1))
    task3 = Task("name3", "ipsum loren yadda yadda yoo3", datetime.now(), datetime(2024,6,10))
    task_handler.add_task(task1)
    task_handler.add_task(task2)
    task_handler.add_task(task3)
    
    task_handler.load_local_db()
    print(task_handler.get_tasks_ids())
    print(task_handler.get_task(0))
    
    