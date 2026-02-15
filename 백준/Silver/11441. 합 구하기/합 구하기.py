import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
M = int(input())
sum_v = [0] * (N+1)
for i in range(N):
    sum_v[i+1] = nums[i] + sum_v[i]
ans = []
for _ in range(M):
    i, j = map(int,input().split())
    ans.append(sum_v[j]-sum_v[i-1])
print('\n'.join(map(str,ans)))