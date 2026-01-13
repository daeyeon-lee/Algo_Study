from collections import deque
def backtraking(start, depth):
    if depth == 4:
        print(1)
        exit()
    visited[start] = True
    for next in friends[start]:
        if not visited[next]:
            backtraking(next, depth + 1)
    visited[start] = False

N, M = map(int,input().split())
friends = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

ans = []
for _ in range(M):
    a, b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(N):
    backtraking(i,0)

print(0)