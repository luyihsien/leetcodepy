class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        # dp[i][j] stores the sum of A[0][j], A[1][j], ..., A[i][j].
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            for i in range(m):
                if i == 0: dp[i][j] = matrix[0][j]
                else: dp[i][j] = dp[i - 1][j] + matrix[i][j]
        rtn = 0
        # enumerate r1, r2.
        for r1 in range(m):
            for r2 in range(r1, m):
                # A[r1...r2][c...d] = target
                index = {0: 1}
                curr = 0
                for c in range(n):
                    curr += dp[r2][c]
                    if r1: curr -= dp[r1 - 1][c]
                    if curr - target in index:
                        rtn += index[curr - target]
                    if curr not in index: index[curr] = 1
                    else: index[curr] += 1
        return rtn
