class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n=[]
        for i in range(1,numRows+1):#range(numRows)0至n-1非1至n導致[]導致index超過
            a=[0]*i
            a[0]=a[-1]=1
            n.append(a)
        #print(n)
        for i in range(2,len(n)):
            for j in range(len(n[i-1])-1):
                n[i][j+1]=n[i-1][j]+n[i-1][j+1]
        print(n)
        return n
Solution().generate(5)
