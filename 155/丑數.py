import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        na,nb,nc=1,1,1
        for i in range(n):
            m=min(a*na,b*nb,c*nc)
            if m==a*na:
                na+=1
            if m==b*nb:
                nb+=1
            if m==c*nc:
                nc+=1
        return m
print(Solution().nthUglyNumber(n = 5, a = 2, b = 11, c = 13))
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        n0=[a,b,c]
        n0.sort()
        a,b,c=n0[0],n0[1],n0[2]
        n1=n*a
        b0=n1//b
        c0=n1//c
        d0=n1//((b0*c0)//math.gcd(b0,c0))
        n1=a*(n-b0-c0+d0)
        return max(n1,b0*b,c0*c)
print(Solution().nthUglyNumber(n = 1000000000, a = 2, b = 217983653, c = 336916467))