class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        c=0
        for i in range(2,n):
            print('i',i)
            for j in range(2,i):
                print('j',j)
                if i%j==0:
                    c-=1
                    break
            c+=1
            print(c)
        return c
print(Solution().numPrimeArrangements(100))
