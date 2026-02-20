N = int(input())
liqs = list(map(int,input().split()))
liqs.sort()

left = 0
right = N-1
ans = liqs[left]+liqs[right]
while left < right:
    ans_v = liqs[left] + liqs[right]

    if abs(ans_v) < abs(ans):
        ans = ans_v
    if ans_v < 0:
        left += 1
    else:
        right -= 1

print(ans)
