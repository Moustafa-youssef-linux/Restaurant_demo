from flask import Flask,render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/restaurants', methods=['GET'])
def home():
    error = None
    return render_template('restaurants.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('restaurants.html', error=error)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    error = None
    if request.method == 'POST':
        if request.form['username'] and request.form['password'] and request.form['fn'] and request.form['ln'] and request.form['age']:
            #error = 'Registration is done' 
            #print (request.form['username'])
            #return redirect(url_for('reg_result', error=error))
            return ("done")
            
        else:
            error = 'Please Fill all the inputs'
    return render_template('registration.html', error=error)

app.run()
