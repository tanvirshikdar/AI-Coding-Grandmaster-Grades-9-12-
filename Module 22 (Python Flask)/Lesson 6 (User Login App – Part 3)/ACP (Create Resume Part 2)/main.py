from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/resume', methods=['POST'])
def generate_resume():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        education = request.form['education']
        experience = request.form['experience']
        skills = request.form['skills']
        
        return render_template('resume.html', name=name, email=email, phone=phone, education=education, experience=experience, skills=skills)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)