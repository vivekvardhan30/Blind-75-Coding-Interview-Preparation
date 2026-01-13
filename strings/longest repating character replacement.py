# longest repeating character replacement

from collections import defaultdict

def longest_repeating_character_replacement(s, k):
    freq=defaultdict(int)
    left=0
    maxi=0
    cnt=0
    max_len=0
    for right in range(len(s)):
        freq[s[right]]+=1
        maxi=max(maxi,freq[s[right]])
        cnt=(right-left+1)-maxi
        if(cnt>k):
            freq[s[left]]-=1
            left+=1
        max_len=max(max_len,right-left+1)
    
    return max_len

s=input()
k=int(input())
print(longest_repeating_character_replacement(s, k))