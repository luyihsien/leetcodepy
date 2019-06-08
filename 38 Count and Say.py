#此題我搞不清楚要如何判斷何時1何時2 猜:
'''
class Solution:
    def countAndSay(self, n: int) -> str:
'''

'''
i代表字符下标，从0开始取值，也就是从第一个字符开始
因为要让i取到最后一个字符，并且后面还要进行i+1的操作
所以将原字符串随意加上一个‘*’字符防止溢出
Q1 有做字串內增刪嗎?字串內本就不能刪或自由增(除了str+'a'這種直接尾巴增存到另一數，以及.replace()可以改

class Solution:
    def countAndSay(self, n):
        if n==1:
            return '1'
        else:
            i='1*'
            count=1
            for j in range(n-1):
                if i[j]==i[j+1]:
                    count+=1
                else:
                    i+=str(count)+i[j]
                    count=1
        return i[0:len(i-1)]
            
'''
a='123'
a+='1'#不能改，但能從最尾增東西
print(a)

class Solution(object):
    def countAndSay(self, n):#反覆從第14列執行至21列
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n-1) + '*'#星號不會有問題，一堆星號??不會，因為都先處理完return了
        print(s)
        res, count = '', 1
        for i in range(len(s)-1):
            print(s[i],s[i+1])
            if s[i] == s[i+1]:
                print('s[i]',s[i])
                count += 1
                print('count',count)
            else:
                res += str(count) + str(s[i])
                print('res',res)
                count = 1
                print('count',count)
        return res
print(Solution().countAndSay(8))
'''
1*
11*
21*
1211*
111221*
312211*
13112221*
1113213211*
31131211131221*
'''
b=Solution().countAndSay(2)
a=Solution().countAndSay(2)
print(a==b)
print(a is b)