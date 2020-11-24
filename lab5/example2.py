x = int(input("How many numbers will you enter? "))

even = 0
odd = 0

for i in range(1, x+1):

  a = int(input("Enter a number ="))

  if a % 2 == 0:

    even += 1

  elif a % 2 == 1:

    odd += 1


print((even / (even + odd)) * 100)