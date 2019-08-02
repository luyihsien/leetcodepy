def b():
    a.append('b')
    return a
a=[]
print(b())
print(a)
def c():
    b=a+1
    return b
a=1
print(c())
ops = ['+', '-', '*', '/', '']

def solve3():
    for i in range(100, 1000):
        s = str(i)
        for op1 in ops:
            for op2 in ops:
                exp = s[0] + op1 + s[1] + op2 + s[2]
                print('exp', exp)
                if len(exp) > len(s):
                    try:
                        print('s[::-1]',s[::-1])
                        if s[::-1] == str(eval(exp)):
                            ans.append(exp + '=' + s[::-1])
                            print('ans',ans)
                    except:
                        print(exp)
                        print('pass')
                        pass

ans = []
solve3()
print(ans)
