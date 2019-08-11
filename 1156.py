import collections
'''
import collections
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        res=0
        c=collections.Counter(text)
        s=[]
        n=len(text)
        for i in range(n):
            b=1
            a=0
            if s==[]:
                s.append(text[i])
                a=a+1
            elif s[-1]!=text[i] and c[s[-1]]>1 and b>0:
                s.append(s[-1])
                b-=1
'''
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        res=0
        c=collections.Counter(text)
        n=len(text)
        r=1
        for i in range(n):
            s=i+1
            print('i',i)
            while 1:
                print('res',res)
                if s<n and text[i]==text[s]:
                    print('s',s)
                    s=s+1
                if s<n and text[i]!=text[s] and c[i]>1:
                    r=r-1
                    print('r',r)
                    if r<0:
                        break
                    s=s+1
                if s<n and text[i]!=text[s] and c[i]<=1:
                    print('s',s)
                    break
            res=max(res,s-r)
            print('res',res)
        return res
#print(Solution().maxRepOpt1(text = "ababa"))
print(Solution().maxRepOpt1("aaabaaa"))
