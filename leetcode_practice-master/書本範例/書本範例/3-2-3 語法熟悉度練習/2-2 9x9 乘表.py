for i in range(1,10):
    for j in range(1,10):
        print("%3d" %(i*j), end='')  # 不換行，跟著印
    print(end='\n') # 換行
