def demo(f):
    def f_new(x):
        print(f.__name__)
        return f(x)
    return f_new
@demo
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
    def f_new(*args,**kwargs):#傳遞可隨意伸縮參數，並在return呼叫f函數，共用同樣參數
        print(f.__name__)
        return f(*args,**kwargs)
    return f_new
@demo
def test3(x,y):
    return (x,y)
print(test3(1,2))#test3 return (1,2)