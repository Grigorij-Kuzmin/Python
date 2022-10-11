import re
N = int(input())
ans = ''
r = r'[ABCEHKMOPTXY]\d{3}[ABCEHKMOPTXY]{2}'
for i in range(N):
    number = input()
    if len(number) != 6:
        ans += 'No\n'
        continue
    if re.match(r, number):
        ans += 'Yes\n'
    else:
        ans += 'No\n'
print(ans)
