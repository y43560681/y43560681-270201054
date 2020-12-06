num = int(input("Please enter a number : "))
n = ["0"]
m = num * n
a = []
b = ''
for i in range(num):
  m[i] = "1"
  a.append(m)
  m = num * n
for i in a:
  for ii in i:
    b += ii
  if len(i) == num:
      print(b)
      b = ''
      



      
      
      
    





