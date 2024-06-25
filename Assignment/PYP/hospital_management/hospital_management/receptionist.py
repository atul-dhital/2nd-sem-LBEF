# receptionist.py
from .patient import (
    register_patient, register_family_member, add_medication_history,
    search_patient, view_drugs_prescription, add_medical_result,
    add_medical_certificate, view_medical_certificates, view_patient,
    delete_patient, update_patient_status
)

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
