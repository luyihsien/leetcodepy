def test(number):
    def test_in(number_in):
        print('in test_in 函數,number_in is %d',number_in)
        return number+number_in
    return test_in
ret=test(20)#不印東西，傳了20
print(ret(100))
print(ret(200))
'''
結果
in test_in 函數,number_in is %d 100
120
in test_in 函數,number_in is %d 200
220
'''