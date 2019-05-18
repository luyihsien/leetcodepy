#http://www.runoob.com/python/att-list-append.html
def fib1(n):
    if n==0 or n==1:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)
'''
a=[]
a[0]=1#IndexError: list assignment index out of range
'''

'''
def fib2(n):
    #a=[1,1]#等同a=[] a[0]=1 a[1]=1?#錯 IndexError: list assignment index out of range
    
    for i in range(n):
        if n==0 or n==1:
            return 1
        else:
            a[n]=a[n-1]+a[n-2]
    return a[n]
#fib2(4)#IndexError: list index out of range
'''

'''
def fib2(n):
        if n == 0 or n == 1:
            return 1
        else:
            a=[]
            for i in range(n):
                if i==0 or i==1:
                    a.append(1)
                else:
                    a.append(a[n-1]+a[n-2])
        return a[n]
fib2(4)
#IndexError: list index out of range
'''


def fib2(n):
    if n == 0 or n == 1:
        return 1
    else:
        a = []
        for i in range(n):
            if i == 0 or i == 1:
                a.append(1)
            else:
                a.append(a[i - 1] + a[i - 2])
    return a[n-1]#a[i]#a[n]不對


print(fib2(7))