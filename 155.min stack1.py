#https://leetcode-cn.com/problems/min-stack/solution/python-mei-ge-yi-xing-by-knifezhu/
class MinStack:
    def __init__(self):
        self.data = [(None, float('inf'))]

    def push(self, x):
        self.data.append((x, min(x, self.data[-1][1])))

    def pop(self):
        if len(self.data) > 1: self.data.pop()

    def top(self):
        return self.data[-1][0]

    def getMin(self):
        return self.data[-1][1]
