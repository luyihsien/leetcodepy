import collections
class Solution:
    def countLetters(self, S: str) -> int:
        s=S[0]
        c=1
        Sum=0
        for i in range(1,len(S)):
            #print('i',i,'S[i]',S[i],'c',c,'s',s)
            if S[i]==s:
                c+=1
            else:
                Sum+=(c*(c+1))//2
                #print('Sum',Sum)
                s=S[i]
                c=1
            if i==len(S)-1:
                Sum+=(c*(c+1))//2
        return Sum
print(Solution().countLetters("jjjjxttttn"))


