number = int(input("How many fibonacci numbers do you want to generate? "))

a = 1
b = 1

print(a)

print(b)

for i in range(number - 2):
  
  c = a+b
  a = b
  b = c
  
  print(c)
