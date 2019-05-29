'''
思路
1)递归：根节点对应的最大深度是左右子树最大深度的最大值加一。

2）广度优先搜索： 广度优先搜索最后到达的叶子节点的是最大深度。

3）深度优先搜索：记录各节点的深度，通过访问到的叶子节点的深度更新max，直到遍历完成。

实例
#(1)递归：
'''
class Solution:
    def maxDepth(self, root):
        if not root: return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))


#(2)广度优先搜索：

class Solution:
    def maxDepth(self, root):
        if not root: return 0
        queue = []
        queue.append(root)
        level = 0

        while queue:
            level += 1
            num = len(queue)
            for i in range(num):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return level


#(3)深度优先搜索：

class Solution:
    def maxDepth(self, root):
        if not root: return 0

        self.max_level = 1
        self._dfs(root, 1)
        return self.max_level

    def _dfs(self, node, level):
        if not node: return
        if level > self.max_level: self.max_level = level

        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)
