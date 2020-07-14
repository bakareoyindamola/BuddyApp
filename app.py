from flask import Flask, render_template, request
from database import database_manager

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method ==  "POST":
        email = request.form['email']  
        result = database_manager.find_by_email(email)
        if result is not None:
            return "Email Exist"
        database_manager.insert_into_db(email)    
    return render_template("index.html", name="Buddy App")

if __name__ == "__main__":
    app.run(debug=True)