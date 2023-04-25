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

    # Print rows with counter
    """total = 1
    for x in myresult:
        print(x, total)
        total += 1"""


fifteen_or_less = get_age_info("Age <= 15")  # 92

sixteen_to_thirty = get_age_info("Age >= 16 AND Age <=30")  # 9

thirty1_to_forty5 = get_age_info("Age >= 31 AND Age <= 45")  # 8

forty6_to_sixty = get_age_info("Age >= 46 AND Age <= 60")  # 9

sixty1_to_seventy5 = get_age_info("Age >= 61 AND Age <= 75")  # 18

seventy6_to_ninety = get_age_info("Age >= 76 AND Age <= 90")  # 12

ninety1_to_110 = get_age_info("Age >= 91 AND Age <= 110")  # 14

age_data = [fifteen_or_less, sixteen_to_thirty, thirty1_to_forty5, forty6_to_sixty, sixty1_to_seventy5,
            seventy6_to_ninety, ninety1_to_110]
