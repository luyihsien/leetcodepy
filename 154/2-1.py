class Solution:
    def reverseParentheses(self, s: str) -> str:
        l=[]
        l0=[]
        l1=[]
        n=len(s)
        for i in s:
            l1.append(i)
        for i in range(n):
            if s[i]=='(':
                l.append(i+1)
            if s[i]==')':
                l0.append(i-1)
        l[:]=l[:][::-1]
        m = len(l)
        for i in range(m):
            l1[l[i]:l0[i]+1]=l1[l[i]:l0[i]+1][::-1]
        while '(' in l1:
            l1.remove('(')
        while ')' in l1:
            l1.remove(')')
        return ''.join(l1)


print(Solution().reverseParentheses(s = "a(bcdefghijkl(mno)p)q"))