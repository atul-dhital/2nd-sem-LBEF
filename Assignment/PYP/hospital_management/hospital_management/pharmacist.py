# pharmacist.py
from .drug import (
    register_drug_category, register_drug, update_drug_quantity,
    update_drug_cost, delete_drug
)

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
