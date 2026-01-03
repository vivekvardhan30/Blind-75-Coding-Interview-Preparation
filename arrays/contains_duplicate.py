# contains duplicate 

# approach 1: using the hashmap function(dictionary)

def contains_duplicate(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    for first,second in freq.items():
        if second>=2:
            return True
    return False



# approach 2: using set

def contains_duplicate(nums):
    st=set()
    for i in nums:
        st.add(i)
    return len(st)==len(nums)


nums=list(map(int,input().split()))
print(contains_duplicate(nums))