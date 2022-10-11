def Encode(text, key):
    alph = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for i in range(len(text)):
        pos = alph.find(text[i])
        if pos != -1:
            res += alph[(pos + key) % len(alph)]
        else:
            res += text[i]
    return res


def Decode(text, key):
    alph = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for i in range(len(text)):
        pos = alph.find(text[i])
        if pos != -1:
            res += alph[(len(alph) + pos - key) % len(alph)]
        else:
            res += text[i]
    return res

print(Decode("khoor", 3))