import collections
class Solution:
    def countCharacters(self, words, chars: str) -> int:
        res=0
        for i in words:
            d =collections.Counter(chars)
            #print('d',d)
            for j in i:
                d[j]-=1
            if min(d.values())>=0:
                res+=len(i)
        return res
print(Solution().countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))
d=collections.Counter()
print(d[1])