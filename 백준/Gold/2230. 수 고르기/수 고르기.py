N, M = map(int,input().split())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()

left = 0
right = 0
min_v = 2e21

while left < N and right < N:
    if abs(nums[left] - nums[right]) >= M:
        if abs(nums[left] - nums[right]) < min_v:
            min_v = abs(nums[left] - nums[right])
        left += 1
    else:
        right += 1
print(min_v)
