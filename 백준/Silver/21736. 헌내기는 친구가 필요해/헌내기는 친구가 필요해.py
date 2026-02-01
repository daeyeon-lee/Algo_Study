from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]


N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


q = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            q.append([i,j])
cnt = 0
while q:
    r,c = q.popleft()
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if 0<=nr<N and 0<=nc<M and visited[nr][nc] == False:
            if arr[nr][nc] == "P":
                cnt += 1
                visited[nr][nc] = True
                q.append([nr,nc])
            if arr[nr][nc] == "X":
                continue
            if arr[nr][nc] == "O":
                visited[nr][nc] = True
                q.append([nr,nc])
if cnt == 0:
    print("TT")
else:
    print(cnt)
