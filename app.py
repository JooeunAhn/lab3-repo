
from flask import Flask
from flask_mysqldb import MySQL
from flask import render_template
from flask import abort, redirect, url_for

mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'qwe123'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = "35.189.82.155"
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return render_template('index.html', rv=str(rv))      #Return the data in a string format

@app.route("/add/<student_name>/")
def add(student_name):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO students (studentName, email) values ("%s", "%s@mydit.ie");' % (student_name, student_name,))
    rv = cur.fetchall()
    return render_template('index.html', rv=str(rv))

@app.route("/edit/<old_student_name>/<new_student_name/")
def edit(old_student_name, new_student_name):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE %s SET studentName = %s WHERE studentName = %s" % (app.config["MYSQL_DB"], new_student_name, old_student_name)
    return redirect(url_for('hello'))

@app.route("/delete/<student_name>/")
def delete(student_name):
    cur = mysql.connection.cursor()
    cur.execute("DELETE %s WHERE studentName= %s" % (app.config["MYSQL_DB"], student_name)
    return redirect(url_for('hello'))
 



if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000

