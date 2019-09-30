class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s1=''
        n=len(s)
        c=0
        l=0
        for i in range(n):
            if s[i]==s[l]:
                c+=1
                if c == k:
                    c = 0
                    l = i+1
                    continue
            else:
                s1+=s[l]*c
                c=0
                l=i+1

        return s1
print(Solution().removeDuplicates(s = "deeedbbcccbdaa", k = 3))
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        f =True
        while f:
            f=False
            d = 'abcdefghijklmnopqrstuvwxyz'
            for i in d:
                while i * k in s:
                    s =s.replace(i * k, '')
                    f = True
        return s
print(Solution().removeDuplicates(s = "deeedbbcccbdaa", k = 3))
