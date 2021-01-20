def binary_to_dec(num):
    a = 0
    n = 0
    c = 0
    num = str(num)
    num = num[::-1]
    for i in num:
        c = int(int(i) * int(2**n))
        n += 1
        a += c
    return a



def dec_to_binary(num):
    a = 0
    i = 0
    n = 0
    while (num > 0):
        n = int((num % 2) * 10**i)
        i += 1
        num = num // 2
        a = a + n
    return a


def main():
    print("Binary to decimal = 1")
    print("Decimal to binary = 2")
    action = input("Which action do you want to do? ")
    num = int(input("Please enter a number: "))
    if action == "1":
        print(binary_to_dec(num))
    if action == "2":
        print(dec_to_binary(num))


main()