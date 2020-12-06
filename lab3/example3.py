gpa = float(input("Enter your gpa :"))
numOfLec = int(input("Enter your number of lecture :"))

if gpa<2.0:
  if numOfLec < 47:
    print('Not enough number of lectures and GPA!')
  else:
    print('Not enough GPA!')
else:
  if numOfLec < 47:
    print('Not enough number of lectures')
  else:
    print('GRADUATED!!!')