def fixLayout(str):
    en = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
    ru = "йцукенгшщзхъфывапролджэячсмитьбю."
    res = ""
    for i in range(len(str)):
        pos = en.find(str[i])
        if pos != -1:
            res += ru[pos]
        else:
            pos = ru.find(str[i])
            if pos != -1:
                res += en[pos]
            else:
                res += str[i]
    return res

print(fixLayout('d%sk fh jkjао*вр'))