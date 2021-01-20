a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]

def sum(list):
    a = 0
    for i in list:
        a += i
    return a**2

print(sum(a_list))