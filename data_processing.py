import pymysql

mydb = pymysql.connect(
    host='hcitDB.cmswaq8q4kav.us-east-1.rds.amazonaws.com',
    port=3306,
    user='admin',
    password='POnMQIgR6AB3FbyYJ5DZ',
    db='sys'
)


def get_age_info(age_condition):
    cursor = mydb.cursor()
    query = "SELECT * FROM sys.Patient WHERE " + age_condition + ";"
    cursor.execute(query)
    myresult = cursor.fetchall()
    return len(myresult)


age_data = []

age_ranges = ["Age <= 15", "Age >= 16 AND Age <=30", "Age >= 31 AND Age <= 45", "Age >= 46 AND Age <= 60",
              "Age >= 61 AND Age <= 75", "Age >= 76 AND Age <= 90", "Age >= 91 AND Age <= 110"]

for age in age_ranges:
    age_data.append(get_age_info(age))

print(age_data)


def get_insurance_data(insurance_nane):
    cursor = mydb.cursor()
    query = "SELECT * FROM sys.Patient WHERE Insurance = '" + insurance_nane + "';"
    print(query)
    cursor.execute(query)
    myresult = cursor.fetchall()
    return len(myresult)


insurance_list = ["Aetna", "Anthem", "Blue Cross Blue Shield", "Cigna Health", "Humana", "Medicaid", "NO_INSURANCE",
                  "UnitedHealthcare"]

insurance_data = []

for insurance in insurance_list:
    insurance_data.append(get_insurance_data(insurance))

print(insurance_data)


def get_city_data(city):
    cursor = mydb.cursor()
    query = "SELECT * FROM sys.Patient WHERE City = '" + city + "';"
    print(query)
    cursor.execute(query)
    myresult = cursor.fetchall()
    return len(myresult)


city_list = ["Fort Myers", "Jacksonville", "Miami", "Orlando", "Tampa"]

city_data = []

for city in city_list:
    city_data.append(get_city_data(city))