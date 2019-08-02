#時複 O(n) 空複 O(1)
def fac(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a
#時複O(n)空複O(n)
def fac(n):#我能變的花招就是1.參數n可用在外部2.與減少內部參數而代入的fac函數ex:fac(n-1),fac(n//2)其中是用前面定義的東西去串起來解題策略3.參數順序變化(參Hanoi.py)
    if n==0 or n==1:
        return 1
    elif n>1:
        return n*fac(n-1)
print(fac(-1))#None
