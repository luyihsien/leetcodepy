#append(新值)與pop()即是stack後進先出的運用
print(list(range(3)))#list(range(負數))會是空list 即[]
a=['123',1,'123',2,3,4,5,'123']
a.remove('123')
print(a)#從最前面的一個開始remove
for i in a:
    b=a.pop()
    print('pop出去'+str(i))
    print(i)
    print(a)
'''
[1, '123', 2, 3, 4, 5, '123']
pop出去1
1
[1, '123', 2, 3, 4, 5]
pop出去123
123
[1, '123', 2, 3, 4]
pop出去2
2
[1, '123', 2, 3]
pop出去3
3
[1, '123', 2]

'''