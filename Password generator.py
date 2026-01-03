import random
import json
while True:
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{};:',.<>?/`~"
    option = ""
    json_pass = []
    cycle = 0

    option = input("\nOptions:\n 1. Create new password \n 2. Load new password \n --->  ")
    allcharacters = ""
    passwordlength = int(input("\nEnter the desired password length: "))
    passwordtype = input("Select the password type: \n 1. Random \n 2. Custom \n ---> " )
    if option == "1":
        if passwordtype == "1":
            allcharacters = lowercase + uppercase + numbers + symbols

        elif passwordtype == "2":

            up = input("Should the password contain uppercase letters?: ")

            if up.title() == "Yes":
                allcharacters+= uppercase
            elif up.title() == "No":
                uppercase = ""
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

            low = input("Should the password contain lowercase letters?: "  )
            if low.title() == "Yes":
                allcharacters += lowercase
            elif low.title() == "No":
                lowercase = ""
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

            num =input("Should the password contain numbers?: "  )
            if num.title() == "Yes":
                allcharacters += numbers
            elif num.title() == "No":
                numbers = ""
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

        while True:
            if passwordlength >= 5:
                password = "".join(random.sample(allcharacters, passwordlength))
                print("Generated password:", password)
                
            save = int(input("Do you wish to save the passowrd? \n 1. Yes  \n 2. No \n --->"))
            if save == "1":
                json_pass.append(password)
                
            elif passwordlength < 5:
                print("Your passowrd should have a minimum length of 8 characters.")
                cycle += 1
            break
   
    elif option == "2":

        break
