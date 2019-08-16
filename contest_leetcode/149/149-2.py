import collections,itertools
c=collections.Counter('hellowl')
print(c.most_common(1)[0][0])
#Q 1156
#https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
class Solution:#
    def maxRepOpt1(self, s: str) -> int:
        res = 0
        count = collections.Counter()
        countChar = collections.Counter(s)
        print('countChar',countChar)
        start = 0
        maxCount = 0
        maxChar = s[0]

        for right in range(len(s)):
            count[s[right]] += 1
            print('count',count,'count[s[right]]',count[s[right]],'s[right]',s[right])
            maxCount = max(count[s[right]], maxCount)
            print('maxcount',maxCount)
            print('right - start + 1 - maxCount',right - start + 1 - maxCount)
            while right - start + 1 - maxCount > 1:#我可以接受目前量之下透支一個且繼續計算，但兩個我不行#right很單純的一直往前衝(亦是終止條件)#start在未透支到兩個預算前不會動
                count[s[start]] -= 1
                start += 1
            print('count.items()',count.items(),'count',count)
            maxChar = max(count.items(), key=lambda x: x[1])[0]#maxChar=count.most_common(1)[0][0]也可
            print('maxchar',maxChar)
            print('right',right,'start',start,'right - start + 1',right - start + 1,'res',res)
            if right - start + 1 > res:
                res = right - start + 1
            print('res',res)
        return min(res, countChar[maxChar])
print(Solution().maxRepOpt1('aabbbbbaa'))




#https://leetcode.com/problems/swap-for-longest-repeated-character-substring/discuss/355852/Python-Groupby
#groupby function
'''
class Solution:
    def maxRepOpt1(self, S):
        A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
        count = collections.Counter(S)
        res = max(min(k + 1, count[c]) for c, k in A)
        for i in range(1, len(A) - 1):
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res
print(Solution().maxRepOpt1('aabbbbaa'))
'''