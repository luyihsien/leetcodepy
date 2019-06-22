record=[]
nums=[1,2,3,2,1]
n=len(nums)-1
print(n)
while n > 0:
    print('入while')
    print('nums[n]','nums[n-1]',nums[n],nums[n-1])
    if nums[n] > nums[n - 1]:
        k = 0
        record.append(nums[n])
        print('record k',record[k])