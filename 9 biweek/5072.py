class Solution:
    def maxNumberOfApples(self, arr) -> int:
        arr.sort()
        c=0
        num=0
        for i in arr:
            print('num',num)
            if num<5000:
                num+=i
                c+=1
                print('num',num,'c',c)
        return c
print(Solution().maxNumberOfApples(arr = [900,950,800,1000,700,800]))
class Solution:
    def maxNumberOfApples(self, arr) -> int:
        arr.sort()
        c=0
        arr=[0]+arr
        for i in range(len(arr)-1):
            if arr[i]+arr[i+1]<5000:
                c+=1
                arr[i+1]=arr[i]+arr[i+1]
            return c
print(Solution().maxNumberOfApples(arr = [900,950,800,1000,700,800]))