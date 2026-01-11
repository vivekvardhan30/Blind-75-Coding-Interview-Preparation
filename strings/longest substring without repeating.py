#longest substring without repeating 

def longest_substring(s):
    st=set()
    left=0
    maxi=0
    for right in range(len(s)):
        while s[right] in st:
            st.remove(s[left])
            left+=1
        st.add(s[right])
        maxi=max(maxi,right-left+1)
    return maxi

s=input()
print(longest_substring(s))