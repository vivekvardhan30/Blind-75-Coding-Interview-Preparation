# maximum product subarray

def max_prod_subarray(nums):
    prod=1
    maxi=float('-inf')
    for i in nums:
        prod*=i
        maxi=max(maxi,prod)
        if prod==0:
            prod=1
    prod=1
    for i in range(len(nums)-1,-1,-1):
        prod*=i
        maxi=max(maxi,prod)
        if prod==0:
            prod=1
    return maxi

nums=list(map(int,input().split()))
print(max_prod_subarray(nums))