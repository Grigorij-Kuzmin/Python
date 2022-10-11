import re
f = open('text',encoding = 'utf-8')
t = f.read()

word = re.findall(r'[\w-]+', t)
print(word)