class Solution:
    def uniquePaths(self, m: int, n: int,d={}) -> int:
        print('uniqe({},{})'.format(m,n),'d',d)
        if m < 1 or n < 1: return 0
        if m == 1 and n == 1: return 1
        if (m, n) in d:#if m,n in d 是不對的，一定要有小括號
            print('節省')
            return d[(m, n)]
        d[(m, n)] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        print('d[({}, {})] = self.uniquePaths({},{}) + self.uniquePaths({},{})'.format(m,n,m-1,n,m,n-1))
        return d[m, n]
print(Solution().uniquePaths(3,2))