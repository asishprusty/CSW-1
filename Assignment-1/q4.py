import string
def is_palindrome_for_loop(s):
    s = s.lower()  # ignore case
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True
def is_palindrome_two_pointer(s):
    s=s.lower() #ignore case
    s=s.replace(' ','') #remove space
    translator=s.maketrans('','',string.punctuation)
    s=s.translate(translator)
    left,right=0,len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
word=input("Enter a given string: ")
if is_palindrome_for_loop(word):
    print("For-loop Check: Palindrome",end=",")
if is_palindrome_two_pointer(word):
    print("Two-pointer Check: Palindrome")

