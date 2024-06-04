import getpass
import datetime
import os
import re

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
waiting_queue = []

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

def login(user_role):
    attempts = 3
    while attempts > 0:
        print(f"{user_role.capitalize()} Login")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        if username == users[user_role]["username"] and password == users[user_role]["password"]:
            return True
        else:
            print("Invalid username or password. Please try again.")
            attempts -= 1
    print("Maximum login attempts reached. Exiting program.")
    return False

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

def register_drug_category():
    category = input("Enter new drug category: ")
    drugs[category] = []
    print(f"New drug category '{category}' registered.")
    save_data()

def register_drug():
    global drug_id_counter
    drug_id = drug_id_counter
    drug_id_counter += 1
    drug = {
        "id": drug_id,
        "name": input("Drug Name: "),
        "category": input("Category (general drug, vaccine, poisonous, psychotropic, others): "),
        "quantity": int(input("Quantity: ")),
        "supplier": input("Supplier: "),
        "cost_per_unit": float(input("Cost per unit: ")),
        "expiry_date": input("Expiry date (YYYY-MM-DD): ")
    }
    if drug["category"] not in drugs:
        drugs[drug["category"]] = []
    drugs[drug["category"]].append(drug)
    print(f"Drug {drug['name']} registered with ID {drug_id}.")
    save_data()

def update_drug_quantity(drug_id, quantity):
    for category in drugs:
        for drug in drugs[category]:
            if drug["id"] == drug_id:
                drug["quantity"] = quantity
                print(f"Drug ID {drug_id} quantity updated to {quantity}.")
                save_data()
                return
    print(f"Drug ID {drug_id} not found.")

def update_drug_cost(drug_id, cost):
    for category in drugs:
        for drug in drugs[category]:
            if drug["id"] == drug_id:
                drug["cost_per_unit"] = cost
                print(f"Drug ID {drug_id} cost updated to {cost}.")
                save_data()
                return
    print(f"Drug ID {drug_id} not found.")

def delete_drug(drug_id):
    for category in drugs:
        for drug in drugs[category]:
            if drug["id"] == drug_id:
                drugs[category].remove(drug)
                print(f"Drug ID {drug_id} deleted.")
                save_data()
                return
    print(f"Drug ID {drug_id} not found.")

def receptionist_menu():
    while True:
        print("\nReceptionist Menu:")
        print("1. Register Patient")
        print("2. Register Family Member")
        print("3. Add Medication History")
        print("4. Search Patient")
        print("5. View Drugs Prescription")
        print("6. Add Medical Result")
        print("7. Add Medical Certificate")
        print("8. View Medical Certificates")
        print("9. View Patient")
        print("10. Delete Patient")
        print("11. Update Patient Status")
        print("12. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_patient()
        elif choice == "2":
            patient_id = int(input("Enter Patient ID: "))
            register_family_member(patient_id)
        elif choice == "3":
            patient_id = int(input("Enter Patient ID: "))
            add_medication_history(patient_id)
        elif choice == "4":
            patient_id = int(input("Enter Patient ID: "))
            search_patient(patient_id)
        elif choice == "5":
            patient_id = int(input("Enter Patient ID: "))
            view_drugs_prescription(patient_id)
        elif choice == "6":
            patient_id = int(input("Enter Patient ID: "))
            add_medical_result(patient_id)
        elif choice == "7":
            patient_id = int(input("Enter Patient ID: "))
            add_medical_certificate(patient_id)
        elif choice == "8":
            patient_id = int(input("Enter Patient ID: "))
            view_medical_certificates(patient_id)
        elif choice == "9":
            patient_id = int(input("Enter Patient ID: "))
            view_patient(patient_id)
        elif choice == "10":
            patient_id = int(input("Enter Patient ID: "))
            delete_patient(patient_id)
        elif choice == "11":
            patient_id = int(input("Enter Patient ID: "))
            status = input("Enter new status: ")
            update_patient_status(patient_id, status)
        elif choice == "12":
            break
        else:
            print("Invalid choice. Please try again.")

def doctor_menu():
    while True:
        print("\nDoctor Menu:")
        print("1. Search Patient")
        print("2. Add Medical Result")
        print("3. Add Medical Certificate")
        print("4. View Medical Certificates")
        print("5. View Patient")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = int(input("Enter Patient ID: "))
            search_patient(patient_id)
        elif choice == "2":
            patient_id = int(input("Enter Patient ID: "))
            add_medical_result(patient_id)
        elif choice == "3":
            patient_id = int(input("Enter Patient ID: "))
            add_medical_certificate(patient_id)
        elif choice == "4":
            patient_id = int(input("Enter Patient ID: "))
            view_medical_certificates(patient_id)
        elif choice == "5":
            patient_id = int(input("Enter Patient ID: "))
            view_patient(patient_id)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def pharmacist_menu():
    while True:
        print("\nPharmacist Menu:")
        print("1. Register Drug Category")
        print("2. Register Drug")
        print("3. Update Drug Quantity")
        print("4. Update Drug Cost")
        print("5. Delete Drug")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_drug_category()
        elif choice == "2":
            register_drug()
        elif choice == "3":
            drug_id = int(input("Enter Drug ID: "))
            quantity = int(input("Enter new quantity: "))
            update_drug_quantity(drug_id, quantity)
        elif choice == "4":
            drug_id = int(input("Enter Drug ID: "))
            cost = float(input("Enter new cost: "))
            update_drug_cost(drug_id, cost)
        elif choice == "5":
            drug_id = int(input("Enter Drug ID: "))
            delete_drug(drug_id)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def cashier_menu():
    print("Cashier functionality not implemented yet.")

def main():
    load_data()
    
    print("Welcome to the Hospital Management System")
    print("Please select your role:")
    print("1. Receptionist")
    print("2. Doctor")
    print("3. Pharmacist")
    print("4. Cashier")
    
    role = input("Enter your role: ")
    if role == "1" and login("receptionist"):
        receptionist_menu()
    elif role == "2" and login("doctor"):
        doctor_menu()
    elif role == "3" and login("pharmacist"):
        pharmacist_menu()
    elif role == "4" and login("cashier"):
        cashier_menu()
    else:
        print("Invalid role or login failed.")

if __name__ == "__main__":
    main()
