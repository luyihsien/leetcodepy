'''
import collections
class Solution:
    def longestArithSeqLength(self, A) -> int:
        n = len(A)
        dp = [collections.Counter() for _ in range(n)]
        print('dp',dp)
        ans = 0
        for i in range(n):
            for j in range(i - 1, -1, -1):
                dp[i][A[i] - A[j]] = max(dp[i][A[i] - A[j]], dp[j][A[i] - A[j]] + 1)
                #此時dp[i][A[i] - A[j]]=0<誤>以為等於None or會產生error
                print('dp',dp)
                ans = max(ans, dp[i][A[i] - A[j]])
        return ans + 1
        
'''


class Solution:#時複O(n^2)
    def longestArithSeqLength(self, A):
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[(j, A[j] - A[i])] = dp.get((i, A[j] - A[i]), 1) + 1
                #print('dp',dp)
        return max(dp.values())
print(Solution().longestArithSeqLength([20,1,15,3,10,5,8]))