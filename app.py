import os
import io
import sqlite3
import csv
from flask import Flask, render_template, request, send_file, make_response
from database import database_manager

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method ==  "POST":
        email = request.form['email']
        if not email:
            return render_template("index.html", name="Buddy App", message='Email cannot be blank!', success=None) 
        result = database_manager.find_by_email(email)
        if result is not None:
            return render_template("index.html", name="Buddy App", message='Email Exist, please try another email', success=False)
        database_manager.insert_into_db(email)
        return render_template("index.html", name="Buddy App", success=True)
    return render_template("index.html", name="Buddy App", message='', success='')

@app.route('/export')
def export():
    string_io = io.StringIO()
    csv_writer = csv.writer(string_io)
    connection = sqlite3.connect("./database/BuddyApp.db")
    cursor = connection.cursor()
    query = "SELECT * FROM notification"
    cursor.execute(query)
    rows = cursor.fetchall()
    csv_writer.writerow(i[0] for i in cursor.description)
    csv_writer.writerows(rows)
    response = make_response(string_io.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=buddy_app_subscribers_email.csv'
    response.headers['Content-type'] = 'text/csv'
    return response

if __name__ == "__main__":
    database_manager.create_database()
    app.run(debug=True)
