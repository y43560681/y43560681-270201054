age = int(input("Please enter your age :"))

ticket = 3
discount_ticket = str((ticket * 50)/100)

if age < 6 or age > 60:
  print("Free !")
elif age >= 6 and age <= 18:
  
  print(discount_ticket + " TL")
else:
  print("3 TL")


