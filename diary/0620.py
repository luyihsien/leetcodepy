class Rectangle:
    def __init__(self,length,width):
        if length<=0 or width<=0:
            raise ValueError('length and width should be positive or zero')
        self.length=length
        self.width=width
    def perimeter(self):
        return 2*(self.length+self.width)
    def area(self):
        return self.length*self.width
rec=Rectangle(4,2)
print(rec.area())
rec.width=-4
print(rec.area())#-16#以上指保護了物件始值，未保護物件更動後
