def fun1(n):
    return n * (n + 1) / 2

def fun2(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

def fun3(n):
    total_sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            total_sum += 1
    return total_sum

input_val = 4

print(f"Results for input n = {input_val}:")
print(f"Fun1 Result: {fun1(input_val)}")
print(f"Fun2 Result: {fun2(input_val)}")
print(f"Fun3 Result: {fun3(input_val)}")