def solution(N):
    # write your code in Python 3.6
    c = ''
    while N > 0:
        a, b = N // 2, N % 2
        print('a',a,'b',b)
        c += str(b)
        N = a
    c=c[::-1]
    print(c)
#solution(6)與solution(3)值都11
'''
a 1 b 1
a 0 b 1
11
a 3 b 0
a 1 b 1
a 0 b 1
11
'''
