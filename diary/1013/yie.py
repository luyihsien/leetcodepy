x=1
def a():
    global x
    yield x
    x+=1
for j in range(3):
    for i in a():
        print(i)