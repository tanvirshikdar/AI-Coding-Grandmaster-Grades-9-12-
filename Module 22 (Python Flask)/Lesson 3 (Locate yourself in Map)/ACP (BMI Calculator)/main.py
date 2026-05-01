from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    bmi = ''
    if request.method == 'POST' and 'Weight' in request.form and 'Height' in request.form:
        try:
            weight = float(request.form.get('Weight'))
            height = float(request.form.get('Height'))
            
            bmi = round(weight / ((height / 100) ** 2), 2)
            
            return render_template("index.html", bmi=bmi)
        except (ValueError, ZeroDivisionError):
            return render_template("index.html", error="Please enter valid numbers.")
            
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)