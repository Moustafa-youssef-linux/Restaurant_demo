from flask import Flask,render_template, redirect, url_for, request
import  db_module

app = Flask(__name__)


@app.route("/")
def entry():
    return render_template('entry.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = "Athentication Faild!,Please Register"
    print (request.method)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        exist = db_module.auth_(username,password)
        if not exist  :
            #error = 'Invalid Credentials. Please try again.'
            #data = db_module.database_con()
            return str(error)
            #error = data
        elif exist and username =='admin' :
            return redirect(url_for('admin_console'))
        else:
            return redirect(url_for('restaurant'))
    return render_template('login.html', error=error)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    error = None
    print (request.method)
    if request.method == 'POST':
        u_ = request.form['username']
        fn_ = request.form['fn']
        ln_ = request.form['ln']
        age_ = request.form['age']
        pass_ = request.form['password']
        gender_ = request.form['gender']
        print (u_+ pass_ + ln_ + age_ + gender_ + pass_)
        if  u_ !=  'admin':
          result= db_module.register_(u_,fn_,ln_,age_,gender_,pass_)
          #return redirect(url_for('reg_result', error=error))
          return str("Registration is done.")
        else:
            error = 'Please Fill all the inputs'
    return render_template('registration.html', error=error)
#####
###INSERT INTO users (username,fn,ln,age,gender,password)
##    -> values ("admin","admin","admin",28,"male","admin@123");

#
@app.route('/restaurants', methods=['GET'])
def restaurant():
    error = None
    if request.method == 'GET':
        data = db_module.get_rest()
    return render_template('restaurants.html', restaurants=data)



@app.route('/admin_console', methods=['GET', 'POST'])
def admin_console():
    error = None
    if request.method == 'GET':
        select = request.form.get('actions')
        #print (select)
        return render_template('console.html')
    else:
        #error = "Wrong url"
        select = request.form.get('actions')
        if select == 'read':
            return redirect(url_for('restaurant'))
        elif select == 'add':
            return redirect(url_for('create_rest'))
        #print (select)
        return str(select)


@app.route('/rest/create', methods=['GET', 'POST'])
def create_rest():
    error = None
    if request.method == 'GET':
        return render_template('create.html')
        



app.run()
