str2='ABCABC'
str1 = "ABC"
for i in range(len(str2)-1):
    #print('str2[i]',str2[i])
    for j in range(i+1,len(str2)):
        #print('str2[i:j]',str2[i:j+1])
        #print('replace完',str2.replace(str2[i:j+1]
        if str2.replace(str2[i:j+1],'')=='' and str1.replace(str2[i:j+1],'')=='':
            a=str2[i:j+1]
    
'''
for i in range(len(str1)-1):
    #print('str2[i]',str1[i])
    for j in range(i+1,len(str1)):
        #print('str2[i:j]',str2[i:j+1])
        #print('replace完',str2.replace(str2[i:j+1]
        if str1.replace(str1[i:j+1],'')=='':
            b=str1[i:j+1]
'''