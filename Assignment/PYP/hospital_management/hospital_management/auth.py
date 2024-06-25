# auth.py
import getpass
from .data import users

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
