#離散數學p.4-18(1)
def f(n):#時間複雜度O(n) 空間複雜度O(n)
    if n==0:#與下方f(n-1)+2*n+1其實是互斥事件(要嘛=0要嘛!=0)不會既等於0又不等於0#我只擇一return不會兩個都return
        return 3
    return f(n-1)+2*n+1
print(f(5))#38