# doctor.py
from .patient import (
    search_patient, add_medical_result, add_medical_certificate,
    view_medical_certificates, view_patient
)

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
