class Solution():
    def counting(self,urls):
        def sortedDictValue(self, dict):
            return dict
        dict = {}
        '''
        for i in range(len(urls)):
            urls[i]=urls[i].split('/',-1)[-1]#能切割'/'的最多次數的最後一項
        '''
        for i in urls:
            i = i.split('/', -1)[-1]# i.split('/',-1)[-1]若不賦值給i，那就只是切在這個字串上，沒有改變i
            print(i)
            # for i in urls:
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
            return self.sortedDictValues3(dict)  # {'a.txt': 1}#NameError: name 'sortedDictValues3' is not defined

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
print(Solution().counting(urls))