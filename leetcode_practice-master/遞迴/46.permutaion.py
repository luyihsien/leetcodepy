class Solution:#是在計算可能數，不是數量#數量固定就是n個
    def permutation(self,nums):
        if len(nums)<=1:#len必大於等於0
            return [nums]
        else:
            res=[]
            for i,j in enumerate(nums):
                n=nums[:i]+nums[i+1:]#n*O(1)=O(n)
                for k in self.permutation(n):#n*T(n-1)#n源自於for i,j in enumerate(nums):
                    res.append([j]+k)
            return res
print(Solution().permutation([1,2,3]))
#https://stackoverflow.com/questions/5363619/complexity-of-recursive-string-permutation-function
#T(n) = n*T(n-1) + O(n)