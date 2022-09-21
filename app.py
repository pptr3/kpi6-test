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
    print(id_role) # here we have the ID of the new user+role\
    if request.method == 'POST':

        # Fetch form data
        userDetails = request.form
        print(userDetails)
        new_role = userDetails['new_role']
        #print(new_role) # this is what is in the user+role field
        # insert new user + role
        #cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO users (user_name, role_id_user) VALUES (%s, %s)", (new_user,id_role,))
        #mysql.connection.commit()
        #cur.close()

        # Fetch form data
        if not new_role:
            print("here: ")
            print(userDetails)
            new_user = userDetails['new_user']
            #print(new_user) # this is what is in the user+role field
            # insert new user + role
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (user_name, role_id_user) VALUES (%s, %s)", (new_user,id_role,))
            mysql.connection.commit()
            cur.close()

    cur = mysql.connection.cursor()
    all_roles = cur.execute("SELECT * FROM roles")
    userDetails = ''
    if all_roles > 0:
        userDetails = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('index.html', userDetails=userDetails)



if __name__ == '__main__':
    app.run(debug=True)
