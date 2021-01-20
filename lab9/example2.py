list = []
reversed_list = []


def get_reversed(list, k=0):
    if k == len(list):
        return
    else:
        reversed_list.append(list[k])
    return get_reversed(list, k + 1)


print("To finish press 'f' ")
while True:
    num = input("Please enter a number : ")
    if num == "f":
        break
    else:
        list.append(num)


print("Your list : ", list)
list = list[::-1]
get_reversed(list)
print(reversed_list)