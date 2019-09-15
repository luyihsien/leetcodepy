
def a(x,l=[]):
    x=x+1
    l.append(x)
    print('l', l, 'id', id(l))
    print(x)
    if x==4:

        return x
        #return x

    #return x
    return a(x)+a(x)
print(a(1))
'''
2
3
4
[4]
4
[4, 4]
3
4
[4, 4, 4]
4
[4, 4, 4, 4]
16
'''

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