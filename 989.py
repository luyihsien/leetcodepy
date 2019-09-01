a=int('1')
print(a)
a='1 2 3'
print(a.split())
print(min(i+3 for i in [4,5,6]))
a=[1,2,3,4]
for i in reversed([1,2,3]):
    print(i)
b=a[-1-2:-1]#[2,3]
print(b)
a=[map(str,a)]#不等於[map(str,a)]
print(a)
a=''.join(['1','2','3'])
print(a)
a=''.join(i for i in ('1','2','3','4'))
print(a)
print(i for i in ('1','2','3','4'))
print(sum([1,2]))