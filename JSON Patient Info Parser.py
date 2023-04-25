import json
import os
from datetime import date
from datetime import datetime


# Function to recursively extract key values from nested JSON objects
def extract_key(json_obj, key):
    result = []
    if isinstance(json_obj, dict):
        for k, v in json_obj.items():
            if k == key:
                result.append(v)
            else:
                result.extend(extract_key(v, key))
    elif isinstance(json_obj, list):
        for item in json_obj:
            result.extend(extract_key(item, key))
    return result

# calculate age with variables
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <
           (birthDate.month, birthDate.day))

    return age


# local directory
directory = "C:\\Synthea2\\output\\EarInfectionFiles"
# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        # Open the JSON file
        with open(os.path.join(directory, filename), encoding="utf8") as f:
            nested_data = json.load(f)

            # find patient id
            find_id = extract_key(nested_data, 'id')[0]
            print(f'Patient id: {find_id}')

            # find patient Date of Birth
            find_DOB = extract_key(nested_data, 'birthDate')[0]
            print(f'Patient DOB: {find_DOB}')

            # calculates date variables with DOB
            dt = datetime.strptime(find_DOB, '%Y-%m-%d')

            # find patient age using function
            find_age = calculateAge(date(dt.year, dt.month, dt.day))
            print(f"Patient Age: {find_age} years")

            # find patient First Name
            find_first_name = extract_key(nested_data, 'given')[0][0]
            print(f'Patient First Name: {find_first_name}')

            # find patient Last Name
            find_last_name = extract_key(nested_data, 'family')[0]
            print(f'Patient Last Name: {find_last_name}')

            # find patient Gender
            find_gender = extract_key(nested_data, 'gender')[0]
            print(f'Patient Gender: {find_gender}\n')
