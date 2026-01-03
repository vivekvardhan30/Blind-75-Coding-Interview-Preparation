# product of array itself

def product_of_array_itself(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    result = [0] * n

    # Prefix product
    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    # Suffix product
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    # Result
    for i in range(n):
        result[i] = prefix[i] * suffix[i]

    return result


nums = list(map(int, input().split()))
print(product_of_array_itself(nums))
