#import a會import不到<誤>以為interpreter壞掉路徑搜尋壞掉或不同資夾，其實正確是按照系統路徑之下從flweb始去找 故之前要先import testss
'''
from testss.a import a
def b():
    print('b')
'''
from testss import a
