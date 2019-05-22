s='123'
a=s.replace('1','3')
print(a)#換1變成3 #323
print(s)#依然123
s='123123123'
b=s.replace('12','3',2)#只換兩次#不代表換了原本的str，因為str不能換內部元素
a=s.replace('1','3')
print(s)
print(a)
print(b)