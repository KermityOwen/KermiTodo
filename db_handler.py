import sqlite3
from datetime import datetime

SQL_CREATE_TABLE = f"CREATE TABLE tasks (id INTERGER NOT NULL PRIMARY KEY, name TEXT, description TEXT, startDate TEXT, endDate TEXT, complete INTEGER NOT NULL)"

SQL_DELETE_TABLE = f"DROP TABLE tasks"


def init_local_db(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute(SQL_CREATE_TABLE)
    
    
def reset_local_db(conn: sqlite3.Connection):
    cursor = conn.cursor()
    try:
        cursor.execute(SQL_DELETE_TABLE)
    except:
        pass
    cursor.execute(SQL_CREATE_TABLE)

def toggle_complete_local(conn: sqlite3.Connection, id: int):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE tasks SET complete = ((complete | 1) - (complete & 1)) WHERE id = {id}")
    conn.commit()


def add_task_local(conn: sqlite3.Connection, id: int, name: str, desc: str, startdate: datetime, enddate:datetime):
    cursor = conn.cursor()
    startstr = startdate.strftime("%d/%m/%Y")
    endstr = enddate.strftime("%d/%m/%Y")
    # TODO Check for ID clashes
    cursor.execute(f"INSERT INTO tasks VALUES('{id}', '{name}', '{desc}', '{startstr}', '{endstr}', '0')") # 0 as boolean for False
    conn.commit()


def remove_task_local(conn: sqlite3.Connection, id):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM tasks WHERE id={id}")
    conn.commit()
    
    
def update_task_name_local(conn: sqlite3.Connection, id:int, new_name: str):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE tasks SET name = ('{new_name}') WHERE id = {id}")
    conn.commit()


def update_task_desc_local(conn: sqlite3.Connection, id:int, new_desc: str):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE tasks SET description = ('{new_desc}') WHERE id = {id}")
    conn.commit()
    
    
def update_task_deadline_local(conn: sqlite3.Connection, id:int, new_deadline: str):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE tasks SET endDate = ('{new_deadline}') WHERE id = {id}")
    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("tasks_db.sqlite")
    reset_local_db(conn)
    # add_task_local(conn, 1, "test", "desc", datetime.now(), datetime(2024,6,5))
    