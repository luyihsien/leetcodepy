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
a=[[1,2],[3,4]]
print('a[0]',a[0])#[1,2]
print('a[0:1]',a[0:1])#[[1,2]]
class Solution:
    def twoSum(self, nums, target):
        idxDict = dict()
        idx_list = []
        for idx, num in enumerate(nums):#0至len(nums)-1，視同所有座標，每次增1;每項走一遍
            if target - num in idxDict:
                idx_list.append([idxDict[target - num], idx])#先 尋找曾經的idxDict[num]=idx 即[targe-num]座標 後 新idx跑出去
            idxDict[num] = idx#idxDict[數字]=座標#若一樣則會複寫
        return idx_list

    def threeSum(self, num):
        num.sort()
        res = dict()
        result = []
        for i in range(len(num)-2):  # 遍历至倒数第三个，后面两个指针
            if (i == 0 or num[i] > num[i-1]) and num[i] <= 0:  #num[i]只可能大於或等於num[i-1]因為sort過# 只检索不重复并且目标数（第一个数）小于等于0的情况
                left = i + 1
                print('left',left)
                # right = len(num) - 1
                result_idx = self.twoSum(num[left:], -num[i])#傳送位址#要是此class的實例才能用性質
                print("result_idx",result_idx)#index
                for each_idx in result_idx:# 数组后方切片后给twoSum
                    each_result = [num[i], num[each_idx[0]+(left)], num[each_idx[1]+(left)]]
                    print('each result',each_result)
                    print('res',res)
                    if str(each_result) not in res:#因list不能直接當key#下一次for又是新num[i]故在這裡就要先讀入
                        res[str(each_result)] = each_result
                    print('加入字典後 res',res)
        for value in res.values():#將所有key對應的value跑一遍
            result.append(value)
            print(value)
        print(result)
        return result
print('two sum for 7',Solution().twoSum([1,2,2,5],7))#[[1, 2], [2, 3]]故最好先sort過同3sum
print(Solution().threeSum([-4,-3,-3,-3,0,1,1,1,2,3,4,4,4,4]))#-4之下 1座標4 3座標6 又 0座標3 4座標7
#result_idx [[6, 8], [3, 9], [3, 10], [3, 11], [3, 12]]
#each result [-4, 1, 3]
#因-4 0 4 已在
'''
left 1
result_idx [[6, 8], [3, 9], [3, 10], [3, 11], [3, 12]]
each result [-4, 1, 3]
res {}
加入字典後 res {'[-4, 1, 3]': [-4, 1, 3]}
each result [-4, 0, 4]
res {'[-4, 1, 3]': [-4, 1, 3]}
加入字典後 res {'[-4, 1, 3]': [-4, 1, 3], '[-4, 0, 4]': [-4, 0, 4]}
each result [-4, 0, 4]
res {'[-4, 1, 3]': [-4, 1, 3], '[-4, 0, 4]': [-4, 0, 4]}
加入字典後 res {'[-4, 1, 3]': [-4, 1, 3], '[-4, 0, 4]': [-4, 0, 4]}
each result [-4, 0, 4]
res {'[-4, 1, 3]': [-4, 1, 3], '[-4, 0, 4]': [-4, 0, 4]}
加入字典後 res {'[-4, 1, 3]': [-4, 1, 3], '[-4, 0, 4]': [-4, 0, 4]}
each result [-4, 0, 4]
res {'[-4, 1, 3]': [-4, 1, 3], '[-4, 0, 4]': [-4, 0, 4]}
加入字典後 res {'[-4, 1, 3]': [-4, 1, 3], '[-4, 0, 4]': [-4, 0, 4]}
left 2
result_idx [[5, 6], [2, 7]]
each result [-3, 1, 2]
res {'[-4, 1, 3]': [-4, 1, 3], '[-4, 0, 4]': [-4, 0, 4]}
加入字典後 res {'[-4, 1, 3]': [-4, 1, 3], '[-4, 0, 4]': [-4, 0, 4], '[-3, 1, 2]': [-3, 1, 2]}
each result [-3, 0, 3]
res {'[-4, 1, 3]': [-4, 1, 3], '[-4, 0, 4]': [-4, 0, 4], '[-3, 1, 2]': [-3, 1, 2]}
加入字典後 res {'[-4, 1, 3]': [-4, 1, 3], '[-4, 0, 4]': [-4, 0, 4], '[-3, 1, 2]': [-3, 1, 2], '[-3, 0, 3]': [-3, 0, 3]}
left 5
result_idx []
[-4, 1, 3]
[-4, 0, 4]
[-3, 1, 2]
[-3, 0, 3]
[[-4, 1, 3], [-4, 0, 4], [-3, 1, 2], [-3, 0, 3]]
[[-4, 1, 3], [-4, 0, 4], [-3, 1, 2], [-3, 0, 3]]
3



'''
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
def a():
    print(b(1,2))
def b(x,y):
    return x+y
a()#3