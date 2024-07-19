import json


with open('DataEngineeringQ2.json', 'r') as f:
    data = json.load(f)


missing_first_name = 0
missing_last_name = 0
missing_birth_date = 0


for record in data:
    if record.get('patientDetails', {}).get('firstName', '') == '':
        missing_first_name += 1
    if record.get('patientDetails', {}).get('lastName', '') == '':
        missing_last_name += 1
    if record.get('patientDetails', {}).get('birthDate') is None:
        missing_birth_date += 1


total_records = len(data)
percent_missing_first_name = round((missing_first_name / total_records) * 100, 2)
percent_missing_last_name = round((missing_last_name / total_records) * 100, 2)
percent_missing_birth_date = round((missing_birth_date / total_records) * 100, 2)


print(f"{percent_missing_first_name},{percent_missing_last_name},{percent_missing_birth_date}")


import json
from statistics import mode


with open('DataEngineeringQ2.json', 'r') as f:
    data = json.load(f)


gender_values = [record.get('patientDetails', {}).get('gender', '') for record in data]


mode_gender = mode(gender_values)


imputed_gender_values = [gender if gender else mode_gender for gender in gender_values]


female_count = imputed_gender_values.count('Female')


total_records = len(imputed_gender_values)
percentage_female = round((female_count / total_records) * 100, 2)


print(percentage_female)




import json
from datetime import datetime


with open('DataEngineeringQ2.json', 'r') as f:
    data = json.load(f)


import json
from datetime import datetime




def calculate_age_group(birth_date_str):
    if birth_date_str is None:
        return None
    birth_date_str = birth_date_str.split('T')[0]


    birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


    if age <= 12:
        return 'Child'
    elif 13 <= age <= 19:
        return 'Teen'
    elif 20 <= age <= 59:
        return 'Adult'
    else:
        return 'Senior'


for record in data:
    birth_date_str = record.get('patientDetails', {}).get('birthDate')
    age_group = calculate_age_group(birth_date_str)
    record['ageGroup'] = age_group


adult_count = sum(1 for record in data if record.get('ageGroup') == 'Adult')


print(adult_count)


import json


with open('DataEngineeringQ2.json', 'r') as f:
    data = json.load(f)


total_medicines = 0
num_records_with_medicines = 0


for record in data:
    medicines = record.get('consultationData', {}).get('medicines', [])
    if medicines:  
        total_medicines += len(medicines)
        num_records_with_medicines += 1




if num_records_with_medicines > 0:
    average_medicines = round(total_medicines / num_records_with_medicines, 2)
else:
    average_medicines = 0 


print(average_medicines)




import json
from collections import Counter


with open('DataEngineeringQ2.json', 'r') as f:
    data = json.load(f)


all_medicines = []


for record in data:
    medicines = record.get('consultationData', {}).get('medicines', [])
    for medicine in medicines:
        medicine_name = medicine.get('medicineName')
        if medicine_name:
            all_medicines.append(medicine_name)


medicine_counts = Counter(all_medicines)


third_most_common = medicine_counts.most_common(3)[2][0]


print(third_most_common)


import json


with open('DataEngineeringQ2.json', 'r') as f:
    data = json.load(f)


active_count = 0
inactive_count = 0


for record in data:
    medicines = record.get('consultationData', {}).get('medicines', [])
    for medicine in medicines:
        if medicine.get('isActive'):
            active_count += 1
        else:
            inactive_count += 1


total_medicines = active_count + inactive_count


if total_medicines > 0:
    active_percentage = round((active_count / total_medicines) * 100, 2)
    inactive_percentage = round((inactive_count / total_medicines) * 100, 2)
else:
    active_percentage = 0
    inactive_percentage = 0


print(f"{active_percentage},{inactive_percentage}")


import json


with open('updated_data.json', 'w') as f:
       json.dump(data, f, indent=2) 
def is_valid_indian_number(phone_number):
    """
    Checks if a phone number is a valid Indian number (basic validation).


    Args:
        phone_number: The phone number string.


    Returns:
        True if valid, False otherwise.
    """
    if not phone_number:
        return False 


    if not phone_number.isdigit():
        return False  


    if len(phone_number) != 10:
        return False  


    if not phone_number.startswith(('6', '7', '8', '9')):
        return False 
    return True  
for record in data:
    phone_number = record.get('phoneNumber')
    is_valid = is_valid_indian_number(phone_number)
    record['isValidMobile'] = is_valid
    valid_count = sum(1 for record in data if record.get('isValidMobile'))
    invalid_count = sum(1 for record in data if not record.get('isValidMobile'))


print("Valid phone numbers:", valid_count)
print("Invalid phone numbers:", invalid_count)
import json
from datetime import datetime
from scipy.stats import pearsonr


with open('DataEngineeringQ2.json', 'r') as f:
    data = json.load(f)


def calculate_age(birth_date_str):
    if birth_date_str is None:
        return None


    birth_date_str = birth_date_str.split('T')[0]


    birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


ages = []
num_medicines = []


for record in data:
    age = calculate_age(record.get('patientDetails', {}).get('birthDate'))
    medicines = record.get('consultationData', {}).get('medicines', [])


    if age is not None:
        ages.append(age)
        num_medicines.append(len(medicines))


if ages and num_medicines:
    correlation, _ = pearsonr(ages, num_medicines)
    print(round(correlation, 2))  
else:
    print("Not enough data to calculate correlation.")



