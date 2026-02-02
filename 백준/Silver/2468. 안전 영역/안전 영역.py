from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]


max_height = 0 # 물 최대 높이 구하기
for r in range(N):
    for c in range(N):
        if arr[r][c] >= max_height:
            max_height = arr[r][c]
ans = 1 # 최소 안전영역의 개수는 1개
for h in range(max_height): # 물 높이 바꿀 때마다 visited 초기화
    visited = [[False] * N for _ in range(N)]
    cnt = 0 # 안전영역 개수

    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and not visited[i][j]: # 물높이보다 높고 방문하지 않은 곳이 시작점
                cnt += 1
                q = deque([(i,j)])
                visited[i][j] = True

                while q:
                    r,c = q.popleft()
                    for d in range(4):
                        nr, nc = r+dr[d],c+dc[d]
                        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                            if arr[nr][nc] <= h:
                                continue
                            if arr[nr][nc] > h:
                                q.append((nr,nc))
                                visited[nr][nc] = True
    ans = max(ans,cnt)
print(ans)
