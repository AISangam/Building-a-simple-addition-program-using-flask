# Building-a-simple-addition-program-using-flask  

![Entries_stored](https://user-images.githubusercontent.com/35392729/54876968-79ce1a80-4e3e-11e9-955b-4f49e77896bc.png)

# What does this code provides to you???  
<ul>
  <li>Creating an api using flask microframework.</li>
  <li>Sending the data from the html page to the database using POST method and python coding</li>
  <li>Database connectivity with the back end uisng python programming language</li>
  <li> Restricting the entries to the database as unique so as to remove the redundancy in the database.</li>
  <li>Installing phpmyadmin, php, apache2,mysql to save the entries in the database in a graphical user interface format for better visualization</li>
</ul>  

## Creating an api using flask microframework  
Flask is a microframework which is very light weight and is very beneficial for a beginner who wants to create api. To satrt with it we need the module flask which can be imported using the below command
```
from flask import Flask,request
```
If flask is not installed, please install it using below command
```
pip install flask
```
Concept says that when you enter data at the fronend like in the html page as shown below  
![frontend](https://user-images.githubusercontent.com/35392729/54877139-82bfeb80-4e40-11e9-8012-7b8348c9a67c.png)  
This data is redirected to the function created by @app.route which is the functionality of flask using the request method which may be post or get. In this way data is fetched from the front end using python programming language and request method. Please have a look at the below code to understand the concept in more details  
```
@app.route('/add',methods = ['POST'])
def add():
  if request.method == 'POST':
    first_nu = request.form['first number']
    second_nu =   request.form['second number']
```
## Sending the data from the html page to the database using POST method and python coding  
To complete this step we have used form action in the html page so that when user click on the submit buttion it is directed to the url which is mentioned in the form action. Data entered in the html page is then fetched using the appropriate method used in the function created for such url using flask. Have a look at the below code
```
#coding done in the html page for redirecting to the below url when submit button is clicked
<form action="http://localhost:5000/add" method="POST" >
```
```
#same url is called here as data will be received here
@app.route('/add',methods = ['POST'])
def add():
  if request.method == 'POST':
    first_nu = request.form['first number']
    second_nu =   request.form['second number']
```     
## Database connectivity with the back end uisng python programming language  
Vision is to append numbers and their addtions to the database so it is very important that backend is connected to the database. Please use the below command to implement the above.  
```
mydb = mysql.connector.connect(
    host="localhost",
    #replace with your username  which you have created while installing phpmyadmin
    user="xxxx",
    ##replace with your password  which you have created while installing phpmyadmin
    passwd="xxxxx",
    database="addition"
  )
  print("Connection is established...")

``` 
For this step, you need to import mysql.connector and if it is not installed please install it with the below command
```
pip install mysql.connector
```

## Restricting the entries to the database as unique so as to remove the redundancy in the database
This step is very important and i personally feel that same  entries should not be repeated. To perform this step please append the word unique with each column name for a table which you will create for a database, For more details, please have a look at the below code.  
```
sql="CREATE TABLE Addition_flask (id int NOT NULL AUTO_INCREMENT,first_number varchar(20) UNIQUE, second_number varchar(20) UNIQUE, sum varchar(20), PRIMARY KEY (id))"
```
## Installing phpmyadmin, php, apache2,mysql to save the entries in the database in a graphical user interface format for better visualization  

To install apache2 please follow this link https://websiteforstudents.com/installing-apache2-mariadb-on-ubuntu-16-04-17-10-18-04-with-php-7-2-support-lamp/  
To install mysql please follow https://support.rackspace.com/how-to/installing-mysql-server-on-ubuntu/  
To install php, please execute the below command
```
sudo apt install php7.2-cli
```
To install phpmyadmin please follow this link https://www.hostingadvice.com/how-to/install-phpmyadmin-on-ubuntu/

## How to run this code  
To run this code, please run the file database_connectivity.py first because it will run the flask at 5000 port. To run this file please execute the below code
```
python database_connectivity.py  
```
Now open the file frontend.html in the browser and play with the code. I hope you will learn a lot from this ReadMe file. I have elaborated points keeping the begginers in my mind. 


  
  
