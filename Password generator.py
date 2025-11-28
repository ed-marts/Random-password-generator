import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

allcharacters = lowercase + uppercase + numbers + symbols
passwordlength = int(input("Enter the desired password length: "))
if passwordlength < 8:
    password = "".join(random.sample(allcharacters, passwordlength))
    print("Generated password:", password)

elif passwordlength > 8:
    print("Your passowrd should have a maximium length of 8 characters.")
