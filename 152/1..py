class Solution:
    def dietPlanPerformance(self, calories, k: int, lower: int, upper: int) -> int:
        n = len(calories)
        c = 0
        for i in range(0, n - k + 1):
            print(calories[i:i + k])
            if sum(calories[i:i + k]) < lower:
                c -= 1
                continue
            if sum(calories[i:i + k]) > upper:
                c += 1
        return c
print(Solution().dietPlanPerformance([6,13,8,7,10,1,12,11],6,5,37))