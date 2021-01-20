times = 0


def f(n, k=0):
    if k == 3:
        return
    else:
        global times
        times += int(n)
    return f(n, k + 1)


n = input("Please enter a number : ")
f(n)
print(times)
