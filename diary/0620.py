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
class Rectangle:
    def __init__(self,length,width):
        if length<=0 or width<=0:
            raise ValueError('length and width should be positive')
        self.__length=length
        self.__width=width
    def perimeter(self):
        return 2*(self.__length+self.__width)
    def area(self):
        return self.__length*self.__width
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self,length):
        if length<=0:
            raise ValueError('length and width should be positive or zero')
        self.__length=length

    @property
    def width(self):
        return self.__length

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('length and width should be positive or zero')
        self.__width =width
rec=Rectangle(4,2)
print(rec.area())
rec.width=10
print(rec.area(),'hi')#依然16#故知rec.__width與rec.width不同，此處誤把意思以為成多了一個新定義變數width(不是__width)其值為10，故area依舊去__width拿，依然是拿到2
rec.width=4
print(rec.area())
'''
Traceback (most recent call last):
-16
16
16
  File "C:/Users/luyih/Desktop/search_job/programmer diary/leeetcodepy/diary/0620.py", line 47, in <module>
    rec.width=-4
  File "C:/Users/luyih/Desktop/search_job/programmer diary/leeetcodepy/diary/0620.py", line 41, in width
    raise ValueError('length and width should be positive or zero')
ValueError: length and width should be positive or zero
'''