class Solution:
    def maxAbsValExpr(self, arr1, arr2) :
        d1={}
        d2={}
        d1['min1']=[0,arr1[0]]
        d2['min2']=[0,arr2[0]]

        for i in range(1,len(arr1)):
            if arr1[i]<d1['min1'][1]:
                d1['min1']=[i,arr1[i]]
                arr1[i]=float('-inf')
            else:
                arr1[i]=arr1[i]-d1['min1'][1]
                d1[i]=(d1['min1'][0])
            if arr2[i] < d2['min1'][1]:
                d2['min1'] = [i, arr2[i]]
                arr2[i] = float('-inf')
            else:
                arr2[i] = arr2[i] - d2['min1'][1]
                d2[i] = (d2['min1'][0])

