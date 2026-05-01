from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/resume', methods=['POST'])
def generate_resume():
    return render_template('resume.html', data=request.form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')