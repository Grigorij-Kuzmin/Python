num = [1, 2, 3, 4, 5, 6]
def ShiftLeft(arr):
    return arr[1:] + arr[:1]
#print(ShiftLeft(num))
#print(num[:1])



def ShiftRight(arr):
    return arr[-1:] + arr[:-1]
#print(ShiftRight(num))


def Reverse(arr):
    return num[::-1]
print(Reverse(num))