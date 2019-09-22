#1
#Process finished with exit code 0
#return 扮演至關重大角色，使得算出來的值似直接子Q解慢慢一層層疊成原問題解
#Lintcode822#stack資料結構聯想此結果(後進先出)沒return vs 後進先出有return #大Q(先進)切成小Q(後進) 靠後進先出+return變成小聚成大Q
#聯想誤解
#def fib(i):
    #if i==0 or i==1:
    #    return 1
    #else:
        #fib(i-1)+fib(i-2)

#
'''
def fac(n):
    print('n',n)
    if n==1:
        return 1
    n*fac(n-1)#TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

fac(10)
'''
def fib(i):
    if i==0 or i==1:
        return 1
    fib(i-1)+fib(i-2)


print(fib(3))