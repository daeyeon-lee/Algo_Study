import sys
import heapq
input = sys.stdin.readline

N = int(input())
ans = []

for _ in range(N):
    arr = list(map(int,input().split()))
    for i in arr:
        if len(ans) < N:
            heapq.heappush(ans,i)
        else:
            if i > ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans,i)
print(ans[0])