import collections
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c0=collections.Counter("balloon")
        c=collections.Counter(text)
        for i in c0:
            c[i]=c[i]//c0[i]
        l=[]
        for i in c0:
            l.append(c[i])
        return min(l)



print(Solution().maxNumberOfBalloons(text = "nlaebolko"))
print(Solution().maxNumberOfBalloons("loonbalxballpoon"))
print(Solution().maxNumberOfBalloons('leetcode'))
a=[3,4]
print(a.pop())