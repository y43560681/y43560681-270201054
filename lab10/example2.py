store = []

def hailstone(n):
    if n == 1:
        return
    else:
        if n % 2 == 0:
            n = n//2
            store.append(n)
        else:
            n = (3*n) + 1
            store.append(n)
    return hailstone(n)




n = int(input("Please enter a number : "))
hailstone(n)
print(store)