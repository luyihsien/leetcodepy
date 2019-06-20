def test1(x):
    return x*2
def test2(x):
    return x*x*x
test1(1)
test2(2)
def demo(f):#f為一未呼叫函式
    def f_new(x):#f_new與f 同參數x
        print(f.__name__)
        return f(x)
    return f_new#可被return看作tmp的function#可看作訂在func內的變數
f=demo(test1)
f(2)#test1
#print(f(2))
f=demo(test2)
#print(f(2))
@demo
def test3(x):
    return x*2*x
a=test3(4)#比起原本的test3多增加了印函數型態名字的功能
print(a)
