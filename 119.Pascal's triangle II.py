'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
'''
class Solution:
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        else:
            a=[1,1]
            for i in range(rowIndex-1):
                a.insert(i+1,a[i]+a[i+1])
            return a
'''
題解->編程學徒
python3的两种解法

法1：根据组合数公式n!/(i!*(n-i)!)计算

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 法1：根据组合数公式n!/(i!*(n-i)!)计算
        if rowIndex < 0:
            return []
        factorials = [1]*(rowIndex+1) 
        ans = [1]*(rowIndex+1)
        for i in range(1, rowIndex+1):
            factorials[i] = factorials[i-1]*i # 0!~rowIndex!
        # print(factorials)
        for i in range(rowIndex): # 根据组合数公式计算n!/(i!*(n-i)!)
            ans[i] = factorials[-1]//(factorials[i]*factorials[rowIndex-i])
        return ans
法2：根据组合数公式C(n,i)=n!/(i!*(n-i)!)直接由C(n,i)算C(n,i+1),后者是前者的(n-i)/(i+1)倍

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 法2：根据组合数公式C(n,i)=n!/(i!*(n-i)!)直接由C(n,i)算C(n,i+1),后者是前者的(n-i)/(i+1)倍
        if rowIndex < 0:
            return []
        ans = [1]*(rowIndex+1)
        for i in range(rowIndex):
            ans[i+1] = ans[i]*(rowIndex-i)//(i+1)
        return ans
作者：bian-cheng-xue-tu
链接：https://leetcode-cn.com/problems/two-sum/solution/119yang-hui-san-jiao-2de-python3he-cjie-fa-by-bian/
来源：力扣（LeetCode）
'''
class Solution:
    def getRow(self, rowIndex):
        # 法1：根据组合数公式n!/(i!*(n-i)!)计算
        if rowIndex < 0:
            return []
        factorials = [1]*(rowIndex+1)#當3時 則[1,1,1,1]
        print(factorials)
        ans = [1]*(rowIndex+1)
        print(ans)
        for i in range(1, rowIndex+1):
            factorials[i] = factorials[i-1]*i# 0!與1!~rowIndex!
            print(factorials[i])
        print(factorials)#當3時 [1,1,2,6]
        # print(factorials)
        for i in range(rowIndex): # 根据组合数公式计算n!(分子已固定)/(i!*(n-i)!)(分母變動)
            ans[i] = factorials[-1]//(factorials[i]*factorials[rowIndex-i])
        return ans
print(Solution().getRow(3))
print(4/2)#整數相除因通常有小數點，故預設
print(4/4)