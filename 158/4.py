import collections
c=collections.Counter()
c[2]+=1
print(c)
from collections import namedtuple

Friend = namedtuple("Friend", ['name', 'age', 'email'])

f1 = Friend('xiaowang', 33, 'xiaowang@163.com')
print(f1)
print(f1.age)
print(f1.email)
f2 = Friend(name='xiaozhang', email='xiaozhang@sina.com', age=30)
print(f2)

name, age, email = f2
print(name, age, email)