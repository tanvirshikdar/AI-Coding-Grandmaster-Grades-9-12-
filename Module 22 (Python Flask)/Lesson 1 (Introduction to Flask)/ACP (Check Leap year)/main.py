from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_leap_year():
    try:
        year = int(request.form["year"])
        
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            result = f"{year} is a Leap Year!"
            is_leap = True
        else:
            result = f"{year} is not a Leap Year."
            is_leap = False

        return render_template("index.html", result=result, is_leap=is_leap)

    except ValueError:
        return render_template("index.html", error="Please enter a valid numeric year.")

if __name__ == "__main__":
    app.run(debug=True)