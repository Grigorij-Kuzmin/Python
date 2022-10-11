import re
f = open('input.txt')
t = f.read()
f = open('nasty.txt')
nasty = f.readlines()
for i in range(len(nasty)):
    t = re.sub(nasty[i], nasty[i][0] + ('*'*(len(nasty[i]) - 2)) + nasty[i][len(nasty[i]) - 1], t)
print(t)