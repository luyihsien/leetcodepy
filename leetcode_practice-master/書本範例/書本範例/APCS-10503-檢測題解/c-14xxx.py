#1050305-14

def foo(i):
    if (i <= 5):
        print("foo:  %d\n"  %i)
    else:
        bar(i-10)

def bar(i):
    if (i <= 10):
        print("bar:  %d\n"  %i)
    else:
        foo(i-5)

#main
foo(15106)
bar(3091)
foo(6693)



