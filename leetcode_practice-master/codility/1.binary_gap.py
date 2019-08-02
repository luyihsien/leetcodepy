def solution(N):
    # write your code in Python 3.6
    # 使用format將int轉成binary string，接著過濾0與使用1切割轉成list，再利用len與max求出該list最大長度。
    return len(max(format(N,'b').strip('0').split('1')))

N = 1041
print(solution(N))
a=format(1041,'b')
b=a.strip('0')
print(b)
print(b.split('1',1))#從前到後，遇到切一次就出來#切了直接不見#str->list
c=b.split('1')
d=[len(i) for i in c]
print(d)#遇到1全切


