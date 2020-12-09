dict1 = {}
names = []
salary = []
salary1 = []

for i in range(5):
    n = input("Please enter a name :")
    s = input("Please enter the salary of the person you entered : ")
    dict1[s] = n
    names.append(n)
    salary.append(s)

salary.sort()
salary.reverse()
salary1.append(salary[0])
salary1.append(salary[1])
salary1.append(salary[2])

for i in salary1:
    print(dict1[i])