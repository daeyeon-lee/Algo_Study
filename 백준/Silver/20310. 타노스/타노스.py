import sys
S = sys.stdin.readline().strip()


cnt_v = {}

for letter in S:
    cnt_v[letter] = cnt_v.get(letter,0) + 1

# 0인 경우엔 0으로
remove_1 = cnt_v.get('1',0) // 2
remove_0 = cnt_v.get('0',0) // 2


temp = []

# 앞에서부터 1 절반 제거
for l in S:
    if l == '1' and remove_1 > 0:
        remove_1 -= 1
        continue
    else:
        temp.append(l)

ans = []
# 뒤에서부터 0 절반 제거
for l in reversed(temp):
    if l == '0' and remove_0 > 0:
        remove_0 -= 1
        continue
    else:
        ans.append(l)


print(''.join(reversed(ans)))
