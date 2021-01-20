t = input("Please enter second : ")


def sleep(t, k = t):
    k = int(k)
    if k == -1:
        return
    else:
        print(k)
    return sleep(t, k - 1)


sleep(t)