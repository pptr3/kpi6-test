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
    id_role = request.form.get('all_roles')
    if request.method == 'POST':
        # insert new role
        userDetails = request.form
        if userDetails and 'new_role' in userDetails:
            new_role = userDetails['new_role']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO roles (role_name) VALUES (%s)", (new_role,))
            mysql.connection.commit()
            cur.close()

        # insert new user and assign to a role
        if userDetails and 'new_user' in userDetails:
            new_user = userDetails['new_user']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (user_name, role_id_user) VALUES (%s, %s)", (new_user,id_role,))
            mysql.connection.commit()
            cur.close()

    cur = mysql.connection.cursor()
    all_roles = cur.execute("SELECT role_id, role_name FROM roles GROUP BY role_name")
    userDetails = ''
    if all_roles > 0:
        userDetails = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('index.html', userDetails=userDetails)

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT distinct user_name, role_name FROM users u, roles r WHERE u.role_id_user = r.role_id ")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)


if __name__ == '__main__':
    app.run(debug=True)
