a=[2,5,10,9]
for i in a:
    print(i)#2 5 9 10
'''
for i in len(a):#TypeError: 'int' object is not iterable
    print(i)
    print(a[i])
'''
for i in range(len(a)):
    print(i)
    print(a[i])
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            if nums[i] not in a:
                a[target-nums[i]]=i
            else:
                return [a[i],i]
'''
class Solution:#盡量第一個字要大寫#class Sol()==class Sol
    #nums=[2,7,11,15]
    #target=9
    def twoSum(self, nums, target):#self在pycharm直接自動給#他依然是一個參數，但是是不用指名的參數#透過實體操作#對象呼叫後可看作一個函數
        # self==Solution()跟__init__無關，皆要Solution()
        a={}
        for i in range(len(nums)):#比較range(nums)#依然保有同樣len但又有了座標能力(從0始)#跑一次座標
            #if nums[i] not in a:#key error
            if target-nums[i] not in a:#預設找key非value#有key i 才會有value a[i]
                a[nums[i]]=i#需要i座標故如此做，故沒有用for i in nums
                #a[target-nums[i]]=i#並不是找相同的 而是找差符合的
            else:
                return [a[target-nums[i]],i]#此時的i已非當初的i#若無符合則回傳None非error
print(Solution().twoSum([2,7,11,15],10))#Solution.twoSum(....)會報錯
class b:
    x=3
    def a(self,nums,target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
print(b().a([2,10,9,5],5))#回傳3#若target=4則None

b.x=4
c=b()
print(c.x)#4

class c:
    print('c')
print(c)#<class '__main__.c'>#集合
print(c())#<__main__.c object at 0x000001B99684DEF0>#集合模子印出的對象
def d():
    print('d')
print(d())#d
          #None