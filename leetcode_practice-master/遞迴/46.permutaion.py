class Solution:#是在計算可能數，不是數量#數量固定就是n個
    def permutation(self,nums):
        if len(nums)<=1:#len必大於等於0
            return [nums]
        else:
            res=[]
            for i,j in enumerate(nums):
                n=nums[:i]+nums[i+1:]
                for k in self.permutation(n):
                    res.append([j]+k)
            return res
print(Solution().permutation([1,2,3]))