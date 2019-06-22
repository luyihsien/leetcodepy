c = 0
class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        path = []
        res = []
        self.dfs(nums, path, res)
        return res

    def dfs(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path)
            print('res',res)
            return

        for i in nums:
            if i not in path:
                print('i',i)
                path.append(i)
                b = path[:]
                print('b',b)
                global c
                c=c+1
                print(c)
                self.dfs(nums, b, res)
                print('pop前path',path)
                path.pop()
                print('pop後path',path)
Solution().permute([1,2,3])
'''
作者：zong_mingyang
链接：https: // leetcode - cn.com / problems / two - sum / solution / quan - pai - lie - by - zong_mingyang /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''