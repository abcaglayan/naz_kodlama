def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
def printPrimes(num):
    for i in range(2, num+1):
        if isPrime(i):
            print(i)

printPrimes(10)