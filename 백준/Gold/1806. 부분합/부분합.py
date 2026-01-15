N, S = map(int,input().split())
nums = list(map(int,input().split()))


left = 0
right = 0
sum_v = 0
ans = 2e21

while left < N:
    if sum_v >= S:
        ans = min(ans, right-left)
        sum_v -= nums[left]
        left += 1
    else:
        if right == N:
            break
        sum_v += nums[right]
        right += 1

if ans == 2e21:
    print(0)
else:
    print(ans)