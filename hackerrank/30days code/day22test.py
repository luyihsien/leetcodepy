class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data=data
root=Node(1)
print('root',root)
print(root.data,root.left,root.right)
root.left=Node(2)#放一個超級大數ex:2X10^(200)，記憶體位置也一樣
print('root',root)
print(root.data,root.left.data,root.right)



