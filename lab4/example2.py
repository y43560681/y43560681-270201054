year = int(input("Please enter a year :"))

year4 = year%4
year400 = year%400

if year4 == 0 and year400 == 0:
  print("a leap year!")

else:
  print("not leap year!")
