a = int(input("Enter the value 'a' : "))
b = int(input("Enter the value 'b' : "))
c = int(input("Enter the value 'c' : "))

Δ = b**2 - 4*a*c

if Δ < 0:
  print('There are two complex roots')

elif Δ == 0 :
  print('There is one real root')

else:
 print('There are two real roots')