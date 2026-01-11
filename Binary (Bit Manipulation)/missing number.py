# missing number using bit manipulation

def missing_num(nums):
    ans=0
    n=len(nums)
    for i in range(1,n+1):
        ans^=i
    
    for x in nums:
        ans^=x
    
    return ans

nums=list(map(int,input().split()))
print(missing_num(nums))