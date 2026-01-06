import random
import json
import os

FILE_NAME = "passwords.json"

# Load or create JSON file
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
else:
    data = {"passwords": []}

while True:
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{};:',.<>?/`~"

    option = input("\nOptions:\n 1. Create new password \n 2. Load saved passwords \n 3. Exit \n ---> ")

    if option == "1":
        allcharacters = ""

        passwordlength = int(input("\nEnter the desired password length: "))
        passwordtype = input("Select the password type: \n 1. Random \n 2. Custom \n ---> ")

        if passwordlength < 5:
            print("Password must be at least 5 characters.")
            continue

        if passwordtype == "1":
            allcharacters = lowercase + uppercase + numbers + symbols

        elif passwordtype == "2":
            up = input("Include uppercase letters? (Yes/No): ")
            if up.title() == "Yes":
                allcharacters += uppercase

            low = input("Include lowercase letters? (Yes/No): ")
            if low.title() == "Yes":
                allcharacters += lowercase

            num = input("Include numbers? (Yes/No): ")
            if num.title() == "Yes":
                allcharacters += numbers

            sym = input("Include symbols? (Yes/No): ")
            if sym.title() == "Yes":
                allcharacters += symbols

        if allcharacters == "":
            print("You must select at least one character type.")
            continue

        password = "".join(random.sample(allcharacters, passwordlength))
        print("\nGenerated password:", password)

        save = input("\nDo you wish to save the password? (Yes/No): ")
        if save.title() == "Yes":
            data["passwords"].append(password)

            with open(FILE_NAME, "w") as file:
                json.dump(data, file, indent=4)

            print("Password saved successfully!")

    elif option == "2":
        if data["passwords"]:
            print("\nSaved passwords:")
            for i, p in enumerate(data["passwords"], start=1):
                print(f"{i}. {p}")
        else:
            print("No saved passwords found.")

    elif option == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
