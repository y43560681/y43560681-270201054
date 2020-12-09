password = input("Please enter your password :")

while True:
    if len(password) < 8:
        print("ERROR!")
        break
    elif password.lower() == password:
        print("ERROR!")
        break
    elif password.upper() == password:
        print("ERROR!")
        break
    elif "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
        print("SUCCESSFUL!")
        break
    else:
        print("ERROR!")
        break