from collections import deque

n = int(input())
a, b = map(int,input().split()) # 촌수를 계산해야하는 서로 다른 두 사람
m = int(input())
family = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    family[x].append(y)
    family[y].append(x)


q = deque([a])
dist = [-1] * (n+1) # 촌수 계산
dist[a] = 0
ans = -1
while q:
    node = q.popleft()
    if node == b:
        ans = dist[node]
        break
    for next_node in family[node]:
        if dist[next_node] == -1:
            dist[next_node] = dist[node]+1
            q.append(next_node)
print(ans)