#1050305-12

def f1(m):
    if (m>3):
        print("%d\n"  %m)
        return
    else:
        print("%d\n"  %m)
        f2(m+2)
        print("%d\n"  %m)

def f2(n):
    if (n>3):
        print("%d\n"  %n)
        return
    else:
        print("%d\n"  %n)
        f1(n-1)
        print("%d\n"  %n)

#main
f1(1)

