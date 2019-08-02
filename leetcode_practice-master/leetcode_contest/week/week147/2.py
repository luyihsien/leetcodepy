board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
class Solution:
    def alphabetBoardPath(self, target: str):
        a = [[0, 0]]
        b = []
        for i in target:
            for j in range(len(board)):
                for k in range(len(board[j])):
                    if i==board[j][k]:
                        a.append([j,k])
        for m in range(len(a)-1):
            b.append([a[m+1][0]-a[m][0],a[m+1][1]-a[m][1]])
        #print(b)
        c=''
        for i in range(len(b)):
            if b[i][1] > 0:
                c += 'R' * abs(b[i][1])
            if b[i][1] < 0:
                c += 'L' * abs(b[i][1])
            if b[i][0]>0:
                c += 'D' * abs(b[i][0])
            if b[i][0] < 0:
                c += 'U' * abs(b[i][0])
            c+='!'
            #print(c)
        return c


#print(Solution().alphabetBoardPath("leet"))
#print(Solution().alphabetBoardPath('code'))
#RRU!LLUUU!!RRR!
print(Solution().alphabetBoardPath('zdz'))
board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

class Solution:
    def alphabetBoardPath(self, target: str):
        m={c:[i//5,i%5] for i,c in enumerate('abcdefghijklmnopqrstuvwxyz') }
        print(m)
        x0,y0=0,0
        res=[]
        for c in target:
            #print('c',c)
            x,y=m[c]
            #print('x,y',x,y)
            if y<y0:res.append('L'*(y0-y))
            if x<x0:res.append('U'*(x0-x))
            if x>x0:res.append('D'*(x-x0))
            if y>y0:res.append('R'*(y-y0))
            res.append('!')
            x0,y0=x,y
        return "".join(res)
print(Solution().alphabetBoardPath('b'))
print(Solution().alphabetBoardPath("zdz"))
print(Solution().alphabetBoardPath("leet"))