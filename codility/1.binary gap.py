def solution(N):
    # write your code in Python 3.6
    c = ''
    while N > 0:
        a, b = N // 2, N % 2
        c += str(b)
        N = a
    c = int(c)
    print(c)
#solution(6)與solution(3)值都11