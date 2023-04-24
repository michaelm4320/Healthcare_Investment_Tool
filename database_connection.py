import mysql.connector


mydb = mysql.connector.connect(
  host="hcitDB.cmswaq8q4kav.us-east-1.rds.amazonaws.com",
  user="admin",
  password="POnMQIgR6AB3FbyYJ5DZ"
)

print(mydb)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM sys.Patient")

myresult = cursor.fetchall()

print(myresult)

for x in myresult:
  print(x)