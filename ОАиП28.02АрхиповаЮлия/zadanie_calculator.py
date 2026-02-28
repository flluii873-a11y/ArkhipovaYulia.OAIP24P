from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Впишите в строчку браузера числа через слэш'

@app.route('/<float:n1>/<string:op>/<float:n2>/')
def calculator(n1, op, n2):
    return render_template('index.html', n1=n1, op=op, n2=n2)

if __name__ == '__main__':
    app.run(debug=True)