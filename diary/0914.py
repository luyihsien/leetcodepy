class B:
    def a(self,n=5):
        if n>=0:
            print(n)
            self.a(n - 1)

B().a()

class C:
    a = 0
    def b(self,l=[]):
        if len(l)==10:
            return l
        l.append(self.a)
        print(l)
        self.a=self.a+1
        return self.b()

print(C().b())