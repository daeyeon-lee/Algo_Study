from collections import deque
import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
dist = [0] * (N+1)
for _ in range(M):
    u,v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)
for i in range(1,N+1):
    arr[i].sort(reverse=True) # 오름차순


q = deque()
q.append(R)
visited[R] = True
cnt = 1
dist[R] = 1

while q:
    node = q.popleft()
    for next_node in arr[node]:
        if not visited[next_node]:
            visited[next_node] = True
            cnt += 1
            dist[next_node] = cnt
            q.append(next_node)
for i in range(1,N+1):
    print(dist[i])
