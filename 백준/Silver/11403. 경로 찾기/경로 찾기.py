from collections import deque

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = [[0] * N for _ in range(N)]

for i in range(N):
    visited = [False] * N
    q = deque()
    q.append(i) # i에서 출발

    while q:
        node = q.popleft()
        for next_node in range(N):
            if arr[node][next_node] == 1 and not visited[next_node]: # 간선이 있고(1이고) 방문한적이 없다면
                visited[next_node] = True
                q.append(next_node)
    for j in range(N): # bfs 돌고 나서 방문한 곳은 1로 바꿈
        if visited[j]:
            ans[i][j] = 1

for i in ans:
    print(*i)