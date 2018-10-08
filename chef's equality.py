def equality():
    t= int(raw_input())
    for j in range(t):
        n = int(raw_input())
        coins_pile = [int(i) for i in raw_input().split()]
        from collections import Counter
        coins_pile=Counter(coins_pile)
        max_count=max(coins_pile.itervalues())
        print n-max_count


if __name__=="__main__":
    equality()