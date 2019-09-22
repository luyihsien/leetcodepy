import collections
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        l = [i for i in s]
        pairs.sort(key=lambda x: (l[x[0]],l[x[1]]))
        c=collections.Counter(tuple(i) for i in pairs)
        for i in c:
            print(i)
            if c[i]%2==1:
                l[i[0]],l[i[1]]=l[i[1]],l[i[0]]
                print('l',l)
        return ''.join(l)
print(Solution().smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))



#print(l)#['dcab']
