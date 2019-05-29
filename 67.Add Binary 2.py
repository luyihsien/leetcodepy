class Solution:
    def addBinary(self, a, b):
        carry, val = 0, 0
        for i in range(max(len(a), len(b))):
            carry = val
            if i < len(a):
                val += int(a[-1])
            if i < len(b):
                val += int(b[-1])
            carry, val = val // 2, val % 2
        if carry:
            val += str(1)
        return val[::-1]


#二刷0529
class Solution:
    def addBinary(self, a, b):
        carry, val, st = 0, 0, ''
        for i in range(max(len(a), len(b))):
            carry = val
            if i < len(a):
                val += int(a[-1])
            if i < len(b):
                val += int(b[-1])
            carry, val = val // 2, val % 2
            c = str(val)
            st += c
        if carry:
            st += str(1)
        return st[::-1]
#二刷0529
class Solution:
    def addBinary(self, a, b):
        carry,val,st=0,0,''
        for i in range(max(len(a),len(b))):
            val=carry
            if i<len(a):
                val+=int(a[-1])
            if i<len(b):
                val+=int(b[-1])
            carry,val=val//2,val%2
            c=str(val)
            st+=c
        if carry:
            st+=str(1)
        return st[::-1]

