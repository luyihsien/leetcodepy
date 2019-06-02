#https://extenshu.com/2017/09/24/python%E5%88%9D%E5%AD%B8%E9%87%8D%E9%BB%9E-05-global%E8%AE%8A%E6%95%B8/
#1.global()用法
def test():
    global var1
    var1=10


var1 = 5
test()
print(var1)
a=[1,2,4,7]
left,right=0,len(a)-1
mid=(left+right)//2
print(a[:mid])
def binary_search(seq, value):
    if len(seq) == 0:
        return False
    else:
        mid = len(seq) // 2
        if value == seq[mid]:
            return True
        elif value < seq[mid]:
            return binary_search(seq[:mid], value)
        elif value > seq[mid]:
            return binary_search(seq[mid + 1:], value)
print(binary_search([1,2,4,7],1))
a=[]
print(a[:-2])#[]
#print(a[-2])#IndexError: list index out of range
def a():
    b=2
    print(b)
a()
z=1
def demo2(a):
    #global z
    #z=z+a
    print(z)
demo2(2)