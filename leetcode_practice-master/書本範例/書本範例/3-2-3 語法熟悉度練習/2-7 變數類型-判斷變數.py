list = ['Jerome', 0.38, 1234, True] 
for i in range(0, len(list)):
    print (list[i],type(list[i]))

print ('變數是string的有：')
for i in range(0,len(list)):
    # 變數的 class 類型判斷，可以用 isinstance()
    if isinstance(list[i], str):
        print (list[i], type(list[i])) 
