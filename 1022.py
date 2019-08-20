'''
def a(acc):
    if acc>=20:
        acc=acc+1
    a(acc)
    a(acc)
print(a(1))#不會停止
#RecursionError: maximum recursion depth exceeded while calling a Python object
'''
def a(x):
    x=x+1
    if x==5:
        return
    print(x)
    a(x)
    a(x)
a(1)



