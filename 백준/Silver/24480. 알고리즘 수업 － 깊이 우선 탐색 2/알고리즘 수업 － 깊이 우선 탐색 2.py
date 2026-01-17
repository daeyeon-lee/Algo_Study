import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int,input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1,N+1):
    arr[i].sort(reverse=True) # 인접정점 내림차순 정렬

stack = []
stack.append(1)
cnt = 1 # 몇번째 방문인지 세주기 위함

def dfs(x):
    global cnt
    visited[x] = cnt
    for nx in arr[x]:
        if not visited[nx]:
            cnt += 1
            dfs(nx)
dfs(R)

for i in range(1,N+1):
    print(visited[i])

