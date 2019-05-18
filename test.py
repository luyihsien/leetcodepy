while 0 and a:#Linked List Cycle
    print(1)
print(0)
#輸出而沒出現未定義的error
#故知根本沒去判a 故即使a未定義而其實會錯也沒報錯
a={1:'2',3:'4'}
if 1 in a:#for i in a亦同#https://www.youtube.com/watch?v=CjYKrbq8BCw#驗的是key不是整塊或value
    print('key is'+'\t' +str(1)+'\t'+"value is"+a[1])
def b():#函數可以沒參數
    print('b')
b()
class A:
    a=4
    def b():
        print('b')#method不能沒有參數print('b')
#內部即使有錯，在未呼叫執行時亦未即時出現error
A.b()
A().b()#實體屬性不能用，but class屬性能#猜可能是怕訂同樣會有衝突
#一旦錯了就不再向下執行直議程式
'''
myList = []
for i in range(10):
    myList.append(i)
is equivalent to

myList = [i for i in range(10)]#總要跟[i in range(10)]不一樣吧
'''
'''
http post與get差異
https://blog.toright.com/posts/1203/%E6%B7%BA%E8%AB%87-http-method%EF%BC%9A%E8%A1%A8%E5%96%AE%E4%B8%AD%E7%9A%84-get-%E8%88%87-post-%E6%9C%89%E4%BB%80%E9%BA%BC%E5%B7%AE%E5%88%A5%EF%BC%9F.html
'''
'''
00:03:15
https://www.youtube.com/watch?v=GVQBN46pa58&list=PLXfTLiJIRszzVJ6ZLHTK0bWb1cw_LrhjH&index=8
'''