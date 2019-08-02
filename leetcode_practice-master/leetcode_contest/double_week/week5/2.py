class Solution:
    def isArmstrong(self, N: int) -> bool:
        b=str(N)
        a=0
        for i in b:
            print('i',i)
            a+=(int(i))**3
            print(a)
        if N==a:
            return True
        else:
            return False
Solution().isArmstrong(153)