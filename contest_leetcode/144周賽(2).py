class Sol:
    def corp(self,bookings,n):
        a=[0]*n
        for i,j,k in bookings:
            a[i-1]+=k
            print('a',a,'a[i-1]', a[i - 1])
            if j<n:
                a[j]-=k
                print('a',a,'a[j]',a[j])
        print(a)
        seats=0
        for i in range(n):
            seats+=a[i]
            print('seats',seats)
            a[i]=seats
            print('a',a,'a[i]',a[i])
        return a
print(Sol().corp([[1,2,10],[2,3,20],[2,5,25]],5))
