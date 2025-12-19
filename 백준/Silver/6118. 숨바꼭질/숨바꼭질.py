from collections import deque

N, M = map(int,input().split())
farms = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    farms[u].append(v)
    farms[v].append(u)

start = 1
dist = [-1] * (N+1)
q = deque([start])
dist[1] = 0

while q:
    node = q.popleft()
    for next_node in farms[node]:
        if dist[next_node] == -1:
            dist[next_node] = dist[node] + 1
            q.append(next_node)

ans = []
max_v = 0
for i in range(1,N+1):
    if dist[i] > max_v:
        max_v = dist[i]
        ans = [i]
    elif dist[i] == max_v:
        ans.append(i)
print(min(ans), max_v, len(ans))