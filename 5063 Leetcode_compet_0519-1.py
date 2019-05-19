'''
5063. 最后一块石头的重量  显示英文描述  
用户通过次数 0
用户尝试次数 0
通过次数 0
提交次数 0
题目难度 Easy
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
'''
'''
提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000
'''
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
'''
a=[2,2,2,3,3]
b=[1,3,2,4,5,9,7]
a.remove(max(a))#一次只移一個
a.remove(max(a))
#print(a)
'''
class Solution:
    def lastStoneWeight(self, stones):
        while(len(stones)>1):
            y=max(stones)
            stones.remove(y)
            print(stones)
            x=max(stones)
            stones.remove(x)
            print(stones)
            if x<y:
                stones.append(y-x)
            print(stones)
        return stones[0]
print(Solution().lastStoneWeight(b))
'''


class Solution:
    def lastStoneWeight(self, stones):
        while (len(stones) > 1):
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if x < y:
                stones.append(y - x)
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
