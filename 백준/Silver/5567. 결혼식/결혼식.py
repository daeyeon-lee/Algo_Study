from collections import deque

N = int(input())
M = int(input())
friends = [[] for _ in range(N+1)]
distance = [-1] * (N+1)
for _ in range(M):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)



q = deque()
q.append(1)
distance[1] = 0
while q:
    node = q.popleft()

    if distance[node] >= 2:
        break
    for next_node in friends[node]:
        if distance[next_node] == -1:
            distance[next_node] = distance[node] + 1
            q.append(next_node)

cnt = 0
for i in range(2,N+1):
    if distance[i] != -1:
       cnt += 1
print(cnt)