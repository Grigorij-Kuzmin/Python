import re
f = open('input.txt')
text = f.read()

print(re.findall(r'((\+7|8)(\s|\()?\d{3}(\s|\))?\d{3}( |-)?\d{2}(\s|-)?\d{2})',text))
