'''
Given an array A of positive integers (not necessarily distinct), return the lexicographically largest permutation that is smaller than A, that can be made with one swap (A swap exchanges the positions of two numbers A[i] and A[j]).  If it cannot be done, then return the same array.
Example 1:
Input: [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:
Input: [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:
Input: [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
Example 4:
Input: [3,1,1,3]
Output: [1,3,1,3]
Explanation: Swapping 1 and 3.
Note:
1 <= A.length <= 10000
1 <= A[i] <= 10000
'''
class Solution():
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        for i in range(n - 2, -1, -1):#本來倒敘就要少一，此處又用i+1判故少2
            print('A[i]',A[i],'A[i+1]',A[i+1])
            if A[i] > A[i + 1]:
                break
        else:
            return A
        for j in range(n - 1, i, -1):
            print('A[j]',A[j],'A[i]',A[i])
            if A[j] < A[i]:
                break
        A[i], A[j] = A[j], A[i]
        return A
print(Solution().prevPermOpt1([1,9,4,6,7]))
print(Solution().prevPermOpt1([3,1,1,3]))
class Solution:
    def prevPermOpt1(self, nums):
        if len(nums) < 2:
            return nums
        k, l = -1, -1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                k = i
                l = i+1
            elif k != -1 and nums[i] < nums[k]:
                l = i
        if k == -1:
            return nums
        else:
            if nums[-1] < nums[k]:
                l = len(nums)-1
            nums[k], nums[l] = nums[l], nums[k]
        return nums
print(Solution().prevPermOpt1([1,9,4,6,7]))
print(Solution().prevPermOpt1([3,1,1,3]))