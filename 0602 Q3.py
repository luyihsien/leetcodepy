lass Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = [0] * 2000
        n1 = len(arr1)
        n2 = len(arr2)
        for i, x in enumerate(arr1):
            actual = n1 - i - 1
            if x: count[actual] += 1
        for i, x in enumerate(arr2):
            actual = n2 - i - 1
            if x: count[actual] += 1
        for i in range(1500):
            while count[i] > 1:
                if count[i + 1]:
                    count[i] -= 2
                    count[i + 1] -= 1
                else:
                    count[i] -= 2
                    count[i + 1] += 1
                    count[i + 2] += 1
        count.reverse()
        if 1 not in count: return [0]
        return count[count.index(1):]
