import json
from datetime import datetime
import numpy as np

# Helper functions for validation and processing
def is_valid_mobile(number):
    if not number:
        return False
    # Remove any leading '+' if present
    if number.startswith('+'):
        number = number[1:]
    # Remove leading '91' if present
    if number.startswith('91'):
        number = number[2:]
    # Check if the remaining number is 10 digits and in the valid range
    return number.isdigit() and len(number) == 10 and 6000000000 <= int(number) <= 9999999999

def calculate_age(birth_date):
    if not birth_date:
        return None
    birth_date = datetime.fromisoformat(birth_date[:-1])  # Parse date
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Load data
file_path = './data/DataEngineeringQ2.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Process the data (including missing values, age, medicines, etc.)

# Save the updated data to a new file
updated_file_path = './data/Updated_DataEngineeringQ2.json'
with open(updated_file_path, 'w') as updated_file:
    json.dump(data, updated_file, indent=4)

print("Data processing complete. Updated file saved.")