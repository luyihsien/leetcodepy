class Solution:
    def countSteppingNumbers(self, low: int, high: int):
        l=[]
        for i in range(low,high+1):
            f=True
            for j in range(len(str(i))-1):

                if abs(int(str(i)[j])-int(str(i)[j+1]))!=1:
                    f=False
                    break
            if f==True:
                l.append(i)
        return l
print(Solution().countSteppingNumbers(0,21))