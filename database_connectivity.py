import mysql.connector
from flask import Flask,request
app = Flask(__name__)

@app.route('/add',methods = ['POST'])
def add():
  if request.method == 'POST':
    first_nu = request.form['first number']
    second_nu =   request.form['second number']

  mydb = mysql.connector.connect(
    host="localhost",
    user="datascience",
    passwd="aisangam",
    database="addition"
  )
  print("Connection is established...")

  #creating a new database
  cursor=mydb.cursor()
  # cursor.execute("CREATE DATABASE addition")
  # print("Database is created.")

  #sql="CREATE TABLE Addition_flask (id int NOT NULL AUTO_INCREMENT,first_number varchar(20) , second_number varchar(20), sum varchar(20), PRIMARY KEY (id))"
  #cursor.execute(sql)
  #mydb.commit()

  sql = "INSERT INTO Addition_flask(first_number, second_number, sum) VALUES (%s, %s, %s)"
  sum = int(first_nu) + int(second_nu)
  values= ([first_nu, second_nu, sum])
  cursor.execute(sql, values)
  mydb.commit()
  mydb.close()
  return "thank you, database has been saved"


if __name__ == '__main__':
   app.run(debug = True)

