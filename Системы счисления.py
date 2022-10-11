def tobase(number, base):
    res = ""
    alph = "0123456789abcdefghijklmnopqrstuvwxyz"
    while number > 0:
        res += alph[number % base]
        number = number // base
    return res[::-1]

print(tobase(314, 2))

