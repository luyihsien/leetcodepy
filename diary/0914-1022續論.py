def a(x,l=[]):
    x=x+1
    print(x)
    if x==4:
        l.append(x)
        print(l)
        return x

    #return x
    return a(x)+a(x)
print(a(1))
'''
l=[]
def a(x):
    x=x+1
    l.append(x)
    if x==4:
        return
    a(x)
    a(x)
a(1)
print(l)
'''