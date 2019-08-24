a=[]
c=4
def b():
    a.append(4)
    #c+=1
    print(a)
b()
print(a)
class A():
    def a(self):
        c=4
        def b():
            c=c+1
            print(c)
        b()
A().a()