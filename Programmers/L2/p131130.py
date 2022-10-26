def gets(a, cards, i):
    if a[i]!=0:
        if(a[cards[i]]!=0 and i!=cards[i]):
            a[cards[i]] += a[i]
            a[i] = 0
            return gets(a, cards, cards[i])
    return a
def solution(cards):
    a = [1 for _ in range(len(cards)+1)]
    cards.insert(0,0)
    a[0] = 0
    for i in range(len(cards)):
        a = gets(a, cards, i)
    a.sort()
    return a[-1]*a[-2]
