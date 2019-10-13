a='123'
a=a.replace('1','4')
print(a)
a = frozenset(range(10))
print(a)
#http://www.runoob.com/python/python-func-frozenset.html
print(type({1:1,2:4,3:3}.keys()))
a={1:1,2:4,3:3}.values()
for i in a:
    print(i)
a='0110000100000'
a=a.strip('0')
print(a)
a=10
a=format(a,'b')
print(a)
a=[2,4,6,8]
b=[1,3,5,7]
d=[5,5,5,5]
c=list(map(lambda x,y,z:x-y+z,a,b,d))

print(c)
e=filter(lambda x: x>6,a)
print(e)