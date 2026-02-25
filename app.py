from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/me')
def me_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        
        #Проверка пароля
        if user == 'admin' and pwd == '1234':
            return redirect('/me')
        else:
            return render_template('login.html', error='Неверный парольчик или логинчик')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)