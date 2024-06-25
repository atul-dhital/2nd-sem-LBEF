# drug.py
from .data import drugs, drug_id_counter, save_data

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
