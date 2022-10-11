def printSeq(start, stop, step):
    for i in range(start, stop, step):
        print(i, end=' ')


def sumSeq(start, stop, step):
    s = 0
    for i in range(start, stop, step):
        s += i
    return s


printSeq(3, 20, 2)
print(f'\nsum = {sumSeq(3, 20, 2)}')
printSeq(4, 60, 7)
print(f'\nsum = {sumSeq(4, 60, 7)}')


