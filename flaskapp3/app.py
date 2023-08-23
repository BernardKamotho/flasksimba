from flask import Flask
from flask import render_template,request,redirect
import pymysql

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST','GET'])
def signup():

    if request.method == 'POST':

        # get for mdata
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm_password')

        # validate the form data
        if not username or not email or not password or not confirm:
            return render_template('signup.html', message ="Error: please fill in all fields")
        elif password != confirm:
            return render_template('signup.html', message = "Error : password do not match confirm password")
        # check is the user existxs in the db
        else:
        # register the user
            connection = pymysql.connect(host='localhost', user='root', password='',
                                                    database='workers')
        
            sql = "insert into Employees (username, email, password) values(%s, %s, %s)"

            cursor = connection.cursor()

            cursor.execute(sql,(username, email, password))

            connection.commit()

            return 'Registration Successful \n' '<a style="color:blue;" href =/signup>Go Back</a>'
    else:
        return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)