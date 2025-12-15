S = input()

cnt_v = {}

for letter in S:
    cnt_v[letter] = cnt_v.get(letter,0) + 1


ans = ''
sorted_cnt = sorted(cnt_v.items())

for num, cnt in sorted_cnt:
    ans += num * (int(cnt) // 2)
print(ans)