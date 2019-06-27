c=0
class Sol:
    def per(self,nums):
        global c
        c=c+1
        print('第{}次呼叫per(nums)'.format(c))
        if len(nums)<=1:
            print('return執行完第{}次的遞迴'.format(c),[nums])
            return [nums]
        ans=[]
        for i,num in enumerate(nums):
            n=nums[:i]+nums[i+1:]#將餵進的nums取出來#error nums[i+1]#2個以上始進入此for
            print('固定住{}把n={}餵進self.per(nums)的nums'.format([num],n))
            for y in self.per(n):#把self.per(n)本身一個看成一個list#return了ans至self.per(n) 但其ans依然=[]
                print('[num]',[num])
                print('y',y)#遞迴在跑的是y
                ans.append([num]+y)#[ ]內加上[num]+y
                print('ans',ans)
        print('ans return',ans)
        return ans#誤以為只有這個回去的可能，其實還有上方的return [nums]
print(Sol().per([1,2,3,4]))
'''
好比
c=0
c=c+1
print(c)#1
c=c+1
print(c)#2
只是今天是呼叫函數有次序的去調用更改掉值
'''
