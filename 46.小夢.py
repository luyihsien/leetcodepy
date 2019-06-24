c=0
class Sol:
    def per(self,nums):
        global c
        c=c+1
        print('nums', nums, '第{}次呼叫'.format(c))
        if len(nums)<=1:
            print('return執行完第{}次的遞迴'.format(c),[nums])
            return [nums]
        ans=[]
        for i,num in enumerate(nums):
            n=nums[:i]+nums[i+1:]#error nums[i+1]
            print('把n={}餵進self.per(n)'.format(n))
            for y in self.per(n):#把self.per(n)本身一個看成一個list
                print('[num]',[num])
                print('y',y)#遞迴在跑的是y
                ans.append([num]+y)
                print('ans',ans)
        print('ans return 執行完第{}次的遞迴'.format(c),ans)
        return ans#誤以為只有這個回去的可能，其實還有上方的return [nums]
print(Sol().per([1,2,3]))
