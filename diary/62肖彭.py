def demo(f):
    def f_new(x):#f_new(y):傳的參數沒有
        print(f.__name__)
        return f(x)
    return f_new
@demo#讓test3=demo(test3)
def test3(x):
    return x*2*x
print(test3(1))#test3 return 2
'''
@demo
def test3(x,y):
    :return(x,y)
print(test3(1,2))#TypeError: f_new() takes 1 positional argument but 2 were given
故修正如下
'''
def demo(f):#傳入function f
    def f_new(*args,**kwargs):#傳遞可隨意伸縮參數，並在return呼叫f函數，定義共用同樣參數使用方式but未呼叫
        print(f.__name__)
        return f(*args,**kwargs)
    return f_new
@demo
def test3(x,y):
    return (x,y)
print(test3(1,2))#此刻才呼叫#test3 return (1,2)
def b(x,y,z):
    print(x,y,z)
def a(x,y,z):
    print(x,y)#可供內部呼叫
    return b(x,y,z)
a(1,2,3)
'''
1 2
1 2 3
'''
def a(*args):
    print(args)
    return b(*args)
a(1,2,3)