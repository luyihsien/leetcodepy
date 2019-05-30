print(len([1,1]))#2
a=[1]
a.extend([[1,1]])
print(a)
class Solution:
    def generate(self, numRows):
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        else:
            l=self.generate(numRows-1)
            for i in range(len(l)-1):
                l.insert(i,l[i]+l[i+1])
            return l


class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        else:
            l = self.generate(numRows - 1)
            for i in range(len(l) - 1):
                a = l[:]
                a[-1].insert(i, l[i] + l[i + 1])
                l.extend([a])
            return l
#list無法直接作加法
class Solution:
    def generate(self, numRows):
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        else:
            l=self.generate(numRows-1)
            for i in range(l[-1]):
                a=l[:][-1]
                a.insert(i,l[-1][i]+l[-1][i+1])
                l.extend([a])
            return
class Solution:

    def generate(self, numRows):
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        m=[[1],[1,1]]
        while numRows>2:
            m.extend([m[-1]])
            for i in range(len(m[-2])-1):#TypeError: object of type 'int' has no len()
                m[-1].insert(i+1,m[-1][i]+m[-1][i+1])
                numRows-=1
            return m



        '''
        else:
            l=self.generate(numRows-1)
            for i in range(len(l[-1])-1):
                a=l[:]
                b=a[-1]
                b.insert(i+1,l[-1][i]+l[-1][i+1])
                a.extend([b])
            return a
        '''

print(Solution().generate(3))#[[1], [2, 1, 1], [2, 1, 1]]
'''
输入
5
输出
[[1],[6,6,6,6,3,3,2,1,1],[6,6,6,6,3,3,2,1,1],[6,6,6,6,3,3,2,1,1],[6,6,6,6,3,3,2,1,1],[6,6,6,6,3,3,2,1,1],[6,6,6,6,3,3,2,1,1],[6,6,6,6,3,3,2,1,1],[6,6,6,6,3,3,2,1,1]]
预期结果
[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

'''
'''
只打return則
TypeError: 'NoneType' object is not subscriptable
'''