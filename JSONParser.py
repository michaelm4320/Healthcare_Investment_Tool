import os
import json
import shutil

# The directory containing the JSON files to search
directory = "C:\\Synthea2\\output\\fhir"

# The numerical code to search for (Otitis media)
target_code = "65363002"

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        # Open the JSON file
        with open(os.path.join(directory, filename), encoding="utf8") as f:
            data = json.load(f)

            # Check if the target code is in the JSON data
            if target_code in json.dumps(data):
                print(f"Found target code {target_code} in file {filename}")

                # copies json file to new folder
                src = os.path.join(directory, filename)
                dst = 'C:\Synthea2\output\EarInfectionFiles'
                # uses paths to copy
                shutil.copy(src, dst)
