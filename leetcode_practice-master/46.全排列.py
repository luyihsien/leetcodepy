class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        ans = []
        for i, j in enumerate(nums):
            n = nums[:i] + nums[i + 1:]
            for k in self.permute(n):#放在排列區讓他排
                ans.append([j] + k)
        return ans

#用逆推回去想
