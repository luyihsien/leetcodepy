#print('abcabc'/'abc')#TypeError: unsupported operand type(s) for /: 'str' and 'str'
class Solution:
    def isValid(self, S: str) -> bool:
        while 'abc' in S:
            S=S.replace('abc','')
        if S is '':
            return True
        return False
print(Solution().isValid("cababc"))