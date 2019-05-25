'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    9+1怎麼辦??
'''
'''
a=''.join(list(map(str,[1,2,3])))
print(a)
print(type(a))
b=int(a)
print(b)
print(type(b))
c=123
for i in len(c):#錯誤，int is not iterable
'''
class Solution:
    def plusOne(self, digits):
        a="".join(list(map(str,digits)))#a="".join(digits)#TypeError: sequence item 0: expected str instance, int found
        b=int(a)
        c=b+1
        c=str(c)
        d=[]
        for i in range(len(c)):#for i in len(c)#TypeError: 'int' object is not iterable
            d.append(c[i])#d=d.append#AttributeError: 'NoneType' object has no attribute 'append'
        return list(map(int,d))
a=[1,2,3]
a=a.append(4)
print(a)#None