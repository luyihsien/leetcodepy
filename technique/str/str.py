#str.replace(old,new)#http://www.runoob.com/python/att-string-replace.html
a='123321123231'
if '1' in a:#只一次判別#若要多次用for(計次) or while(條件)
    print('1')
#for '1' in a:#error 應是用一varible名去遍歷
#for i in a:
a.replace('1','').replace('2','').replace('3','')#default為不限次數替換，若有限制，小括號第三參數max輸入
b='123321123231'.replace('3','').replace('1','').replace('2','')

print(a)#為''空字串，看不出來
print(b)#同a
a=6
if a>5:
    print(5)
elif a>4:#即使是符合的，但因為a以符合大於5故就不再往下執行了vs if if 都會去執行 BUT若條件部分or全部互斥??(等同else或if elif else)則沒影響。若本身判別東西就是都符合則有影響
    print(4)
def a():
    for j in range(3):
        for i in range(2):
            print(i)
            if i==1:
                return False#有點像break 到這裡就停止<誤>會繼續因為while for未運行完而自下一項運行下去
                #return 只有def的函數可以用
a()