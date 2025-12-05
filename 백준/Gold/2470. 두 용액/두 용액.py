N = int(input())
liq = list(map(int,input().split()))
# print(liq)

liq.sort()
# print(liq)

left = 0
right = N-1
min_v= 2e21
ans_left = 0
ans_right = 0

while left < right:
    sum_v = liq[left] + liq[right]
    if abs(sum_v) < min_v:
        min_v = abs(sum_v)
        ans_left = liq[left]
        ans_right = liq[right]

    if sum_v < 0:
        left += 1
    else:
        right -= 1

ans = []
ans.append(ans_left)
ans.append(ans_right)
ans.sort()
print(*ans)