'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
'''
a=123
print(len(a))#TypeError: object of type 'int' has no len()


class Solution:
    def addBinary(self, a, b):
        c = 0
        for i in range(len(a), 0, -1):
            if a[i] == '1':
                c += 2 ** (int(i))
        for i in range(len(b), 0, -1):
            if b[i] == '1':
                c += 2 ** (int(i))
        if c == 0:
            return 0
        if c == 1:
            return 1
        while c != 0:
