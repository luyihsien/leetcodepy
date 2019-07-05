class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data=data
class Solution:
    def insert(self, root, data):
        if root==None:
            return Node(data)
        else:
            if data<root.data:
                self.insert(root.left,data)
            else:
                self.insert(root.right,data)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())#data此名字在此之前都沒出現過
    root=myTree.insert(root,data)
print(root.data,root.right,root.left)#7 None None
print(root.right.data)#AttributeError: 'NoneType' object has no attribute 'data'