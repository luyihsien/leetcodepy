class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            cur = min(height[left], height[right]) * (right - left)
            area = max(area, cur)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
print(Solution().maxArea([10,1,1,1000000,999999,1,1,10]))#誤1000000
#right-left至少要大於等於1