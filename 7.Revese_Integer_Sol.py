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
        while x:#x=0 or x=None 則跳出，非二者則繼續
            res = res * 10 + x % 10
            x //= 10#視同x=x//10
        return res if res <= 0x7fffffff else 0#https://cloud.tencent.com/developer/ask/36683
Solution().reverse(-123)