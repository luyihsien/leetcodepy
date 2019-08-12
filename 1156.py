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
        for i in range(n):
            print('i',i)
            r = 1
            s=i+1
            while s<n and c[text[i]]>1:
                print('i',i,'s',s,'res',res,'r',r,'n',n)
                if text[i]!=text[s] and c[text[i]]>1:
                    r-=1
                    if r<0:
                        break
                    s = s + 1
                print('res',res,'s-i',s-i)
                if s-i<=c[text[i]]:
                    res=max(res,s-i)

        return res
print(Solution().maxRepOpt1(text = "ababa"))
print(Solution().maxRepOpt1("abcdef"))

