#https://zhuanlan.zhihu.com/p/41047378
def KMP(s, p):
    """
    s为主串
    p为模式串
    如果t里有p，返回打头下标
    """
    nex = getNext(p)
    i = j = 0  # 分别是s和p的指针
    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]:  # j==-1是由于j=next[j]产生
            i += 1
            j += 1
        else:
            j = nex[j]

    if j == len(p):  # 匹配到了
        return i - j
    else:
        return -1


def getNext(p):
    """
    p为模式串
    返回next数组，即部分匹配表
    等同于从模式字符串的第1位(注意，不包括第0位)开始对自身进行匹配运算。
    """
    nex = [0] * len(p)
    nex[0] = -1
    i = 0
    j = -1
    while i < len(p) - 1:  # len(p)-1防止越界，因为nex前面插入了-1
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            nex[i] = j  # 这是最大的不同：记录next[i]
            print('nex',nex)
        else:
            j = nex[j]
    return nex


s = 'aaaaaaaaaaaaaaaaaaaaaaa'
p = 'a'
print(getNext(p))
print(KMP(s, p))