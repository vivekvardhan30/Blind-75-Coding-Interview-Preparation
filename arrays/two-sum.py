def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        comp = target - x
        if comp in seen:
            return [seen[comp], i]
        seen[x] = i
    return -1


nums = list(map(int,input().split()))
target = int(input())

print(two_sum(nums, target))
