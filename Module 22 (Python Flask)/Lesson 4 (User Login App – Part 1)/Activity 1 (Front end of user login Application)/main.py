from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', msg='')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html', msg='')

@app.route('/logout')
def logout():
    return render_template('login.html', msg='')

if __name__ == '__main__':
    app.run(debug=True)