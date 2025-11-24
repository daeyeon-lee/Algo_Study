from collections import deque

N, M, V = map(int,input().split())
arr = [[] for _ in range(N+1)]
visited_1 = [False] * (N+1)
visited_2 = [False] * (N+1)
for _ in range(M):
    u, v = map(int,input().split())
    # 양방향
    arr[u].append(v)
    arr[v].append(u)

for i in range(1,N+1):
    arr[i].sort()

# # DFS
q_1 = []
q_1.append(V)
ans_dfs = []
while q_1:
    r = q_1.pop()
    if visited_1[r]:
        continue
    visited_1[r] = True
    ans_dfs.append(r)
    for d in reversed(arr[r]):
        if not visited_1[d]:
            q_1.append(d)

print(*ans_dfs)

# BFS
q_2 = deque()
q_2.append(V)
visited_2[V] = True
ans_bfs = []
while q_2:
    r = q_2.popleft()
    ans_bfs.append(r)
    for d in arr[r]:
        if not visited_2[d]:
            q_2.append(d)
            visited_2[d] = True
print(*ans_bfs)
