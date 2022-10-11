import re
f = open('poem',encoding = 'utf-8')
t = f.read()

word = re.findall(r'[\w-]+', t)
uniq = []
for i in range(len(word)):
   word[i] = word[i].lower()
   if word[i] not in uniq:
      uniq.append(word[i])
print(' '.join(uniq))
