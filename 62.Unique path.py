class Solution:
    def uniquePaths(self, m: int, n: int, d={}) -> int:

        if m < 1 or n < 1: return 0
        if m == 1 and n == 1: return 1
        if (m, n) in d:#if m,n in d 是不對的，一定要有小括號
            return d[(m, n)]
        d[(m, n)] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        return d[m, n]
