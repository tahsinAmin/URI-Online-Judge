while True:
    deck1, deck2 = input().split()
    if deck1 == deck2 == '0':
        break
    cards1 = [int(i) for i in input().split()]
    cards2 = [int(i) for i in input().split()]

    otherSet = set(cards2)
    smallSet = set(cards1)

    if len(otherSet) < len(smallSet):
        otherSet, smallSet = smallSet, otherSet

    cList = [x for x in smallSet if x not in otherSet]
    print(len(cList))
