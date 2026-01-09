# counting bits

def counting_bits(n):
    ans=[]
    for i in range(n+1):
        st=str(bin(i)[2:])
        ans.append(st.count('1'))
    return ans

n=int(input())
print(counting_bits(n))