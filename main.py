from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Dummy login logic
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('home'))
    return render_template('login.html')

if _name_ == '_main_':
    app.run(debug=True)