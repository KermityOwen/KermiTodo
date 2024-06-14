python -m venv ./todo_venv
source ./todo_venv/bin/activate

pyinstaller --onefile --paths ./todo_venv/lib/python3.8/site-packages/ ./src/main.py