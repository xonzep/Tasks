import click
import sqlite3

# create our task database

connection = sqlite3.connect("tasks.db")

print(connection.total_changes)

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    description TEXT,
                    status TEXT,
                    priority TEXT,
                    due_date TEXT,
                    created_at TEXT
                )''')

connection.commit()
connection.close()
