'''
521. 去除重复元素
中文English
给一个整数数组，去除重复的元素。

你应该做这些事

1.在原数组上操作
2.将去除重复之后的元素放在数组的开头
3.返回去除重复元素之后的元素个数

样例
例1:

输入:
nums = [1,3,1,4,4,2]
输出:
[1,3,4,2,?,?]
4

解释:
1. 将重复的整数移动到 nums 的尾部 => nums = [1,3,4,2,?,?].
2. 返回 nums 中唯一整数的数量  => 4.
事实上我们并不关心你把什么放在了 ? 处, 只关心没有重复整数的部分.
例2:

输入:
nums = [1,2,3]
输出:
[1,2,3]
3
挑战
1.O(n)时间复杂度.
2.O(nlogn)时间复杂度但没有额外空间

注意事项
不需要保持原数组的顺序
'''
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        s=0
        n=len(nums)
        for i in range(1,n):
            print('i',i,nums)
            if nums[i]==nums[s]:
                for j in range(i+1,n):
                    print('j',j)
                    if nums[i]!=nums[j]:
                        nums[i]=nums[j]#不表示i是j
                        s=i#s=j
                        print('s',s,'nums',nums)
                        break
        return (nums,s)
print(Solution().deduplication([1,3,1,4,4,2]))
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        s=0
        n=len(nums)
        for i in range(1,n):
            if nums[i]==nums[s]:
                for j in range(i,n):
                    if nums[i]!=nums[j]:
                        nums[i]=nums[j]
                        s=i
                        break
        return s+1
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if nums==[]:
            return 0
        se=set(nums[0])
        s=0
        for i in nums:
            if i not in se:
                se.add(i)
                s=s+1
                nums[s]=i
        return s
nums=[1,2,3]
a=set()
a.add(nums[0])
print(a)
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if nums==[]:
            return 0
        se=set()
        se.add(nums[0])
        s=0
        for i in nums:
            if i not in se:
                se.add(i)
                s=s+1
                nums[s]=i
        return s+1
        # write your code here