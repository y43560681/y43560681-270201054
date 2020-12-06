num = int(input("Please enter number :"))

num = str(num)
num1 = []
result = 0


for i in num:
  num1.append(i)


if len(num1) == 1:
  result = num1[0]

elif len(num1) > 1:
  result = int(num1[len(num1)-1]) + int(num1[len(num1)-2])

result = str(result)

if len(result) < 2:
  print("0"+result)
else:
  print(result)




