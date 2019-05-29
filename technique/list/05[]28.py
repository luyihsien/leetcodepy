a=[1,2,3,4]
print(a)
a[:]=[4,3,2,1]
print(a)
b=a[:]
b=[1,2,3,4]
print(b)
print(a)
'''
print(a)
print(b)
b=a[:]
a.remove(4)
print(b)
b.remove(3)
print(a)
c=a[:].remove(3)
print(a)
print(c)#None
'''
'''
https://www.zhihu.com/question/54282837
https://stackoverflow.com/questions/39241529/what-is-the-meaning-of-in-python
[:] is the array slice syntax for every element in the array.

This answer here goes more in depth of the general uses: Explain Python's slice notation

del arr # Deletes the array itself
del arr[:]  # Deletes all the elements in the array
del arr[2]  # Deletes the second element in the array
del arr[1:]  # etc..
'''