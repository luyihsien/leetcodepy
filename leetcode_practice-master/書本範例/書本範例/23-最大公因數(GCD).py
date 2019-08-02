# 求GCD (輾轉相除法)

# 可以試 ( x=546 , y=429 ) or (x=9 , y=24 ) or ( x=24 , y=56 ) 
x=24; y=56      

if (x>y):
    # 先比較二數，把比較大的數放在 Y 當被除數，x當除數
    x,y = y,x 
    
m=x; x=y
while(m>0):
    # 每運算過一次以後，就必須把除數 x 換成被除數，餘數當作除數
    y=x ; x=m ; m=y % x 

print('GCD=',x)


    
