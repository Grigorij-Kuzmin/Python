import re
f = open('input.txt')
text = f.read()

numbers = re.findall(r'((\+7|8)(\s|\()?\d{3}(\s|\))?\d{3}( |-)?\d{2}(\s|-)?\d{2})',text)
for i in range(len(numbers)):
    print(numbers[i][0])
