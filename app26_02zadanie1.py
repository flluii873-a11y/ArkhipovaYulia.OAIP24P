from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    number = float(request.args.get('number', 0))
    doubled_number = number * 2
    text = f"Ваше число {number}, умноженное на 2: {doubled_number}"
    
    return render_template('index26_02zadanie1.html', 
                           number=doubled_number,
                           text=text)

if __name__ == '__main__':
    app.run(debug=True)