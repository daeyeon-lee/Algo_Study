N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))


nums.sort()

start = 0
end = 0
best = 0
while start < N:
    while end < N and nums[end] - nums[start] < 5:
        end += 1
    best = max(best, end-start) # 지금까지의 크기를 최대값으로 기록
    start += 1 # 오른쪽으로 한칸 밀어서 다음 경우의 수
print(5- best)