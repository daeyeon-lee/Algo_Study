from collections import deque

dr = [0,0,-1,1]
dc = [-1,1,0,0]

N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


q = deque()
cnt = 1
q.append([0,0,cnt])
visited[0][0] = True
while q:
    r,c,cnt = q.popleft()
    if r == N-1 and c == M-1:
        break
    for d in range(4):
        nr,nc = r+dr[d], c+dc[d]
        if 0<=nr<N and 0<=nc<M and visited[nr][nc] == False:
            if arr[nr][nc] == 1:
                q.append([nr,nc,cnt+1])
                visited[nr][nc] = True
print(cnt)