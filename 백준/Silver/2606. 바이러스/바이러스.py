from collections import deque

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    u, v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)
# print(arr)

q = deque()
q.append(1)
visited[1] = True
cnt = 0
while q:
    r = q.popleft()
    for nr in arr[r]:
        if visited[nr] == False:
            q.append(nr)
            visited[nr] = True
            cnt += 1

print(cnt)



