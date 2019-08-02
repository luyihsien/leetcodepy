class Solution:
    def subsets(self, nums:'list[int]'):#-> List[List[int]]
        res = []
        n = len(nums)

        def helper(i, tmp):#i表示下次要去的座標
            print('helper({},{})'.format(i,tmp))
            res.append(tmp)#先增這次的
            print('res',res)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        #res.sort()#Solution().subsets([3,2,1])) 輸出變[[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
        return res
print(Solution().subsets([3,2,1]))#[[], [3], [3, 2], [3, 2, 1], [3, 1], [2], [2, 1], [1]]
"""
helper(0,[])
res [[]]
helper(1,[3])
res [[], [3]]
helper(2,[3, 2])
res [[], [3], [3, 2]]
helper(3,[3, 2, 1])#靠著比len小(即len-1)停止
res [[], [3], [3, 2], [3, 2, 1]]#Why??在第二次呼叫那裏，不是第一次，參考backtracking的解法
helper(3,[3, 1])
res [[], [3], [3, 2], [3, 2, 1], [3, 1]]
helper(2,[2])
res [[], [3], [3, 2], [3, 2, 1], [3, 1], [2]]
helper(3,[2, 1])
res [[], [3], [3, 2], [3, 2, 1], [3, 1], [2], [2, 1]]
helper(3,[1])
res [[], [3], [3, 2], [3, 2, 1], [3, 1], [2], [2, 1], [1]]
[[], [3], [3, 2], [3, 2, 1], [3, 1], [2], [2, 1], [1]]

"""
def a():
    for i in range(1,11):
        return i
print(a())#1
class Solution:
    def subsets(self,nums):
        res=[[]]
        for i in nums:
            res=res+[[i]+num for num in res]#先將上一個res遍歷並處理過後，才賦值給新res故不會一邊改一邊遍大(有拿額外list去盛)
            print('i',i,'res',res)
        return res
print(Solution().subsets([3,2,1]))
"""
i 3 res [[], [3]]
i 2 res [[], [3], [2], [2, 3]]
i 1 res [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
[[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
"""