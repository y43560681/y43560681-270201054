password = "12345"

check = input("Please enter the password:")

while check != password or check == "Help":

  if check == "Help":
    print(password[0])
 
  else: 
  
    print("Wrong")
  
  check = input("Please enter the password:")

 
print("Welcome")