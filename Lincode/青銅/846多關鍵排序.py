'''
846. 多关键字排序
中文English
给定 n 个学生的学号(从 1 到 n 编号)以及他们的考试成绩，表示为(学号，考试成绩)，请将这些学生按考试成绩降序排序，若考试成绩相同，则按学号升序排序。

样例
样例1

输入: array = [[2,50],[1,50],[3,100]]
输出: [[3,100],[1,50],[2,50]]
样例2

输入: array = [[2,50],[1,50],[3,50]]
输出: [[1,50],[2,50],[3,50]]
'''
a=[[3,4,5],[1,2,3],[1,3,2],[3,5,5],[1,10,3]]
a.sort(key=lambda x:(x[0],-x[2],-x[1]))#按重要程度排序
print(a)
print(type(sorted((123,345,11,0))))
class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """
    def multiSort(self, array):
        a=sorted(array,key=lambda x:(-x[1],x[0]))
        return a
        # Write your code here