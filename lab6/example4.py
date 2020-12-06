n = int(input("How many you enter number ?:"))
list1 = []

for i in range(n):
  m = int(input("Please enter a number ?:"))
  list1.append(m)

list1 = set(list1)
list1 = list(list1)
list1 = list1[::-1]
print(list1)