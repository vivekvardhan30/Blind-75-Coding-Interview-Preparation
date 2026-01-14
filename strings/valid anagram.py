# valid anagram

def is_anagram(s,t):
    return sorted(s) == sorted(t)

s=input("Enter first string: ")
t=input("Enter second string: ")
print(is_anagram(s,t))
