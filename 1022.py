'''
def a(acc):
    if acc>=20:
        acc=acc+1
    a(acc)
    a(acc)
print(a(1))#不會停止
#RecursionError: maximum recursion depth exceeded while calling a Python object
'''

'''
def a(x):
    x=x+1
    if x==5:
        return
    print(x)
    a(x)
    a(x)
a(1)
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Sol:
    ans = 0
    def sumt(self,root):
        def dfs(node,acc):
            if node is not None:
                acc=acc*2+node.val
                if node.left is None and node.right is None:
                    self.ans+=acc
                dfs(node.left,acc)
                dfs(node.right,acc)
        dfs(root,0)
        return self.ans
        #return self.ans

root=TreeNode(1)
root.left=TreeNode(0)
root.right=TreeNode(1)
root.left.left=TreeNode(0)
root.left.right=TreeNode(1)
root.right.left=TreeNode(0)
root.right.right=TreeNode(1)

print(Sol().sumt(root))


