import mysql.connector
#Takes patient from database and prints to pycharm
#Need to use this file to figure out how to take information and display on website.

mydb = mysql.connector.connect(
  host="hcitDB.cmswaq8q4kav.us-east-1.rds.amazonaws.com",
  user="admin",
  password="POnMQIgR6AB3FbyYJ5DZ"
)

print(mydb)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM sys.Patient")

myresult = cursor.fetchall()

# Get Row as a list
row_data = []

for x in myresult:
  row_data = x

row = list(row_data)

print(row)
