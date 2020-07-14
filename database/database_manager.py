import sqlite3

def find_by_email(email):
    connection = sqlite3.connect("./database/BuddyApp.db")
    cursor = connection.cursor()
    query = "SELECT email from notification WHERE email=?"
    cursor.execute(query, (email,))
    record = cursor.fetchone()
    connection.close()
    return record

def insert_into_db(email):
    connection = sqlite3.connect("./database/BuddyApp.db")
    cursor = connection.cursor()
    query = "INSERT INTO notification VALUES (NULL, ?)"
    cursor.execute(query, (email,))
    connection.commit()
    connection.close()
