l=[1,2,3,4]
l[1:4]=l[1:4][::-1]
print(l)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        l=[]
        n=len(s)
        i=0
        print(n)
        while i<n:
            print('i',i,'n',n)
            if s[i]!=')':
                l.append(s[i])
                i+=1
                print('l append後',l,'i',i)
            else:
                a=i-1
                print('a',a)
                while l[a]!='(':
                    a-=1
                    print('a減一',a)
                print('a',a)
                l[a+1:i]=l[a+1:i][::-1]
                print(l)
                l.pop(a)
                print(l)
                i=i-2
                n=n-1
                i+=1

                print('i',i)
        return l
print(Solution().reverseParentheses(s ="a(bcdefghijkl(mno)p)q"))