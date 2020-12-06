num = int(input("How many you enter the number of students ? :"))

scores = []
scores1 = []
scores2 = []

for i in range(num):
  print("Student" + str(i+1))
  midterm1 = int(input("Please enter the midterm1 score? :"))
  midterm2 = int(input("Please enter the midterm2 score ? :"))
  final = int(input("Please enter the final exam score ? :"))

  n = midterm1 * (3/10) + midterm2 * (3/10) + final * (4/10)
  if n > 90:
    scores1.append(n)
  else:
    scores.append(n)


scores2.append(scores)
scores2.append(scores1)

print(scores2)