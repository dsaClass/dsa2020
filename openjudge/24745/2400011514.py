    pA = a.head
    pB = b.head
    while pA != pB:
        pA = pA.next if pA else b.head
        pB = pB.next if pB else a.head
    return pA.data