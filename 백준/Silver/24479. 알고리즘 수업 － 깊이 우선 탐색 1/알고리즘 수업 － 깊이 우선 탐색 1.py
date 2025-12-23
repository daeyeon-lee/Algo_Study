import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dfs(start):
    global cnt
    visited[start] = cnt
    for next_node in arr[start]:
        if not visited[next_node]:
            cnt += 1
            dfs(next_node)


N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1) # 순서 저장용
cnt = 1 # 순서

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1,N+1):
    arr[i].sort()

dfs(R)

for j in range(1, N+1):
    print(visited[j])