def solve(n):
    cards = [False] * n
    for i in range(2, n+1):
        for j in range(i-1, n, i):#座標1-100在list上是0-99
            cards[j]  = not cards[j]
            print(cards)

    ans = []
    for i in range(n):
        if not cards[i]:
            ans.append(i+1)
            print(ans)

    return ans

ans = solve(100)
print(ans)
