# 时间复杂度: O(lgx)  空间复杂度: O(1)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            print(self.reverse(-x))#負負得正了#類似使用了abs(x) 並再次呼叫進到下方程式碼做處理<誤>以為有一個內建reverse可以用
            return -self.reverse(-x)#最前面再多個負號
        res = 0
        while x:#x=0 or x=None 則跳出，非二者則繼續#vs: for i in x:#其x必須要可迭代，並非int的變化去判別 而while只依給的條件去判，能容較多型別
            res = res * 10 + x % 10
            x //= 10#視同x=x//10
        return res if res <= 0x7fffffff else 0
        #https://blog.csdn.net/zqhhuiyi/article/details/51023868 if else單列
        #https://blog.csdn.net/su_bao/article/details/81484483 if else單列
        #https://cloud.tencent.com/developer/ask/36683#0x7fffffff為內建的無限大#why else 0 是題目要的
Solution().reverse(-123)
'''
https://blog.csdn.net/htuhxf/article/details/79954828
if i>100:
    x=2
elif i<100:
    x=1
else:
    x=0
等同 
x=2 if i>100 else i<100 1 else 0 
'''