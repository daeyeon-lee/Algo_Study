N = int(input())
nums = list(map(int,input().split()))
M = int(input())
sum_v = [0] * (N+1)
for i in range(N):
    sum_v[i+1] = nums[i] + sum_v[i]

for _ in range(M):
    i, j = map(int,input().split())
    print(sum_v[j]-sum_v[i-1])