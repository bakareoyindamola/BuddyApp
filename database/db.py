import sqlite3
connection = sqlite3.connect('BuddyApp.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS notification (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL)"

connection.execute(create_table)
connection.commit()
connection.close()