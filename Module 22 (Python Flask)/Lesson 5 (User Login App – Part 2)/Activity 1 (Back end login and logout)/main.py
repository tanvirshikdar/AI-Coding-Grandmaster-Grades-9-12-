from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        mydb = mysql.connector.connect(
            host="sql12.freesqldatabase.com",
            user="sql12824998",
            password="hl7wLwub8Q",
            database="sql12824998"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name = %s AND Password = %s", (username, password))
        account = mycursor.fetchone()
        
        if account:
            name = account[1]
            id = account[0]
            msg = 'Logged in Successfully'
            return render_template('index.html', msg=msg, name=name, id=id)
        else:
            msg = 'incorrect Credentials. Kindly check'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html', msg='')

@app.route('/logout')
def logout():
    msg = 'Logged out succesfully'
    return render_template('login.html', msg=msg, name='', id='')

if __name__ == '__main__':
    app.run(debug=True)