class Solution:
    def threeSum(self, nums):
        L = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]  #把nums[left]+nums[right]记做res
                l = [nums[i],nums[left],nums[right]]
                if s == 0:
                    L.append(l)
                    left += 1  #先从两边找两个数的和为res,然后逐渐向中间收缩
                    while left<right and nums[left]==nums[left-1]:
                        left += 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return L
