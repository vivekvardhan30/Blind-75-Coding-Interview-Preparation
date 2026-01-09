# number of binary 1 in the given number 

def number_of_bits(n):
    b=bin(n)
    st=b[2:]
    cnt=0
    for i in st:
        if i=='1':
            cnt+=1
    return cnt

n=int(input())
print(number_of_bits(n))