import random
while True:
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"



    allcharacters = ""
    passwordlength = int(input("\nEnter the desired password length: "))
    passwordtype = input("Select the password type: \n 1. Random \n 2. Custom \n ---> " )

    if passwordtype == "1":
        allcharacters = lowercase + uppercase + numbers + symbols

    elif passwordtype == "2":

        up = input("Should the password contain uppercase letters?: ")

        if up.title() == "Yes":
            uppercase += allcharacters
        elif up.title() == "No":
            uppercase = ""
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

        low = input("Should the password contain lowercase letters?: "  )
        if low.title() == "Yes":
            lowercase += allcharacters
        elif low.title() == "No":
            lowercase = ""
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

        num =input("Should the password contain numbers?: "  )
        if num.title() == "Yes":
            numbers += allcharacters
        elif num.title() == "No":
            numbers = ""
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    while True:
        if passwordlength >= 5:
            password = "".join(random.sample(allcharacters, passwordlength))
            print("Generated password:", password)

        elif passwordlength < 5:
            print("Your passowrd should have a minimum length of 8 characters.")
            cycle += 1
        break
