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
