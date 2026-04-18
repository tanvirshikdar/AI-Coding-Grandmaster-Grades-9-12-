a=1
b=0
c=0

aANDb = a & b
bXORc = b ^ c
bORc = b | c
g = bXORc & bORc

final = aANDb ^ g

print("q = ",final)