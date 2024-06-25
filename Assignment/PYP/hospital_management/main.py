# main.py
from hospital_management.data import load_data
from hospital_management.auth import login
from hospital_management.receptionist import receptionist_menu
from hospital_management.doctor import doctor_menu
from hospital_management.pharmacist import pharmacist_menu
from hospital_management.cashier import cashier_menu

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
