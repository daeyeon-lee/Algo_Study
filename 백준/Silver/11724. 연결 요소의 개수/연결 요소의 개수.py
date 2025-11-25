from collections import deque
import sys
input = sys.stdin.readline
q = deque()
N, M = map(int,input().split())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()
        for next_node in arr[node]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True

cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)