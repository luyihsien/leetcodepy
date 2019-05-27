#https://blog.csdn.net/coder_orz/article/details/51706532
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
'''
'''
a=123
print(len(a))#TypeError: object of type 'int' has no len()
'''
'''
class Solution:
    def addBinary(self, a, b):
        c=0
        for i in range(len(a),0,-1):
            if a[i]=='1':
                c+=2**(int(i))
        for i in range(len(b),0,-1):
            if b[i]=='1':
                c+=2**(int(i))
        if c==0:
            return 0
        while c!=0:
            if c%2==1:
                c=c//2
                i=i+1
'''
a=7
a,b=a//2,a
print(a,b)

class Sol:
    def addBin(self,a,b):
        result,carry,val='',0,0
        for i in range(max(len(a),len(b))):
            val=carry
            if i<len(a):
                val+=int(a[-(i+1)])
                print(val,'加 a')
            if i<len(b):
                val+=int(b[-(i+1)])
                print(val,'加 b')
            carry,val=val//2,val%2
            result+=str(val)
            print(result)
        if carry:
            result+=str(1)
        print(result[::-1])
        return result[::-1]
Sol().addBin('101','11')