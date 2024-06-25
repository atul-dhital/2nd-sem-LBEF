# data.py
import os

# Sample data storage
users = {
    "receptionist": {"username": "receptionist", "password": "recpass"},
    "doctor": {"username": "doctor", "password": "docpass"},
    "pharmacist": {"username": "pharmacist", "password": "pharpass"},
    "cashier": {"username": "cashier", "password": "cashpass"}
}

patients = {}
patient_id_counter = 1
drugs = {}
drug_id_counter = 1

def load_data():
    global patients, drugs, patient_id_counter, drug_id_counter
    
    if not os.path.exists("patients.txt"):
        with open("patients.txt", "w") as file:
            file.write("{}")
    
    if not os.path.exists("drugs.txt"):
        with open("drugs.txt", "w") as file:
            file.write("{}")
    
    with open("patients.txt", "r") as file:
        patients = eval(file.read())
        patient_id_counter = max(patients.keys(), default=0) + 1 if patients else 1
    
    with open("drugs.txt", "r") as file:
        drugs = eval(file.read())
        drug_id_counter = max(drugs.keys(), default=0) + 1 if drugs else 1

def save_data():
    with open("patients.txt", "w") as file:
        file.write(str(patients))
    with open("drugs.txt", "w") as file:
        file.write(str(drugs))
