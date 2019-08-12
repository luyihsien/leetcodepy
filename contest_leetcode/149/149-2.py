import collections,itertools
#Q 1156
#https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
class Solution:#
    def maxRepOpt1(self, s: str) -> int:
        res = 0
        count = collections.Counter()
        countChar = collections.Counter(s)
        start = 0
        maxCount = 0
        maxChar = s[0]

        for right in range(len(s)):
            count[s[right]] += 1
            print('count[s[right]]',count[s[right]])
            maxCount = max(count[s[right]], maxCount)
            print('maxcount',maxCount)

            while right - start + 1 - maxCount > 1:
                count[s[start]] -= 1
                start += 1
            print('count.items()',count.items(),'count',count)
            maxChar = max(count.items(), key=lambda x: x[1])[0]
            if right - start + 1 > res:
                res = right - start + 1
        return min(res, countChar[maxChar])
Solution().maxRepOpt1('ababa')
#https://leetcode.com/problems/swap-for-longest-repeated-character-substring/discuss/355852/Python-Groupby
#groupby function
class Solution:
    def maxRepOpt1(self, S):
        A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
        count = collections.Counter(S)
        res = max(min(k + 1, count[c]) for c, k in A)
        for i in range(1, len(A) - 1):
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res
