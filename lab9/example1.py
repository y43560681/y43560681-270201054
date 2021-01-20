sum = 0


def harmonic(n, k=1):
    global sum
    if k == int(n):
        return
    else:
        sum += 1/int(k)
    return harmonic(n, k + 1)


n = input("How many terms do you want to enter? ")
harmonic(n)
print(sum)