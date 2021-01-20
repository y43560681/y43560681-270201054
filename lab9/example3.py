list = []
evens_list = []

def get_evens(list, k=0):
    if k == len(list)-1:
        return
    else:
        if int(list[k]) % 2 == 0:
            evens_list.append(list[k])
    return get_evens(list, k + 1)



print("To finish press 'f' ")
while True:
    num = input("Please enter a number : ")
    if num == "f":
        break
    else:
        list.append(num)

get_evens(list)
print("Even list = ", evens_list)