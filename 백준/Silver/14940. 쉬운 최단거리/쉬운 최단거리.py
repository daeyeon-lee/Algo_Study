from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)] # 방문 체크용
dp = [[0] * m for _ in range(n)] # 거리 체크용


for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            startr,startc = i,j
q = deque()
q.append([startr,startc,1])
visited[startr][startc] = True # 방문체크
dp[startr][startc]

while q:
    r,c,cnt = q.popleft()
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
            if arr[nr][nc] == 0: # 못 가는 땅 패스
                dp[nr][nc] = 0
                visited[nr][nc] = True
                continue
            elif arr[nr][nc] == 1 : # 갈 수 있는 땅 -> cnt dp에 저장하고 큐에 추가
                dp[nr][nc] = cnt # cnt가 결국 거리
                visited[nr][nc] = True
                q.append([nr, nc, cnt+1])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]: # 다 돌았는데도 방문하지 못한 1(가능한 땅)은 -1로
            dp[i][j] = -1
for k in range(n):
    print(*dp[k])