from collections import deque
N, M = map(int,input().split())

def bfs(start):
    dist = [-1] * (N+1) # depth 기록용 배열
    q = deque([start]) # 시작점 넣기
    dist[start] = 0 # 시작점의 거리는 0

    while q:
        node = q.popleft()
        for next_node in friends[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + 1
                q.append(next_node)
    return sum(dist[1:])

friends = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())
    friends[u].append(v)
    friends[v].append(u)

ans = []
min_value = 2e21
for i in range(1,N+1):
    if bfs(i) < min_value:
        ans.clear()
        ans.append(i)
        min_value = bfs(i)
    elif bfs(i) == min_value:
        ans.append(i)
        min_value = bfs(i)
    else:
        continue
ans.sort()
print(ans[0])