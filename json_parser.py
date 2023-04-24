import os
import json

# The directory containing the JSON files to search
directory = "C:\\Users\\govinda\\Desktop\\synthea\\output\\fhir"

# The numerical code to search for
target_code = "185345009"

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        # Open the JSON file
        with open(os.path.join(directory, filename), encoding="utf8") as f:
            data = json.load(f)

            # Check if the target code is in the JSON data
            if target_code in json.dumps(data):
                print(f"Found target code {target_code} in file {filename}")









