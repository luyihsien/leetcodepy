class Solution:
    def minCostToMoveChips(self, chips) -> int:
        c0=map(lambda x:x%2,chips)
        c1=map(lambda x:(x%2+1)%2,chips)
        return min(sum(c0),sum(c1))
print(Solution().minCostToMoveChips(chips = [2,2,2,3,3]))
a=[1,2,3]
print(a.pop())
print(a)