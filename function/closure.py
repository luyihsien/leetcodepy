#https://www.youtube.com/watch?v=gwetZc-7Gg4&list=PLNTlJhYDV6sN8cH0bgaaVwsoF7EVHD_R6&index=16
#參考program diary->pretest2hr->part1 counting.py
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
class Solution():
    def counting(self,urls):
        dict = {}
        '''
        for i in range(len(urls)):
            urls[i]=urls[i].split('/',-1)[-1]#能切割'/'的最多次數的最後一項
        '''
        for i in urls:
            i = i.split('/', -1)[-1]  # i.split('/',-1)[-1]若不賦值給i，那就只是切在這個字串上，沒有改變i
            # print(i)
            # for i in urls:
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
            return self.sortedDictValues3(dict)  # {'a.txt': 1}#NameError: name 'sortedDictValues3' is not defined

    def sortedDictValue(self,dict):
        print(dict)
if __name__ == '__main__':
    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]

print(Solution.counting(urls))