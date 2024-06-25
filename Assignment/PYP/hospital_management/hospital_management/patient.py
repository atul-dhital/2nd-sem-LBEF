# patient.py
import datetime
from .data import patients, patient_id_counter, save_data

def calculate_age(birth_date):
    birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    if age < 0:
        raise ValueError("Invalid birth date")
    return age

def register_patient():
    global patient_id_counter
    patient_id = patient_id_counter
    patient_id_counter += 1
    name = input("Name: ")
    address = input("Address: ")
    birth_date = input("Date of Birth (YYYY-MM-DD): ")
    current_age = calculate_age(birth_date)
    contact_number = input("Contact Number (10 digits): ")
    while len(contact_number) != 10 or not contact_number.isdigit():
        print("Invalid contact number! Please enter a 10-digit number.")
        contact_number = input("Contact Number (10 digits): ")
    nationality = input("Nationality: ")
    
    print("Select Gender:")
    print("1. Male")
    print("2. Female")
    print("3. Others")
    gender_choice = input("Enter your choice: ")
    if gender_choice == "1":
        gender = "Male"
    elif gender_choice == "2":
        gender = "Female"
    elif gender_choice == "3":
        gender = "Others"
    else:
        print("Invalid choice. Defaulting to 'Others'.")
        gender = "Others"

    patient = {
        "id": patient_id,
        "name": name,
        "address": address,
        "birth_date": birth_date,
        "current_age": current_age,
        "contact_number": contact_number,
        "nationality": nationality,
        "gender": gender,
        "family_members": [],
        "medication_history": [],
        "visits": [],
        "status": "waiting"
    }
    patients[patient_id] = patient
    print(f"Patient {name} registered with ID {patient_id}.")
    save_data()

def register_family_member(patient_id):
    family_member = {
        "name": input("Name: "),
        "birth_date": input("Date of Birth in AD(YYYY-MM-DD): "),
        "gender": input("Gender: "),
        "current_age": input("Current Age: ")
    }
    patients[patient_id]["family_members"].append(family_member)
    print(f"Family member {family_member['name']} added to patient ID {patient_id}.")
    save_data()

def add_medication_history(patient_id):
    condition = input("Condition: ")
    patients[patient_id]["medication_history"].append(condition)
    print(f"Medication history updated for patient ID {patient_id}.")
    save_data()

def search_patient(patient_id):
    if patient_id in patients:
        view_patient(patient_id)
    else:
        print(f"Patient with ID {patient_id} not found.")

def view_drugs_prescription(patient_id):
    if patient_id in patients:
        if "prescriptions" in patients[patient_id]:
            print("Previous Drugs Prescription:")
            for prescription in patients[patient_id]["prescriptions"]:
                print(f"  - {prescription}")
        else:
            print("No previous drugs prescription found for this patient.")
    else:
        print(f"Patient with ID {patient_id} not found.")

def add_medical_result(patient_id):
    if patient_id in patients:
        result = input("Enter medical result: ")
        patients[patient_id]["visits"].append(result)
        print(f"Medical result added for patient ID {patient_id}.")
        save_data()
    else:
        print(f"Patient with ID {patient_id} not found.")

def add_medical_certificate(patient_id):
    if patient_id in patients:
        certificate = input("Enter medical certificate details: ")
        if "medical_certificates" not in patients[patient_id]:
            patients[patient_id]["medical_certificates"] = []
        patients[patient_id]["medical_certificates"].append(certificate)
        print("Medical certificate added.")
        save_data()
    else:
        print(f"Patient with ID {patient_id} not found.")

def view_medical_certificates(patient_id):
    if patient_id in patients:
        if "medical_certificates" in patients[patient_id]:
            print("Medical Certificates:")
            for certificate in patients[patient_id]["medical_certificates"]:
                print(f"  - {certificate}")
        else:
            print("No medical certificates found for this patient.")
    else:
        print(f"Patient with ID {patient_id} not found.")

def view_patient(patient_id):
    patient = patients[patient_id]
    print(f"Patient ID: {patient_id}")
    print(f"Name: {patient['name']}")
    print(f"Address: {patient['address']}")
    print(f"Date of Birth: {patient['birth_date']}")
    print(f"Current Age: {patient['current_age']}")
    print(f"Contact Number: {patient['contact_number']}")
    print(f"Nationality: {patient['nationality']}")
    print(f"Gender: {patient['gender']}")
    print("Family Members:")
    for member in patient["family_members"]:
        print(f"  - {member['name']} ({member['gender']}, {member['birth_date']})")
    print("Medication History:")
    for condition in patient["medication_history"]:
        print(f"  - {condition}")

def delete_patient(patient_id):
    if patient_id in patients:
        del patients[patient_id]
        print(f"Patient ID {patient_id} deleted.")
        save_data()
    else:
        print(f"Patient ID {patient_id} not found.")

def update_patient_status(patient_id, status):
    if patient_id in patients:
        patients[patient_id]["status"] = status
        print(f"Patient ID {patient_id} status updated to {status}.")
        save_data()
    else:
        print(f"Patient ID {patient_id} not found.")
