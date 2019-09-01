import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def maxAncestorDiff(self, root) -> int:
        def dfs(node, mn=math.inf, mx=-math.inf):#以上local參數隨你操縱
            if node:
                print('dfs(TreeNode({}))'.format(node.val),'left value id',id())
                mn = min(mn, node.val)
                mx = max(mx, node.val)
                print('mn',mn,id(mn),'mx',mx,id(mx))
                dfs(node.left, mn, mx)
                dfs(node.right, mn, mx)
            else:
                self.ans = max(self.ans, mx - mn)
        self.ans = 0
        dfs(root)
        return self.ans
a=TreeNode(8)
a.left=TreeNode(3)
a.left.left=TreeNode(1)
a.left.right=TreeNode(6)
a.left.right.left=TreeNode(4)
a.left.right.right=TreeNode(7)
a.right=TreeNode(10)
a.right.right=TreeNode(14)
a.right.right.left=TreeNode(13)
print(Solution().maxAncestorDiff(a))