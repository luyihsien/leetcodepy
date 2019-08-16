#997. Find the Town Judge
import collections
'''
c=collections.Counter()
c[1]+=2
print(c)
a=[1,2]
a=a[::-1]
print(a)
'''

class Solution:
    def findJudge(self, N: int, trust) -> int:
        a = []
        d = 0
        c = collections.Counter()
        for i in trust:
            c[i[1]] += 1
            print(c)
            if c[i[1]] == N - 1:
                if d == 0:
                    print('a',a)
                    a.extend(i)
                    print('a',a)
                    d += 1
                elif d > 0:
                    print('d',d)
                    return False
        print('a',a)
        if a == []:
            return False
        for i in trust:
            if a[1] == i[0]:
                return False
            return a[1]
print(Solution().findJudge(N = 2, trust = [[1,2]]))