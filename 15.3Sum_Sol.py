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
'''
class Solution:
    def twoSum(self, nums, target):
        idxDict = dict()
        idx_list = []
        for idx, num in enumerate(nums):
            if target - num in idxDict:
                idx_list.append([idxDict[target - num], idx])
            idxDict[num] = idx
        return idx_list

    def threeSum(self, num):
        num.sort()
        res = dict()
        result = []
        for i in range(len(num)-2):  # 遍历至倒数第三个，后面两个指针
            if (i == 0 or num[i] > num[i-1]) and num[i] <= 0:  # 只检索不重复并且目标数（第一个数）小于等于0的情况
                left = i + 1; 
                # right = len(num) - 1
                result_idx = self.twoSum(num[left:], -num[i])
                for each_idx in result_idx:  # 数组后方切片后给twoSum
                    each_result = [num[i], num[each_idx[0]+(i+1)], num[each_idx[1]+(i+1)]]
                    if str(each_result) not in res:
                        res[str(each_result)] = each_result
        for value in res.values():
            result.append(value)
        return result    
--------------------- 
作者：Rude3knife 
来源：CSDN 
原文：https://blog.csdn.net/qqxx6661/article/details/77104862 
版权声明：本文为博主原创文章，转载请附上博文链接！

'''
class Solution:
    def twoSum(self, nums, target):
        idxDict = dict()
        idx_list = []
        for idx, num in enumerate(nums):
            if target - num in idxDict:
                idx_list.append([idxDict[target - num], idx])
            idxDict[num] = idx
        return idx_list

    def threeSum(self, num):
        num.sort()
        res = dict()
        result = []
        for i in range(len(num)-2):  # 遍历至倒数第三个，后面两个指针
            if (i == 0 or num[i] > num[i-1]) and num[i] <= 0:  # 只检索不重复并且目标数（第一个数）小于等于0的情况
                left = i + 1
                print('left',left)
                # right = len(num) - 1
                result_idx = self.twoSum(num[left:], -num[i])
                print("result_idx",result_idx)#index
                for each_idx in result_idx:# 数组后方切片后给twoSum
                    each_result = [num[i], num[each_idx[0]+(i+1)], num[each_idx[1]+(i+1)]]
                    print(each_result)
                    if str(each_result) not in res:
                        res[str(each_result)] = each_result
        for value in res.values():
            result.append(value)
        return result
print(Solution().threeSum([-4,-3,-3,-3,1,2,3]))
'''
print(Solution().threeSum([-4,-3,-3,-3,1,2,3]))
left 1
result_idx [[3, 5]]
[-4, 1, 3]
left 2
result_idx [[2, 3]]
[-3, 1, 2]
[[-4, 1, 3], [-3, 1, 2]]
'''
