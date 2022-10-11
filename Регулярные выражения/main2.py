# findall() находит все подстроки, удовлетворяющие выражению
import re

text = 'aaa bbbb 123 548 666 ccc d2d 6 dsr'

print(re.findall(r'\b\d+\b', text))

'''
kls 456 +79819862513
89819862513 654
178945612345 +7(981)986-25-13 fs fsf
62651615165 +7 981 986 25 13  efwf w
'''