'''
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
            print('非座標而是值未判i=', i)
            if i not in path:
                print('判後i',i)
                path.append(i)
                b = path[:]
                print('b',b)
                global c
                c=c+1
                print('c=',c)
                print('nums',nums,'b',b,'res',res)
                self.dfs(nums, b, res)
                print('pop前path',path,'c',c)
                path.pop()
                print('pop後path',path,'c',c)
                print('i最後',i)
                #print('num最後', nums, 'b', b, 'res', res)
Solution().permute([1,2,3])
'''
'''
作者：zong_mingyang
链接：https: // leetcode - cn.com / problems / permutations/ solution / quan - pai - lie - by - zong_mingyang /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution:
    def permute(self,nums):
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                print(res)
                return
            for i in range(len(nums)):
                print('i',i)
                print('nums[:i] + nums[i+1:]',nums[:i] + nums[i+1:],'tmp + [nums[i]]',tmp + [nums[i]])
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res
Solution().permute([1,2,3])
'''
作者：powcai
链接：https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''