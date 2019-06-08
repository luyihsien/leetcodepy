def solution(N):
    c=''
    d={}
    e=[]
    while N>0:
        a,b=N//2,N%2
        c+=str(b)
        N=a
    c=c[::-1]
    print(c)
    for i in range(len(c)):
        if c[i]=='1':
            d[i]=1
    if not d:
        return 0
    else:
        g=[]
        for i in d.keys():
            e.append(i)
        print(e)
        for j in range(1,len(e)):
            f=e[j]-e[j-1]
            g.append(f)
        if not g:
            return 0
        return max(g)-1
print(solution(15))
'''
a 1 b 1
a 0 b 1
11
a 3 b 0
a 1 b 1
a 0 b 1
11
'''
