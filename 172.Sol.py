class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0

        while n >= 5:

            res += n // 5
            print('res', res)
            n //= 5
            print('n',n)

        return res
'''
res 20
n 20
res 24
n 4
24
'''
'''
P.S.：[ x ]=小於等於x的最大整數。如[26/5]=[5.2]=5，[50/5]=[10]=10 

例 100!= 1*2*3*...*100 
[100/5](一個5)+[100/25](2個5=原本除以五下的再加上可以再除以一個5)+[100/125]+... 
=[20.…]+[4.…]+[0.…]+... 
=20+4+0+... (5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100) (25,50,75,100)
=24 
∴共有24個0 
'''

#作者：jalan 題解
'''
题目问阶乘的结果有几个零，如果用笨方法求出阶乘然后再算 0 的个数会超出时间限制。

然后我们观察一下，5 的阶乘结果是 120，零的个数为 1：

5! = 5 * 4 * 3 * 2 * 1 = 120
末尾唯一的零来自于 2 * 5。很显然，如果需要产生零，阶乘中的数需要包含 2 和 5 这两个因子。

例如：4 * 10 = 40 也会产生零，因为 4 * 10 = ( 2 * 2 ) * ( 2 * 5) 。

因此，我们只要数一数组成阶乘的数中共有多少对 2 和 5 的组合即可。又因为 5 的个数一定比 2 少，问题简化为计算 5 的个数就可以了。

作者：jalan
链接：https://leetcode-cn.com/problems/two-sum/solution/tong-guo-guan-cha-chan-sheng-ling-de-tiao-jian-er-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
print(Solution().trailingZeroes(100))