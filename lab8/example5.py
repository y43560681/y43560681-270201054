def password_check(password):
    n = [False, False, False]
    if len(password) > 8 or " " in password:
        if password.isnumeric() or password.isalpha():
            print("Level 1")
        else:
            for i in password:
                if i.isnumeric():
                    n[0] = True
                elif i.isalpha():
                    n[1] = True
                else:
                    n[2] = True
            if n[0] and n[1] and n[2]:
                print("Level 3")
            elif n[0] and n[1]:
                print("Level 2")
    else:
        print("Level 0")



def main():
    password = input("Please enter a password: ")
    password_check(password)

main()