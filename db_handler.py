import sqlite3
from datetime import datetime

SQL_CREATE_TABLE = f"CREATE TABLE tasks (id INTERGER NOT NULL PRIMARY KEY, name TEXT, description TEXT, startDate TEXT, endDate TEXT)"

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


def add_task_local(conn: sqlite3.Connection, id: int, name: str, desc: str, startdate: datetime, enddate:datetime):
    cursor = conn.cursor()
    startstr = startdate.strftime("%d/%m/%Y")
    endstr = enddate.strftime("%d/%m/%Y")
    
    # TODO Check for ID clashes
    
    cursor.execute(f"INSERT INTO tasks VALUES('{id}', '{name}', '{desc}', '{startstr}', '{endstr}')")
    conn.commit()


def remove_task_local(conn: sqlite3.Connection, id):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM tasks WHERE id={id}")
    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("tasks_db.sqlite")
    # reset_local_db(conn)
    # add_task_local(conn, 1, "test", "desc", datetime.now(), datetime(2024,6,5))
    