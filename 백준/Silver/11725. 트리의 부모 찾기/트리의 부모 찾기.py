from collections import deque

N = int(input())
node = [[] for _ in range(N+1)]
visited = [False] * (N+1)
q = deque()
start = 1
q.append(start)
visited[start] = True
for _ in range(N-1):
    w, v = map(int,input().split())
    node[w].append(v)
    node[v].append(w)


parent = [2e21] * (N+1)
while q:
    current_node = q.popleft()
    for next in node[current_node]:
        if visited[next] == False:
            q.append(next)
            visited[next] = True
            parent[next] = current_node

print('\n'.join(map(str,parent[2:])))