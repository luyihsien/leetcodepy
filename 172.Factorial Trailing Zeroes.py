class Solution:
    def fac(self,n):
        if n==0:
            return 1
        else:
            return self.fac(n-1)*n#呼叫函數#之所以要加self是因為要有實例才能呼叫method
print(Solution().fac(3))


class Solution:
    def fac(self, n):
        if n == 0:
            return 1
        else:
            return self.fac(n - 1) * n

    def trailingZeroes(self, n):
        a = self.fac(n)
        count = 0
        while a % 10 == 0:
            a, count = a // 10, count + 1
        return count
print(Solution().trailingZeroes(10))
class Solution:
    def fac(self,n):
        b=1
        for i in range(1,n+1):
            b=b*i
            print(b)
Solution().fac(10)


class Solution:
    def fac(self, n):
        b = 1
        for i in range(1, n + 1):
            b = b * i
        return b

    def trailingZeroes(self, n):
        a = self.fac(n)
        count = 0
        while a % 10 == 0:
            a, count = a // 10, count + 1
        return count
print(Solution().trailingZeroes(4108))