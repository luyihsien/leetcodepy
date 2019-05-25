class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
            # if self.climbStairs(1)==self.climbStairs(n-1):
            # return 2

        if self.climbStairs(n - 1) != self.climbStairs(1):
            return (self.climbStairs(n - 1) + self.climbStairs(1)) * 2
        else:
            return (self.climbStairs(n - 1) + self.climbStairs(1))#ex 4漏算2 2
