from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL


app = Flask(__name__)

# Configure db

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'rip'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        role_name = userDetails['role_name']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO roles (role_name) VALUES (%s)", (role_name,))
        mysql.connection.commit()
        cur.close()
    else:
        # get roles
        cur = mysql.connection.cursor()
        all_roles = cur.execute("SELECT * FROM roles")
        userDetails = ''
        if all_roles > 0:
            userDetails = cur.fetchall()
        mysql.connection.commit()
        cur.close()
    return render_template('index.html', userDetails=userDetails)

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
