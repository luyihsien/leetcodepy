class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        tree=[[1]]
        d=cur=num=1
        while cur<label:
            num*=2
            d=(d+1)%2
            new=list(range(cur+1,cur+num+1))
            cur+=num
            if d:
                tree.append(new)
            else:
                tree.append(new[::-1])
        path=[]
        curid=tree[-1].index(label)
        for rowid in range(len(tree)-1,-1,-1):
            path.append(tree[rowid][curid])
            curid/=2
        return path[::-1]
#print(Solution().pathInZigZagTree(14))
#世界第四名#luxcaelestis
#https://zhuanlan.zhihu.com/p/28018082
def transname (num):
    if num == 0:
        return 0
    else:
        print('bin(num)',bin(num))
        bits = len (bin (num)) - 2#得最高位數，與幾個0幾個1無關
        print('bits',bits)
        if bits % 2 == 1:
            print('num',num)
            return num
        else:#bits%2==0
            #print('num ^ ((1 << (bits - 1)) - 1)',num ^ ((1 << (bits - 1)) - 1))
            #return num ^ ((1 << (bits - 1)) - 1)
            return num^((1<<(bits-1))-1)
class Solution:
    def pathInZigZagTree(self, label):
        realname = transname (label)
        ans = []
        while realname > 0:
            ans.append (realname)
            print('ans append後',ans)
            #realname >>= 1
            realname//=2
            print('realname',realname)
        ans = ans[::-1]
        print('ans',ans)
        ans = [transname (x) for x in ans]
        print('ans',ans)
        return ans
print(Solution().pathInZigZagTree(14))
#ans[1,2,4,9]為正常排列
#print(2<<4)
#print(0b11==3)
#print(bin(10),len(bin(10)))
#http://www.runoob.com/python/python-func-bin.html
print(1<<(2-1)-1)
print(6^9)
print(6&9)
print(~1)
print(3>>1)#1