from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST' and 'input_string' in request.form:
        input_string = request.form.get('input_string')
        number_of_vowels = 0
        cleaned_string = input_string.lower()
        
        for i in cleaned_string:
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                number_of_vowels += 1
                
        return render_template('index.html', number_of_vowels=number_of_vowels, original_text=input_string)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)