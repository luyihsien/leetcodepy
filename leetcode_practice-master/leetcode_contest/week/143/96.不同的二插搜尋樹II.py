class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    def generateTrees(self, n: int):
        if n == 0: return []#去掉會error

        def helper(start, end):
            res = []
            if start > end:
                res.append(None)
            for val in range(start, end + 1):#以val為樹根#1至n
                for left in helper(start, val - 1):#<誤>若小於就不會入，but在這之前append了None#依然會入但僅一次，因裡面包的None只一個，且會放入左右子樹
                    for right in helper(val + 1, end):
                        print('left',left)
                        root = TreeNode(val)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res#超重要#參第13列#

        return helper(1, n)
"""
第八行若未加
输入:
0
stdout
res []
输出
[[]]
预期结果
[]
"""
Solution().generateTrees(3)