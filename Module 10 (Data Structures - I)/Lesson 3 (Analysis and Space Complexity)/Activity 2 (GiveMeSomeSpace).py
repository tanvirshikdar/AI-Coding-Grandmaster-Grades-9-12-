def sum_n(n):
    return n * (n + 1) // 2

print("Sum of first n numbers (n=5):", sum_n(5))

def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total

a = [12, 3, 4, 15]
print("Array sum:", array_sum(a))

def summ(n):
    if n <= 0:
        return 0
    return n + summ(n - 1)

print("Recursive sum (n=5):", summ(5))

def sum_n(n):
    return n * (n + 1) // 2

print("Sum of first n numbers (n=5):", sum_n(5))

def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total

a = [12, 3, 4, 15]
print("Array sum:", array_sum(a))

def summ(n):
    if n <= 0:
        return 0
    return n + summ(n - 1)

print("Recursive sum (n=5):", summ(5))