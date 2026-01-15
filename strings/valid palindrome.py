# valid palindrome

def is_palindrome(s):
    st=""
    for i in s:
        if i.isalnum():  
            st+=i.lower()
    
    if len(st)==0 or len(st)==1:
        return True
    left=0
    right=len(st)-1
    while left<right:
        if st[left]==st[right]:
            left+=1
            right-=1
        else:
            return False
    return True

s=input()
print(is_palindrome(s))