class Solution:
    def kthLargestElement(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        return self.partition(A, 0, len(A) - 1, len(A) - k)#最後一項因(len(A)-1)-(k-1)

    def partition(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[k]

        left, right = start, end
        pivot = nums[(start + end) // 2]
        print('pivot',pivot)
        while left <= right:
            print('while left <= right:')
            while left <= right and nums[left] < pivot:
                left += 1
                print('1  left', left)
            while left <= right and nums[right] > pivot:
                right -= 1
                print('1  right',right)
            if left <= right:
                print('nums前',nums)
                nums[left], nums[right] = nums[right], nums[left]
                print('nums後',nums)
                print('nums[{}], nums[{}] = nums[{}], nums[{}]'.format(left,right,right,left))
                print('前right,left',right,left)
                left, right = left + 1, right - 1
                print('後right,left', right, left)

        # left is not bigger than right
        print('k',k)
        if k <=right:
            return self.partition(nums, start, right, k)
        if k >=left:
            return self.partition(nums, left, end, k)

        return nums[k]
print('ans',Solution().kthLargestElement(8,[26,5,1,61,11,59,37,15,48,19]))
class Solution:
    def kthLargestElement(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        return self.partition(A, 0, len(A) - 1, len(A) - k)#最後一項因(len(A)-1)-(k-1)

    def partition(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[k]

        left, right = start, end
        pivot = nums[start]
        print('pivot',pivot)
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
                print('1  left', left)
            while left <= right and nums[right] > pivot:
                right -= 1
                print('1  right',right)
            if left <= right:
                print('nums前',nums)
                nums[left], nums[right] = nums[right], nums[left]
                print('nums後',nums)
                print('nums[{}], nums[{}] = nums[{}], nums[{}]'.format(left,right,right,left))
                print('前right,left',right,left)
                left, right = left + 1, right - 1
                print('後right,left', right, left)

        # left is not bigger than right
        if k <= right:#座標比大小
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)

        return nums[k]
print(Solution().kthLargestElement(1,[1,2,3,4,5,6]))