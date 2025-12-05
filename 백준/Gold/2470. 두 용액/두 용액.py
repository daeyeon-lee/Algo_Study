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
    if abs(liq[left] + liq[right] - 0) <= min_v:
        min_v = abs(liq[left] + liq[right] - 0)
        ans_left = liq[left]
        ans_right = liq[right]
        if abs(liq[left]) > abs(liq[right]):
            left += 1
        else:
            right -= 1

    elif abs(liq[left] + liq[right] - 0) > min_v:
        if abs(liq[left]) > abs(liq[right]):
            left += 1
        else:
            right -= 1

ans = []
ans.append(ans_left)
ans.append(ans_right)
ans.sort()
print(*ans)