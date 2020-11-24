num1 = str(input("Enter a number1: "))
num2 = str(input("Enter a number2: "))

match = 0
digit = 0


num101 = num1[::-1]
num102 = num2[::-1]

while digit < len(num101) and digit < len(num102):
  
  
  if(num101[digit]) == (num102[digit]):
    
    match += 1
  
  digit += 1

print(match)
