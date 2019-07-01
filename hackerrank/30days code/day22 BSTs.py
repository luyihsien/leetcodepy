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
                print('cur=self.insert(root.left,data)')
                cur=self.insert(root.left,data)
                global c
                c=c+1
                print('c',c)
                if root.right==None:
                    print('None')
                else:
                    print('root.right=cur',(root.right).data)
                if cur==None:
                    print('cur',None)
                else:
                    print('cur',cur.data)
            else:
                print('cur=self.insert(root.right,data)')
                cur=self.insert(root.right,data)
                if root.left==None:
                    print('None')
                else:
                    print('root.left=cur',(root.left).data)
                #global c#SyntaxError: name 'c' is used prior to global declaration
                c=c+1
                print('c',c)
                root.right=cur
                if cur==None:
                    print('cur',None)
                else:
                    print('cur',cur.data)
        return root
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())#data此名字在此之前都沒出現過
    root=myTree.insert(root,data)

