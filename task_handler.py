import json
import requests


class Task_handler:
    def __init__(self, cloud_db_url: str):
        self.tasks = {} # <Name> : <Task>
        self.cloud_db_url = cloud_db_url # Firebase URL
    
    def create_task(self, name: str, task: str):
        try:
            self.tasks[name] = task
            return 1
        except:
            return 0
        
        
    def delete_task(self, name: str):
        try:
            self.tasks.pop(name)
            return 1
        except:
            return 0
        
        
    def get_tasks(self):
        return self.tasks
    
    
    def load_file(self, file_path:str):
        with open(file_path) as json_file:
            json_data = json.load(json_file)
            tasks_data = json_data["Tasks"]
            for task in tasks_data:
                name = task["Name"]
                description = task["Description"]
                self.tasks[name] = description
    
    
    def save_file(self, file_path:str):
        with open(file_path, "w+") as json_file:
            json_data = {}
            tasks_data = []
            for name, desc in self.tasks.items():
                task = {}
                task["Name"] = name
                task["Description"] = desc
                tasks_data.append(task)
            json_data["Tasks"] = tasks_data
            
            print(json_data)
            json_file.write(json.dumps(json_data, indent=4))
        
        
    def upload_to_cloud(self, file_path):
        with open(file_path) as json_file:
            json_data = json.load(json_file)
            payload = json.dumps(json_data, indent=4)
            r = requests.put(self.cloud_db_url+".json", data=payload)
            print(r.content)
        
        
    def download_from_cloud(self, file_path):
        content = requests.get(self.cloud_db_url+".json")
        print(content.json())
        with open(file_path, "w+") as json_file:
            json_file.write(json.dumps(content.json(), indent=4))
