# sum of integer using bit manipulation

def sum_of_integer(a,b):
    mask=0xFFFFFFFF
    while b:
        a,b=(a^b)&mask,((a&b)<<1)&mask
    return a if a<=0x7FFFFFFF else ~(a^mask)

a=int(input())
b=int(input())
print(sum_of_integer(a,b))