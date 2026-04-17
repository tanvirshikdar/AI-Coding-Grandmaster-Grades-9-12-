a = 3000

for num in range(1, a + 1):
    c = 0
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1
            
    if c == 2:
        rev = 0
        temp = num
        while temp > 0:
            rev = rev * 10 + (temp % 10)
            temp //= 10
            
        if rev == num:
            print(num)