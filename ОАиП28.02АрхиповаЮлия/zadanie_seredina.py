from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def index():
    return 'Впишите в строчку браузера /seredina/число/число/число'

@app.route('/seredina/<int:a>/<int:b>/<int:c>')
def median_task(a, b, c):
    return render_template('seredina.html', a=a, b=b, c=c)

if __name__ == '__main__': 
    app.run(debug=True)