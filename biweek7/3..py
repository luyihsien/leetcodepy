
'''
5062. 连接棒材的最低费用  显示英文描述  
用户通过次数 29
用户尝试次数 39
通过次数 29
提交次数 45
题目难度 Medium
为了装修新房，你需要加工一些长度为正整数的棒材 sticks。

如果要将长度分别为 X 和 Y 的两根棒材连接在一起，你需要支付 X + Y 的费用。 由于施工需要，你必须将所有棒材连接成一根。

返回你把所有棒材 sticks 连成一根所需要的最低费用。注意你可以任意选择棒材连接的顺序。

 

示例 1：

输入：sticks = [2,4,3]
输出：14
解释：先将 2 和 3 连接成 5，花费 5；再将 5 和 4 连接成 9；总花费为 14。
示例 2：

输入：sticks = [1,8,3,5]
输出：30

'''
import heapq
sticks = [1,8,3,5]
for i in range(len(sticks)):
    if len(sticks)==1:
        break
    p1 = heapq.heappop(sticks)
    p2 = heapq.heappop(sticks)
    p = p1 + p2
    heapq.heappush(sticks,p)
    print(sticks)
class Solution:
    def connectSticks(self, sticks) -> int:
        heapq.heapify(sticks)
        res=0
        for i in range(len(sticks)):
            if len(sticks) == 1:
                break
            p1=heapq.heappop(sticks)
            p2=heapq.heappop(sticks)
            p=p1+p2
            res+=p
            heapq.heappush(sticks,p)
        return res
#Solution().connectSticks(sticks = [1,8,3,5])
print(Solution().connectSticks(sticks = [1,8,3,5]))