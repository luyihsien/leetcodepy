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
