# maximum sum subarray

def maxSum(nums):
    sum1=0
    maxi=nums[0]
    for i in nums:
        sum1+=i
        maxi=max(maxi,sum1)
        if sum1<0:
            sum1=0
    return maxi

nums=list(map(int,input().split()))
print(maxSum(nums))