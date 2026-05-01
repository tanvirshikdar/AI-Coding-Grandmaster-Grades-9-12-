from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    if request.method == 'POST':
        try:
            dt1 = int(request.form.get('dt1'))
            m1 = int(request.form.get('m1'))
            year1 = int(request.form.get('year1'))

            dt2 = int(request.form.get('dt2'))
            m2 = int(request.form.get('m2'))
            year2 = int(request.form.get('year2'))

            n1 = date(year1, m1, dt1)
            n2 = date(year2, m2, dt2)

            diff = abs(n2 - n1)

            return render_template('index.html', difference=diff.days)
        
        except (ValueError, TypeError):
            # Handles invalid dates (like Feb 30th) or empty inputs
            return render_template('index.html', error="Please enter valid numeric dates.")

if __name__ == "__main__":
    app.run(debug=True)