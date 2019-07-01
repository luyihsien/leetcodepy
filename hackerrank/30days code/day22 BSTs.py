
c=0
class Node:
    global c
    def __init__(self,data):
        self.right=self.left=None
        self.data=data
class Solution:
    def insert(self,root,data):
        #global c 加在這無效
        if root==None:
            print('data',data)
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                print('cur=self.insert(root.right,data)')
                cur=self.insert(root.right,data)
                root.right=cur
        return root
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())#data此名字在此之前都沒出現過
    root=myTree.insert(root,data)
print('root.data',root.data)#3
print('root.right',root.right.data)#5
print('root.right.right',(root.right.right).data)#6
print(root.left)#
print('root.left',root.left.data)#2

#AttributeError: 'NoneType' object has no attribute 'data'
#print((root.left).data,((root.left).left).data)



'''
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
#print((myTree.left).value,((myTree.left).left).value)#AttributeError: 'Solution' object has no attribute 'left'
print(root.data)
print('root.data',root.data)#7
print('root.right',root.right.data)#AttributeError: 'NoneType' object has no attribute 'data'
print('root.right.righ',(root.right.right).data)#6
#print(root.left.data)#AttributeError: 'NoneType' object has no attribute 'data'
#print((root.left).data,((root.left).left).data)
'''