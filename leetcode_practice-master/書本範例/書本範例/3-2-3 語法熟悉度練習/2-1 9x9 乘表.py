for i in range(1,10):
    for j in range(1,10):
        # 換行，若要不換行要改成 print(i*j, end=' ')
        if (i*j <10 ):
            print(' ',end='')
        print(i*j,end=' ')
    print()
