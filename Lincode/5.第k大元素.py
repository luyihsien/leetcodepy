'''
Wrong test
3
[9,3,2,4,8]
import heapq
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        heapq._heapify_max(nums)
        for i in range(n):
            a=heapq.heappop(nums)
        return a
        # write your code here
'''
import heapq
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        heapq._heapify_max(nums)
        print(type(nums))
        for i in range(n):
            a=heapq._heappop_max(nums)
            print(a)
        return a
print(Solution().kthLargestElement(3,[9,3,2,4,8]))
b=[4,5,6]
heapq._heapify_max(b)
heapq._heappop_max(b)
print(b)