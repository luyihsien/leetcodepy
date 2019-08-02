class Solution:
    def tribonacci(self, n: int) -> int:
        n0=0
        n1=1
        n2=1
        if n==0:
            return n0
        if n==1 or n==2:
            return n1
        else:
            for i in range(3,n+1):
                n2,n1,n0=n1+n2+n0,n2,n1
            return n2
print(Solution().tribonacci(4))