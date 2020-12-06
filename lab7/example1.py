n = int(input("How many names and ages will you enter? "))

name_store = []
age_store = []
a = ''



for i in range(n):
  name = input("Please enter a name : ")
  age = input("Please enter a age : ")
  if int(age) > 18:
    name_store.append(name)

for i in name_store:
  print(i)