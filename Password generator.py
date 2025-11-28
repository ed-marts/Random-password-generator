import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

allcharacters = ""
passwordlength = int(input("Enter the desired password length: "))
up = input("Should the password uppercase letters?: ")

if up.title() == "Yes":
    uppercase += allcharacters




num =input("Should the password contain numbers?: "  )

while True:
    if passwordlength >= 8:
        password = "".join(random.sample(allcharacters, passwordlength))
        print("Generated password:", password)

    elif passwordlength < 5:
        print("Your passowrd should have a minimum length of 8 characters.")

