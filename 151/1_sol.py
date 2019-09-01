class Solution:
    def invalidTransactions(self, transactions):
        res = []
        for i in transactions:
            #print('i',i)
            name, time, amount, city = i.split(',')
            #print('name','amount','city',name,amount,city)
            amount = int(amount)
            time = int(time)
            if amount > 1000:
                res.append(i)
                continue
            invalid = False
            for j in transactions:
                print('j',j)
                name2, time2, amount2, city2 = j.split(',')
                print('name2','time2','amount2','city2',name2,time2,amount2,city2)
                if name2 != name: continue#名字不同不用擔心
                time2 = int(time2)
                if city2 != city and abs(time2 - time) <= 60:#若是比到自己，city2會等於city
                    invalid = True
                    break
            if invalid: res.append(i)
        return res
#print(Solution().invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,100,beijing"]))
#Q1169