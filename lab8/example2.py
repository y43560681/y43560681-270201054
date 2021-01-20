num11, num22 = [], []


def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if (num % i == 0):
                return False
        return True
            
            
def print_primes_between(num1, num2):
    a = []
    for i in range(2, num1):
        if (num1 % i == 0):
            num11.append(i)
    for i in range(2, num2):
        if (num2 % i == 0):
             num22.append(i)
    for i in num11:
        if i in num22:
            a.append(i)
    if a != []:
        print(a)
    else:
        print("not prime among them")
            
         
        
def main():
    num1 = int(input("Please enter the num1: "))
    num2 = int(input("Please enter the num2: "))
    if is_prime(num1):
        print("num 1 is prime")
    else:
        print("num 1 is not prime ")
    if is_prime(num2):
        print("num 2 is prime")
    else:
        print("num 2 is not prime")
    print_primes_between(num1, num2)
    

    

main()


