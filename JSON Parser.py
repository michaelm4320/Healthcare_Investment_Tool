import os
import json

# The directory containing the JSON files to search
directory = "C:\\Synthea2\\output\\fhir"

# The numerical code to search for
target_code = 129127001

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        # Open the JSON file
        with open(os.path.join(directory, filename)) as f:
            print(f)
            data = json.load(f)

            # Check if the target code is in the JSON data
            if isinstance(data, list):
                for item in data:
                    if item.get('code') == target_code:
                        print(f"Found target code {target_code} in file {filename}")
                        break
            elif isinstance(data, dict):
                if data.get('code') == target_code:
                    print(f"Found target code {target_code} in file {filename}")