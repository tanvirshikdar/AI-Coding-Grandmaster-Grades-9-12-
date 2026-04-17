def primeSeive(n):
    prime = [True for i in range(n + 1)]
    currentNumber = 2
    while (currentNumber * currentNumber <= n):
        if (prime[currentNumber] == True):
            for i in range(currentNumber ** 2, n + 1, currentNumber):
                prime[i] = False
        currentNumber += 1

    prime[0]= False
    prime[1]= False

    for p in range(n + 1):
        if prime[p]:
            print(p)

n = 99
print("All 2 digit prime numbers: ")
primeSeive(n)