from cryptography.fernet import Fernet
from icecream import ic
import json

"""
One time generation of key
"""
"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
"""

def load_key():
    with open("key.key", "rb") as f:
        key = f.read()
        return key

key = load_key()
fer = Fernet(key)
user_no = 0
db = dict()

def view():
    with open("password.json", "r") as f:
        data = json.load(f)
        ic(data)
        for user, user_data in data.items():
            user_name, pwd = user_data["username"], user_data["pwd"]
            print(f"Username : {user_name} | Password : {fer.decrypt(eval(pwd.encode())).decode()}")

def add():
    user_name = input("Enter the username :")
    pwd = input("Enter the password: ")
    global user_no 
    user_no += 1

    try:
        with open("password.json", "r") as f:
            data = json.load(f)
    except:
        data = {}

    ic(data)
    
    data.update({f"User {user_no}": {"username": user_name,
                                     "pwd": str(fer.encrypt(pwd.encode()))}})

    with open("password.json", "w") as f:
        json.dump(data, f, indent=4)


while True:
    print("Would you like to add a password or view existing ones? Press 'q' to exit\n")

    choices = {"1": "Add a password",
               "2": "View existing ones"}

    for key, value in choices.items():
        print(f"{key}. {value}")

    # Convert user input to lowercase
    user_choice = input("\nCHOICE: ").lower()

    if user_choice == "q":
        break
    elif user_choice == "1":
        add()
    elif user_choice == "2":
        view()
    else:
        print("Invalid choice")
        

