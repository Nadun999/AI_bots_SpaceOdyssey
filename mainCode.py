from flask import Flask, render_template, url_for, request, session
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# import re

app = Flask(__name__)

# app.secret_key = 'xyzsdfg'
  
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'rootcode'
  
# mysql = MySQL(app)


# @app.route('/login', methods =['GET', 'POST'])
# def login():
#     return render_template('login.html')


# @app.route('/register', methods =['GET', 'POST'])
# def register():
#     return render_template('signup.html')

# @app.route('/destination_page')
# def explore_planets():
#     return render_template('destination.html')

# @app.route('/profile')
# def profile():
#     return render_template('profile.html')    

# @app.route('/book_flight')
# def book_flight():
#     return render_template('book_flight.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/aboutus')
def aboutUs():
    return render_template('aboutus.html')


if __name__ == '__main__':
    app.run(debug=True)



# @app.route('/login', methods =['GET', 'POST'])
# def login():
#     msg = ''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         username = request.form['username']
#         password = request.form['password']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM user WHERE username = % s AND password = % s', (username, password, ))
#         account = cursor.fetchone()
#         if account:
#             session['loggedin'] = True
#             session['id'] = account['id']
#             session['username'] = account['username']
#             msg = 'Logged in successfully !'
#             return render_template('home.html', msg = msg)
#         else:
#             msg = 'Incorrect username / password !'
#     return render_template('login.html', msg = msg)



# @app.route('/register', methods =['GET', 'POST'])
# def register():
#     msg = ''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM user WHERE username = % s', (username, ))
#         account = cursor.fetchone()
#         if account:
#             msg = 'Account already exists !'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             msg = 'Invalid email address !'
#         elif not re.match(r'[A-Za-z0-9]+', username):
#             msg = 'Username must contain only characters and numbers !'
#         elif not username or not password or not email:
#             msg = 'Please fill out the form !'
#         else:
#             cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (username, email, password, ))
#             mysql.connection.commit()
#             msg = 'You have successfully registered !'
#             return render_template('login.html', msg = msg)
#     elif request.method == 'POST':
#         msg = 'Please fill out the form !'
#     return render_template('signup.html', msg = msg)

