class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        l=[]
        for i in range(len(S)-K+1):
            l.append(S[i:i+K])
        d1=[]
        for k in l:
            a=set()
            for i in k:
                if i not in a:
                    a.add(i)
                else:
                    d1.append(k)
                    break
        for i in d1:
            l.remove(i)
        return len(l)
print(Solution().numKLenSubstrNoRepeats("havefunonleetcode",5))
print(Solution().numKLenSubstrNoRepeats("home",5))
logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
logs.sort()
b=set()
for i in logs:
    b.add({i[1],i[2]})
print(b)
