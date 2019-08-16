from collections import Counter
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        #print('trust',trust)
        o = Counter(a for a, b in trust)
        i = Counter(b for a, b in trust)
        #print('o',o,'i',i)
        for p in range(1, N+1):
            #print('p',p,'o[p]',o[p],'i[p]',i[p])
            if o[p] == 0 and i[p] == N-1:
                return p
        return -1
print(Solution().findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]))