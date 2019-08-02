#https://gist.github.com/m00nlight/daa6786cc503fde12a77
class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            print('剛入range後i',i)
            j = ret[i - 1]
            print('j',j)
            while j > 0 and pattern[j] != pattern[i]:
                print('j',j)
                j = ret[j - 1]
                print('while j > 0 and pattern[j] != pattern[i]:時j ',j)
            print('i','j',i,j)
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
            print('ret',ret)
        return ret

    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0
        print('partial,ret,j',partial,ret,j)

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
                print('while j > 0 and T[i] != P[j]:下 j',j)
            if T[i] == P[j]:
                j += 1
                print('滿足T[i] == P[j]時j',j)
            if j == len(P):
                ret.append(i - (j - 1))
                print('j == len(P):下ret.append後ret',ret)
                j = partial[j - 1]
                print('j',j)

        return ret

kmp=KMP()
print('kmp',kmp.search('aaaaaa','aa'))
print('kmp',kmp.search('aaabcaaaabca','abca'))
print('kmp',kmp.search('aaabacaaaababaaababca','abab'))
print('kmp',kmp.search('aaabacaaaababaaababca','abaa'))#有執行到下
print('partial',kmp.partial('abababca'))