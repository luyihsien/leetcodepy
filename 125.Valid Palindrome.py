a='SET'
b=a.lower()
print(b)
class Solution:
    def isPalindrome(self, s):
        s=s.lower()
        s= filter(str.isalnum,s)
        s=''.join(list(s))
        new_s=''.join(reversed(s))#reverese string
        if new_s==s:
            return True
        else:
            return False