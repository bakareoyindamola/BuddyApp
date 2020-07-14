from flask import Flask, render_template, request
from database import database_manager

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method ==  "POST":
        email = request.form['email']
        if not email:
            return render_template("index.html", name="Buddy App", message='Email cannot be blank') 
        result = database_manager.find_by_email(email)
        if result is not None:
            return render_template("index.html", name="Buddy App", message='Email Exist')
        database_manager.insert_into_db(email)
        return render_template("index.html", name="Buddy App", message="Email captured successfully")    
    return render_template("index.html", name="Buddy App", message='')

if __name__ == "__main__":
    database_manager.create_database()
    app.run(debug=False)