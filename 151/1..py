#print(min(['z','y','w','c','b','aaa']))
print(min('abcdefghijk'))

import collections
class Solution:
    def numSmallerByFrequency(self, queries, words):
        c=[i.count(min(i)) for i in words]
        c.sort(reverse=True)
        d=[i.count(min(i)) for i in queries]
        n=len(d)
        ans=[]
        for i in range(n):
            res=0
            for j in c:
                if d[i]<j:
                    res+=1
                else:
                    break
            if res>=0:
                ans.append(res)
        return ans


import collections


class Solution:
    def invalidTransactions(self, transactions):
        res = []
        c = collections.Counter()
        for i in transactions:
            j = i.split(',')
            if int(j[2]) > 1000:
                res.append(i)
                continue
            if c[j[0]] == 0:
                c[j[0]] = [j[1]]
            if c[j[0]] != 0:
                for _ in c[j[0]]:
                    if abs(int(_) - int(j[1])) <= 60:
                        res.append(i)
            c[j[0]].append(j[1])
        return res


print(Solution().numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"]))
print(Solution().numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))
print(Solution().numSmallerByFrequency(["aabbabbb","abbbabaa","aabbbabaa","aabba","abb","a","ba","aa","ba","baabbbaaaa","babaa","bbbbabaa"],
["b","aaaba","aaaabba","aa","aabaabab","aabbaaabbb","ababb","bbb","aabbbabb","aab","bbaaababba","baaaaa"]))








