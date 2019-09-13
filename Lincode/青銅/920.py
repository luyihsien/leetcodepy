'''
920. 会议室
中文English
给定一系列的会议时间间隔，包括起始和结束时间[[s1,e1]，[s2,e2]，…(si < ei)，确定一个人是否可以参加所有会议。

样例
样例1

输入: intervals = [(0,30),(5,10),(15,20)]
输出: false
解释:
(0,30), (5,10) 和 (0,30),(15,20) 这两对会议会冲突
样例2

输入: intervals = [(5,8),(9,15)]
输出: true
解释:
这两个时间段不会冲突
'''
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        n=len(intervals)
        for i in range(n-1):
            for j in range(i+1,n):
                if intervals[i][1]>intervals[j][0] or intervals[i][0]<intervals[j][1]:
                    return False
        return True