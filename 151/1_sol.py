class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        res = []

        for i in transactions:
            name, time, amount, city = i.split(',')

            amount = int(amount)
            time = int(time)

            if amount > 1000:
                res.append(i)
                continue

            invalid = False

            for j in transactions:
                name2, time2, amount2, city2 = j.split(',')
                if name2 != name: continue
                time2 = int(time2)
                if city2 != city and abs(time2 - time) <= 60:
                    invalid = True
                    break
            if invalid: res.append(i)
        return res
