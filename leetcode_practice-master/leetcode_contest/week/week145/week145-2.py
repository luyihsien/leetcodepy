
"""
1124. Longest Well-Performing Interval
We are given hours, a list of the number of hours worked per day for a given employee.
A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

 
Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
 

Constraints:

1 <= hours.length <= 10000
0 <= hours[i] <= 16
"""
class Solution:
    def longestWPI(self, hours):
        hours = [1 if h > 8 else -1 for h in hours]
        print('hours',hours)
        s = 0
        ans = 0
        memo = {0 : -1}
        for i, v in enumerate(hours):
            s += v
            print('s',s)
            if s > 0:
                ans = i + 1
                print('ans',ans)
            if s not in memo:
                memo[s] = i
                print('meno[s]',memo[s],'memo',memo)
            if (s - 1) in memo:
                ans = max(ans, i - memo[s - 1])
                print('ans max',ans)
        return ans
#Rank2 badgergo
print(Solution().longestWPI([9,9,6,0,6,6,9,9,9,9,9,9,9]))