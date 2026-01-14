# group anagram
from collections import defaultdict
def group_anagrams(strs):
    mpp=defaultdict(list)
    for s in strs:
        key=''.join(sorted(s))
        mpp[key].append(s)
    return list(mpp.values())

n=int(input("Enter number of strings: "))
strs=[]
for _ in range(n):
    strs.append(input())
print(group_anagrams(strs))