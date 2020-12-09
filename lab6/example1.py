email = input("Please enter the email: ")
email_check = "ceng113@example.com"

email0 = email.split("@")
email0[0] = email0[0].replace(".","")

email1 = email0[1].split(".")
email2= email1[0].lower()
email3 = email0[0].lower()
email4 = email3 + "@" + email2 + "." + email1[1]

if email_check == email4:
  print("True")
elif email_check != email4:
  print("False")
