N = int(input())
cards = []
cnt_v = {}
for _ in range(N):
    cards.append(int(input()))


for card in cards:
    cnt_v[card] = cnt_v.get(card,0) + 1


ans = []
max_cnt = 0
for num, cnt in cnt_v.items():

    if cnt > max_cnt:
        if ans:
            ans.clear()
            ans.append(num)
            max_cnt = cnt
        else:
            ans.append(num)
            max_cnt = cnt
    elif cnt == max_cnt:
        ans.append(num)
        max_cnt = cnt
    else:
        continue

ans.sort()
print(ans[0])